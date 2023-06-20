from dotenv import load_dotenv
from flask import Flask, render_template, request, Response
from ibmservices import load_dotenv
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson import SpeechToTextV1,TextToSpeechV1, AssistantV1
import os, uuid,json
from dotenv import load_dotenv

import os

#app = flask('__Name__')
               
                
with open(hi.mp3) as audio_file:
                 result = speech_to_text.recognize(audio=audio_file, content_type='audio/mp3', model='en-US_NarrowbandModel', continuous=True).get_result()

                 json_string = json.dumps(result, indent=2)
                 parsed_response = json.loads(json_string)
                 response = result["results"][0]["alternatives"][0]["transcript"]
                 print(json_string)
    
                
                 
  

#if __name__ == "__main__":
 #   app.run(host="0.0.0.0", port=8080)