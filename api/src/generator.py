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
    transcript = YouTubeTranscriptApi.get_transcript(video_id)
    formatter = TextFormatter()
    return formatter.format_transcript(transcript)

def generate_response(text_type, transcript):
    prompt = f"Generate a {text_type} based on the following transcript:\n{transcript}"
    print(prompt)
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        temperature=0.7,
        max_tokens=3000,
    )
    
    return response

def generate_bulletpoints(transcript):
    prompt = f"Generate a list of key topics based on the following transcript:\n{transcript}"
    print(prompt)
    response = openai.Completion.create(
        engine="text-babbage-001",
        prompt=prompt,
        temperature=0.7,
        max_tokens=2000,
    )
    
    return response

@generator.post('/generate')
def generate():
    text_type = request.json['text_type']
    video_id = request.json['video_id']

    #total_cost += engine_price[model_name]*get_tokens_consumed(response)

    print(video_id)
    print(text_type)

    transcript = transcribe_video(video_id)
    response = generate_response(text_type, transcript)

    return jsonify({
        'text': response.choices[0].text,
    })
    