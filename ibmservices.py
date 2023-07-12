from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson import SpeechToTextV1, TextToSpeechV1, AssistantV2, AssistantV1
from flask import Flask, render_template, request, Response
import json, os


ASSISTANT_ID="d3c09daa-3d64-4926-bf44-6c1ae81cdba7"
tts_api="qcORFfEHIHelOUL5tG_kaui6YBO1Kr2t2JlhaS_rPVS3"
tts_url="https://api.au-syd.text-to-speech.watson.cloud.ibm.com/instances/e9b64468-a4c7-4a74-aadc-1b15d3d7bea4"
stt_api="kaM5cyelaSwcEZSxSCDF9wty_iO1RtNIvf5EkiM1Tbh9"
stt_url="https://api.au-syd.speech-to-text.watson.cloud.ibm.com/instances/2643232d-17f3-41c3-8548-1f26aa643801"
ASSISTANT_ID="d3c09daa-3d64-4926-bf44-6c1ae81cdba7"
assistant_api="FgvhJhrvyxG09ko05FnhABEiTGfQXW2jlKS0bjTMcLry"
assistant_url="https://api.au-syd.assistant.watson.cloud.ibm.com/instances/cc131269-1e43-4679-b902-462cbac0c5e0"


def speechToText(filename, extn):
    
    recognition_service=SpeechToTextV1(IAMAuthenticator(stt_api))
    recognition_service.set_service_url(stt_url)
    SPEECH_EXTENSION="*."+extn
    SPEECH_AUDIOTYPE="audio/"+extn
    audio_file=open(filename,"rb")
    result=recognition_service.recognize(audio=audio_file, content_type=SPEECH_AUDIOTYPE).get_result()
    return result["results"][0]["alternatives"][0]["transcript"]

    
def getResponseFromAssistant(response_text):   
   
    authenticator = IAMAuthenticator(tts_api)
    text_to_speech = TextToSpeechV1(authenticator=authenticator)
    text_to_speech.set_service_url(tts_url)
    filename = 'resp_file.mp3'
    with open(filename, 'wb') as audio_file:
        res = text_to_speech.synthesize(response_text,
         voice='en-US_MichaelV3Voice',accept='audio/mp3').get_result()
        audio_file.write(res.content)
    return filename
 
    


