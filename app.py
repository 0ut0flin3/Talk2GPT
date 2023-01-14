import speech_recognition
from gtts import gTTS
import openai
import json
import os
import time
if os.name=='nt':
   import playsound




# WRITTEN BY 0UT0FLIN3 #### 0UT0FLIN3@PROTONMAIL.COM ####
###SPECIAL THANKS <3 TO: https://github.com/openai/openai-python, https://github.com/Uberi/speech_recognition, https://github.com/pndurette/gTTS
##TESTED ON UBUNTU 22.10#########
##WILL NOT WORK ON WINDOWS######

#REQUIREMENTS: YOU NEED TO INSTALL MPG321 MP3 PLAYER#







#### READ!! First of all, kill all other existent python3 processes because cause mistakes with speech_recognition module (just for me,if you're not affected you can remove this part of code)
import subprocess
import os
if os.name=="posix":
	pyproc=subprocess.check_output(['pidof', 'python3']).decode()
	pyproc=pyproc.replace("\n","")
	pyproc=pyproc.split()[1:]
	for proc in pyproc:
	    os.system("kill -9 "+proc)
################################################


#### Set language you choose from speech_language.json file#####
try:
    speechlang=open("speech_language.json","r")
    jsonf=json.load(speechlang)
    global LANGUAGE_SR_FORMAT
    global LANGUAGE_GTTS_FORMAT
    LANGUAGE_SR_FORMAT=jsonf["language"][0]
    LANGUAGE_GTTS_FORMAT=jsonf["language"][0][:2]
    print(LANGUAGE_GTTS_FORMAT)
except:
       print("Can't find\open speech_language.json file")
#################################################


def main():

    
    os.system('clear')
    openai.api_key = os.getenv("OPENAI_API_KEY") 
    
    global memories
    global pr
    global f
    pr=""
    r = speech_recognition.Recognizer()
    def convert_speech_to_text():
     
        # capture the audio
        with speech_recognition.Microphone() as source:
            audio = r.listen(source)
     
        # convert the speech to text
        try:
            text = r.recognize_google(audio,language=LANGUAGE_SR_FORMAT, show_all=True)
            return text['alternative'][0]['transcript']
        except:
               pass

    try:
        f=open("memories.json","r")
        memories=json.load(f)
        for m in memories:
                    pr=pr+"Human: "+m+"\nAI:"+memories[m]+"\n"
        print("-------------------------")
        print("OPENAI's text-davinci-003")
        print("-------------------------")
        print("AI Memories loaded\n\n")
    except:
           print("Can't load AI's memories from memories.json file. Be sure that the file is not fully empty. It must have at least two brackets {}")
    f.close()

    while True:

                
                q=convert_speech_to_text()
                print("Human: "+q)
                print('\n')
                t1=time.time()
                if isinstance(q,str):
                    response = openai.Completion.create(
                      model="text-davinci-002",
                      
                      
                      prompt=pr+"Human: "+q+"\nAI:\n",
                      temperature=1,
                      max_tokens=3000,
                      top_p=1,
                      
                      frequency_penalty=0.0,
                      presence_penalty=0.0,
                      stop=[" Human:", " AI:"],
                      
                    )
                t2=time.time()
                #print("response ok")
                memories.update({q:response.choices[0].text})
                
                ff=open("memories.json","w")
                j=json.dump(memories,ff)
                ff.close()
                print("AI: "+response.choices[0].text)
                print("\n\n["+str(t2-t1)[:4]+" seconds]\n\n")
                myobj = gTTS(text=response.choices[0].text, lang=LANGUAGE_GTTS_FORMAT, slow=False)
                myobj.save("answer.mp3")
                if os.name=="posix":
                   os.system("mpg321 answer.mp3")
                if os.name=="nt":
                   p = playsound.playsound("answer.mp3")
                   
                
                print('\n')
                

main()
