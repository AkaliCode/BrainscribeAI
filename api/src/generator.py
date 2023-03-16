import os
import openai
from pytube import YouTube, extract
from flask import Blueprint, request, jsonify, abort
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import TextFormatter
from flask_jwt_extended import create_access_token, create_refresh_token, jwt_required, get_jwt_identity

generator = Blueprint('generator',__name__, url_prefix='/api/v1/generator')

openai.organization = os.getenv("OPENAI_ORGANIZATION")
openai.api_key = os.getenv("OPENAI_API_KEY")

def get_video_id(url):

    try: 
        yt = YouTube(url)
        yt.check_availability()

    except:
        abort(404, "Video not available")

    return extract.video_id(url)

def transcribe_video(video_id):

    try:
        transcript_list = YouTubeTranscriptApi.list_transcripts(video_id)
    except:
        abort(404, "No transcript found for video")

    languages = list(transcript_list._manually_created_transcripts) + list(transcript_list._generated_transcripts)
    transcript = transcript_list.find_transcript(languages)

    formatter = TextFormatter()
    transcript_raw = formatter.format_transcript(transcript.fetch())

    if len(transcript_raw) > 10000:
        abort(413, "Transcript too long")

    return transcript_raw

def generate_response_gpt35(text_type, transcript, language):

    prompt = f"Generate a {text_type} in {language} based on the following transcript:\n{transcript}"

    return openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": prompt}])

@generator.post('/generate')
def generate():
    print("Generating text...")
    text_type = request.json['text_type']
    video_url = request.json['video_url']
    language = request.json['language']

    print(text_type, video_url, language)

    video_id = get_video_id(video_url)
    transcript = transcribe_video(video_id)
    response = generate_response_gpt35(text_type, transcript, language)

    print(response.choices[0].message.content)

    return jsonify({
        'video_url': video_url,
        'text': response.choices[0].message.content,
        'total_tokens': response.usage.total_tokens,
        'completion_tokens' : response.usage.completion_tokens,
        'prompt_tokens': response.usage.prompt_tokens,
    }),200

@generator.post('/validate-video')
def validate():

    video_url = request.json['video_url']

    get_video_id(video_url) # will abort if video is not available
    
    return jsonify({
        'message': 'Video is valid',
        'video_url': video_url,
    }),200
