from dotenv import load_dotenv
from flask import Flask, render_template, request, Response
from ibmservices import load_dotenv
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson import SpeechToTextV1,TextToSpeechV1, AssistantV1
import os, uuid,json
from dotenv import load_dotenv

import os

#app = flask('__Name_)

load_dotenv()

stt_api = os.environ['stt_api']

stt_url = os.environ['stt_url']

tts_api = os.environ['tts_api']
tts_url = os.environ['tts_url']

authenticator = IAMAuthenticator('sst_key')
speech_to_text = SpeechToTextV1(authenticator=authenticator)


speech_to_text.set_service_url('sst_url')
               
that_sound = hi.mp3                
with 
  open(that_sound, 'rb') as audio_file:
                 result = speech_to_text.recognize(audio=hi.mp3, content_type='audio/mp3', model='en-US_NarrowbandModel', continuous=True).get_result()

                 result = json.dumps(result, indent=2)
                 #parsed_response = json.loads(json_string)
                 #response = result["results"][0]["alternatives"][0]["transcript"]
                 print(result)
    
                
                 
  

#if __name__ == "__main__":
 #   app.run(host="0.0.0.0", port=8080)