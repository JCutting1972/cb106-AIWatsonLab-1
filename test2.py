from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson import TextToSpeechV1, AssistantV2, SpeechToTextV1, AssistantV1
import os, uuid,json
from flask import Flask, render_template, request, Response

from package import ibmservices
from package import getResponseFromAssistant
from package import speechToText

import urllib.request

tts_api="qcORFfEHIHelOUL5tG_kaui6YBO1Kr2t2JlhaS_rPVS3"
tts_url="https://api.au-syd.text-to-speech.watson.cloud.ibm.com/instances/e9b64468-a4c7-4a74-aadc-1b15d3d7bea4"

stt_api="kaM5cyelaSwcEZSxSCDF9wty_iO1RtNIvf5EkiM1Tbh9"

stt_url="https://api.au-syd.speech-to-text.watson.cloud.ibm.com/instances/2643232d-17f3-41c3-8548-1f26aa643801"

ASSISTANT_ID="d3c09daa-3d64-4926-bf44-6c1ae81cdba7"


assistant_api="FgvhJhrvyxG09ko05FnhABEiTGfQXW2jlKS0bjTMcLry"
assistant_url="https://api.au-syd.assistant.watson.cloud.ibm.com/instances/cc131269-1e43-4679-b902-462cbac0c5e0"

app = Flask(__name__)







   
   


@app.route('/')
def file_uploader():
   return render_template('upload.html')


  





@app.route('/uploader', methods = ['POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        try:
            if f.filename != '':
                l = len(f.filename)
                extn = f.filename[l-3:l]
                if extn not in ["mp3","wav"]:
                    raise Exception("Sorry, the file type is unsupported. Try .mp3 or .wav files")
                f.save(f.filename)
               # return 'hello'
                #return speechToText(f.filename,extn)
                filename = f.filename
               # os.remove(f.filename)
                def speechToText(filename, extn):
                 recognition_service=SpeechToTextV1(IAMAuthenticator(stt_api))
                 recognition_service.set_service_url(stt_url)
                 SPEECH_EXTENSION="*."+extn
                 SPEECH_AUDIOTYPE="audio/"+extn
                 audio_file=open(filename,"rb")
                 result=recognition_service.recognize(audio=audio_file, content_type=SPEECH_AUDIOTYPE).get_result()
                 return result["results"][0]["alternatives"][0]["transcript"]
                 transcript =  result['results'][0]['alteratives'][0]['transcript']
                 #os.remove(f.filename)
                 print(transcript)




            else:
              raise Exception("Sorry. No filename recognized")

    else:
              raise Exception("Sorry. No filename recognized")        
               #  assistant=AssistantV1(version='2019-02-28',authenticator=IAMAuthenticator(assistant_api))
               #  assistant.set_service_url(assistant_url)
                # session=assistant.create_session(assistant_id =ASSISTANT_ID)
                # session_id=session.get_result()["session_id"]
                # response=assistant.message(assistant_id=ASSISTANT_ID,session_id=session_id, 
               #  input={'message_type': 'text','text': transcript}).get_result()
               #  response_text = response["output"]["generic"][0]["text"]
                 
                 
                # print (response_text)
                 
                 #authenticator = IAMAuthenticator(tts_api)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)