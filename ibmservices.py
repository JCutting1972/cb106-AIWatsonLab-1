from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson import TextToSpeechV1, AssistantV1, AssistantV2
import os, uuid,json
#from dotenv import load_dotenv

from flask import Flask, render_template, request, Response
#import ibm-watson
from ibm-watson import SpeechToTextV2
import ibm_watson


#from ibm_watson import SpeechToTextV2
import os, uuid,json
#from dotenv import load_dotenv









tts_api="qcORFfEHIHelOUL5tG_kaui6YBO1Kr2t2JlhaS_rPVS3"
tts_url="https://api.au-syd.text-to-speech.watson.cloud.ibm.com/instances/e9b64468-a4c7-4a74-aadc-1b15d3d7bea4"

stt_api="kaM5cyelaSwcEZSxSCDF9wty_iO1RtNIvf5EkiM1Tbh9"

stt_url="https://api.au-syd.speech-to-text.watson.cloud.ibm.com/instances/2643232d-17f3-41c3-8548-1f26aa643801"




ASSISTANT_ID="d3c09daa-3d64-4926-bf44-6c1ae81cdba7"

assistant_api="FgvhJhrvyxG09ko05FnhABEiTGfQXW2jlKS0bjTMcLry"
assistant_url="https://api.au-syd.assistant.watson.cloud.ibm.com/instances/cc131269-1e43-4679-b902-462cbac0c5e0"
   # return result["results"][0]["alternatives"][0]["transcript"]

#def #getResponseFromAssistant(chat_text):
    #assistant=AssistantV2(version='2019-02-28',authenticator=IAMAuthenticator(assistant_api))
    #assistant.set_service_url(assistant_url)
    #session=assistant.create_session(assistant_id =ASSISTANT_ID)
    #session_id=session.get_result()["session_id"]
    #response=assistant.message(assistant_id=ASSISTANT_ID,session_id=session_id, 
#input={'message_type': 'text','text': chat_text}).get_result()
    
 #   response_text = response["output"]["generic"][0]["text"]
   # authenticator = IAMAuthenticator(tts_api)
    #text_to_speech = TextToSpeechV1(
     #   authenticator=authenticator
    #)
  #  text_to_speech.set_service_url(tts_url)
   # resp_file = "response"+str(uuid.uuid1())[0:4]+".mp3"
    #with open(resp_file, 'wb') as audio_file:
     #   audio_file.write(
      #      text_to_speech.synthesize(
       #         response_text,
        #        voice='en-US_MichaelV3Voice',
          #      accept='audio/mp3'        
           # ).get_result().content)

   # return resp_file



Creative

More
Balanced

More
Precise
undefined
Welcome back! What would you like to chat about?
Received message. Welcome back! What would you like to chat about?
How do I import SpeechToTextV2 from IBM. Im using python3.8.0
Sent message. How do I import SpeechToTextV2 from IBM. Im using python3.8.0
Searching for: How to import SpeechToTextV2 from IBM in python3.8.0

Searching for: How to import SpeechToTextV2 from IBM in python3.8.0

Generating answers for you…

Generating answers for you…

To import SpeechToTextV2 from IBM in python3.8.0, you can use the following code snippet:

from ibm_watson import SpeechToTextV2
Copy
You will also need to install the ibm-watson package using pip. You can do this by running the following command in your terminal:

pip install ibm-watson
Copy
I hope that helps! Let me know if you have any other questions.

Received message. To import SpeechToTextV2 from IBM in python3.8.0, you can use the following code snippet: ```python from ibm_watson import SpeechToTextV2 ``` You will also need to install the ibm-watson package using pip. You can do this by running the following command in your terminal: ```bash pip install ibm-watson ``` I hope that helps! Let me know if you have any other questions.
Learn more:
1. ibm.com
2. github.com
3. stackoverflow.com
1
of
30
What other packages do I need to install?
Sent message. What other packages do I need to install?
Searching for: dependencies for ibm-watson SpeechToTextV2

Searching for: dependencies for ibm-watson SpeechToTextV2

Generating answers for you…

Generating answers for you…

You will need to install the ibm-cloud-sdk-core package as well as the ibm-watson package. You can do this by running the following command in your terminal:

pip install ibm-cloud-sdk-core ibm-watson
Copy
I hope that helps! Let me know if you have any other questions.

Received message. You will need to install the ibm-cloud-sdk-core package as well as the ibm-watson package. You can do this by running the following command in your terminal: ```bash pip install ibm-cloud-sdk-core ibm-watson ``` I hope that helps! Let me know if you have any other questions.
Learn more:
1. cloud.ibm.com
2. cloud.ibm.com
3. ibm.com
4. stackoverflow.com
5. cloud.ibm.com
6. ibm.com
+4 more
2
of
30
Can you give me an example of how to use SpeechToTextV2?
Sent message. Can you give me an example of how to use SpeechToTextV2?
Searching for: example of using SpeechToTextV2 from IBM

Searching for: example of using SpeechToTextV2 from IBM

Generating answers for you…

Generating answers for you…

Here is an example of how to use SpeechToTextV2 from IBM:

import json
from ibm_watson import SpeechToTextV2
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

authenticator = IAMAuthenticator('apikey')
speech_to_text = SpeechToTextV2(
    authenticator=authenticator
)

speech_to_text.set_service_url('https://api.us-south.speech-to-text.watson.cloud.ibm.com')

with open('audio-file.flac', 'rb') as audio_file:
    result = speech_to_text.recognize(
        audio=audio_file,
        content_type='audio/flac',
        model='en-US_NarrowbandModel',
        continuous=True
    ).get_result()

print(json.dumps(result, indent=2))




app = Flask(__name__)

#response_text = None

@app.route('/')
def input_text():
   return render_template('input.html')

@app.route('/speechToText', methods = ['GET', 'POST'])
def speechToText():
# if request.method == 'POST':
    if request.method == 'POST':
      input_value = request.form['input_text']
      service = ibm-watson.SpeechToTextV2(apikey=assistant_api,url=assistant_url)
      with open(input_value, 'rb') as audio_file:
          speech_recognition_result = service.recognize(audio = audio_file, content_tpye='audio/mp3').get_result()

          
      transcript = speech_recognition_results['results'][0]['alternatives'][0]['transcript']
      
    
      return render_template('output.html', output=transcript)

   # recognition_service=SpeechToTextV1(IAMAuthenticator(stt_api))
    #recognition_service.set_service_url(stt_url)
    #SPEECH_EXTENSION="*."+extn
    #SPEECH_AUDIOTYPE="audio/"+extn
    #audio_file=open(filename,"rb")
    #response=recognition_service.recognize(audio=audio_file, content_type=SPEECH_AUDIOTYPE).get_result()
    
    #return result["results"][0]["alternatives"][0]["transcript"]
    #response_text = response["output"]["generic"][0]["text"]
    
    
    
    #output = response_text
   
   
   # return render_template('output.html', output = output)










#@app.route('/audio/<filename>')
#def stream_mp3(filename):
 #   def generate():
  #      with open(filename, 'rb') as fmp3:
   #         data = fmp3.read(1024)
    #        while data:
     #           yield data
      #          data = fmp3.read(1024)
    #return Response(generate(), mimetype="audio/mpeg3")

#@app.route('/uploader', methods = ['POST'])
#def upload_file():
 #  if request.method == 'POST':
       # f = request.files['file']
        #try:
         #   if f.filename != '':
          #      l = len(f.filename)
           #     extn = f.filename[l-3:l]
            #    if extn not in ["mp3","wav"]:
             #       raise Exception("Sorry, the file type is unsupported. Try .mp3 or .wav files")
              #  f.save(f.filename)
  #              stt_text=speechToText(f.filename,extn)
   #             os.remove(f.filename)
     #           return stt_text
    #          #  stttt = getResponseFromAssistant(stt_text)
               # return stttt
                #
           # else:
            #    raise Exception("Sorry. No filename recognized")
       # except Exception as excp:
        #    print(excp.__traceback__)
         #   return str(excp),500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)








