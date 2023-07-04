from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson import TextToSpeechV1, AssistantV2, SpeechToTextV1, AssistantV1
import os, uuid,json
from flask import Flask, render_template, request, Response

from package import ibmservices

import urllib.request

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
   return render_template('input3.html')

@app.route('/upload',methods = ['POST'])
def upload():
    

    
    if request.method == 'POST':

        import urllib.request
        urllib.request.urlretrieve("http://www.example.com/songs/mp3.mp3", "mp3.mp3")        

        audio_file = request.files['audio']
       # return 'audio file uploaded successfully!'
        
        
        
        return render_template("output.html", output = "Hello")


    
   # stt_text = ibmservices.speechToText('file',"mp3")
               # os.remove(f.filename)
                #jason_string = json.dumps(stt_text)
                #{"results":[ {"alternatives": [ {"transript: "the text", "confidence": .87}], "final": truee}]}
                
                
               # response1 = ibmservices.getResponseFromAssistant(stt_text)
    #transcript = stt_text['results'][0]['alternatives'][0]['transcript']
                #print(transcript)
                #output = json.loads(transcript)

               
    #return  render_template("output.html",output= output)
                
           # else: 
           #     raise Exception("Sorry. No filename recognized")
        #except Exception as excp:
        #    print(excp.__traceback__)
        #    return str(excp),500
        #    output = transcript
        #    render_tenplate("output.html",output=output)
       

if __name__ == "__main__":
        app.run(host="0.0.0.0", port=8080)
 