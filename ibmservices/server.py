from dotenv import load_dotenv
from flask import Flask, render_template, request, Response
from ibmservices import load_dotenv
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson import SpeechToTextV1,TextToSpeechV1, AssistantV1
import os, uuid,json
from dotenv import load_dotenv

import os

app = Flask(__name__)
response_text = None
Response = 'error9'

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
               
                
                with open(f. filename, 'rb') as audio_file:
                 result = speech_to_text.recognize(audio=audio_file, content_type='audio/mp3', model='en-US_NarrowbandModel', continuous=True).get_result()

                 json_string = json.dumps(result, indent=2)
                 parsed_response = json.loads(json_string)
                 response = result["results"][0]["alternatives"][0]["transcript"]
                 print(json_string)
    
                
                 
                 #response = json_string

               
               # stt_text=ibmservices.speechToText(f.filename,extn)
               # os.remove(f.filename)
                #return response
            else:
                raise Exception("Sorry. No filename recognized")
        except Exception as excp:
            print(excp.__traceback__)
            return str(excp),500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)