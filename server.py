
from flask import Flask, render_template, request, Response

import os

from ibmservices import speechToText, getResponseFromAssistant


from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson import SpeechToTextV1,TextToSpeechV1, AssistantV1, AssistantV2
import os, uuid,json
#from dotenv import load_dotenv




tts_api="qcORFfEHIHelOUL5tG_kaui6YBO1Kr2t2JlhaS_rPVS3"
tts_url="https://api.au-syd.text-to-speech.watson.cloud.ibm.com/instances/e9b64468-a4c7-4a74-aadc-1b15d3d7bea4"

stt_api="kaM5cyelaSwcEZSxSCDF9wty_iO1RtNIvf5EkiM1Tbh9"

stt_url="https://api.au-syd.speech-to-text.watson.cloud.ibm.com/instances/2643232d-17f3-41c3-8548-1f26aa643801"

ASSISTANT_ID="d3c09daa-3d64-4926-bf44-6c1ae81cdba7"

assistant_api="FgvhJhrvyxG09ko05FnhABEiTGfQXW2jlKS0bjTMcLry"
assistant_url="https://api.au-syd.assistant.watson.cloud.ibm.com/instances/cc131269-1e43-4679-b902-462cbac0c5e0"


app = Flask(__name__)
response_text = None

@app.route('/')
def file_uploader():
   return render_template('upload.html')

@app.route('/audio/<filename>')
def stream_mp3(filename):
    def generate():
        with open(filename, 'rb') as fmp3:
            data = fmp3.read(1024)
            while data:
                yield data
                data = fmp3.read(1024)
    return Response(generate(), mimetype="audio/mpeg3")

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
                stt_text=ibmservices.speechToText(f.filename, extn)
                os.remove(f.filename)

                return ibmservices.getResponseFromAssistant(stt_text)
            else:
                raise Exception("Sorry. No filename recognized")
        except Exception as excp:
            print(excp.__traceback__)
            return str(excp),500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)  