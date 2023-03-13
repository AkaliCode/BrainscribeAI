import os
import openai
from flask import Blueprint, request, jsonify, abort
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import TextFormatter
from flask_jwt_extended import create_access_token, create_refresh_token, jwt_required, get_jwt_identity

generator = Blueprint('generator',__name__, url_prefix='/api/v1/generator')

openai.organization = "org-qzx7KtwC7edug82IJeee0SmF"
openai.api_key = os.getenv("OPENAI_API_KEY")

def transcribe_video(video_id):
    transcript_list = YouTubeTranscriptApi.list_transcripts(video_id)

    languages = list(transcript_list._manually_created_transcripts) + list(transcript_list._generated_transcripts)

    if languages == []:
        abort(404, "No transcript found for video")

    transcript = transcript_list.find_transcript(languages)

    formatter = TextFormatter()
    return formatter.format_transcript(transcript.fetch())

def generate_response_gpt35(text_type, transcript):
    prompt = f"Generate a {text_type} based on the following transcript:\n{transcript}"
    
    response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": prompt}])
    
    return response

@generator.post('/generate')
def generate():
    text_type = request.json['text_type']
    video_id = request.json['video_id']

    print(video_id)
    print(text_type)

    transcript = transcribe_video(video_id)
    response = generate_response_gpt35(text_type, transcript)

    # get the number of tokens used to generate the response
    tokens_used = response.usage.total_tokens
    print(f"Tokens used: {tokens_used}")


    return jsonify({
        'text': response.choices[0].message.content,
        'total_tokens': response.usage.total_tokens,
        'completion_tokens' : response.usage.completion_tokens,
        'prompt_tokens': response.usage.prompt_tokens,
    })
    