'''
MIT License
Copyright (c) 2022 0ut0flin3
Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
'''

import speech_recognition
from gtts import gTTS
import openai
import json
import os
import time
if os.name=='nt':
   import playsound

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
global EXIT;EXIT=['exit','quit','goodbye','exit now','go to sleep','shutdown','go for a walk','goodnight']

global AI_NAME, HUMAN_NAME, AI_GENRE, HUMAN_HOBBIES, AI_HOBBIES,AI_SPECIES,AI_AGE,AI_MOOD,HUMAN_AGE,HUMAN_GENRE,HUMAN_SPECIES,HUMAN_MOOD
global LOL

print("-------------------------")
print("GPTalk by 0ut0flin3")
print("-------------------------")
print(bcolors.OKGREEN+"If you found this software useful please consider a donation: https://github.com/0ut0flin3/GPTalk#donate"+bcolors.ENDC)
print("-------------------------");print("\n\n\n")

def wanttocustomize():

    ww=input("Want to customize the looks, details, and behavior of the AI? (Y/N) > ")
    if ww in ['yes','YES','y','Y']:
        return True
    elif ww in ["no",'NO','n','N']:
        return False
    else:
         return None
         
    
def custom_inputs():
    global LOL
    if wanttocustomize()==True:
        AI_SPECIES=input(bcolors.HEADER+"Of which living species (or not) should the AI ​​be? (a human, a cat, a vegetable, a tree or anything else...)\n Choose what the AI ​​will be.\n This AI will be... "+bcolors.ENDC)
        print('\n\n')
        AI_GENRE=input(bcolors.HEADER+"Choose the genre for the AI (male, female, ...): "+bcolors.ENDC)
        print('\n\n')
        AI_NAME=input(bcolors.HEADER+"Choose a name for the AI:   "+bcolors.ENDC)
        print('\n\n')
        AI_AGE=input(bcolors.HEADER+"Choose an age for the AI:   "+bcolors.ENDC)
        print('\n\n')
        AI_HOBBIES=input(bcolors.HEADER+"Choose some hobbies that the AI will have:   "+bcolors.ENDC)
        print('\n\n')
        AI_MOOD=input(bcolors.HEADER+"Choose a mood for the AI (e.g. happy, angry):   "+bcolors.ENDC)
        print('\n\n\n\n')
        HUMAN_SPECIES=input(bcolors.HEADER+"Of which living species (or not) should YOU ​​be? (Human, animal, a vegetable, a tree, anything..)\nChoose what YOU ​​will be.\n I am...    "+bcolors.ENDC)
        print('\n\n')
        HUMAN_GENRE=input(bcolors.HEADER+"Choose you genre (male, female, ...):   "+bcolors.ENDC)
        print('\n\n')
        HUMAN_NAME=input(bcolors.HEADER+"Your name:   "+bcolors.ENDC)
        print('\n\n')
        HUMAN_AGE=input(bcolors.HEADER+"Your age:   "+bcolors.ENDC)
        print('\n\n')
        HUMAN_HOBBIES=input(bcolors.HEADER+"Your hobbies: "+bcolors.ENDC)
              
        LOL_0=f"Your name is {AI_NAME}, you are {AI_SPECIES}, your genre is {AI_GENRE}, your age is {AI_AGE}, your hobbies are: {AI_HOBBIES}.Reply to questions with an {AI_MOOD} tone. My name is {HUMAN_NAME}, I'm not a human, I am {HUMAN_SPECIES}, my genre is {HUMAN_GENRE}, my age is {HUMAN_AGE}, my hobbies are {HUMAN_HOBBIES}"
        LOL_1=f"Ok, my name is {AI_NAME}, i am {AI_SPECIES}, my genre is {AI_GENRE}, my age is {AI_AGE}, my hobbies are: {AI_HOBBIES}. I'll reply to questions with an {AI_MOOD} tone. your name is {HUMAN_NAME}, you are not a human, you are {HUMAN_SPECIES}, your genre is {HUMAN_GENRE}, your age is {HUMAN_AGE}, your hobbies are {HUMAN_HOBBIES}"
        LOL={'':[],LOL_0:LOL_1}
    else:
        LOL=''

# WRITTEN BY 0UT0FLIN3 (github.com/0ut0flin3)#### 0UT0FLIN3@PROTONMAIL.COM ####
###SPECIAL THANKS <3 TO: https://github.com/openai/openai-python, https://github.com/Uberi/speech_recognition, https://github.com/pndurette/gTTS
# DONATE BTC: 17AnP1zuvLV9cQrGQi6H6qMLeWeujHzAYX 

#REQUIREMENTS: YOU NEED TO INSTALL MPG321 MP3 PLAYER IF YOU'RE USING LINUX#







#### READ!! First of all, kill all other existent python3 processes because cause mistakes with speech_recognition module (just for me,if you're not affected you can remove this part of code)

try:
    import subprocess
    import os
    if os.name=="posix":
        pyproc=subprocess.check_output(['pidof', 'python3', '2>/dev/null']).decode()
        pyproc=pyproc.replace("\n","")
        pyproc=pyproc.split()[1:]
        for proc in pyproc:
            os.system("kill -9 "+proc)
    if os
except:
       pass
       
################################################


#### Set language you choose from speech_language.json file#####
try:
    speechlang=open("speech_language.json","r")
    jsonf=json.load(speechlang)
    global LANGUAGE_SR_FORMAT
    global LANGUAGE_GTTS_FORMAT
    LANGUAGE_SR_FORMAT=jsonf["language"][0]
    LANGUAGE_GTTS_FORMAT=jsonf["language"][0][:2]
    
except:
       print("Can't find\open speech_language.json file")
#################################################


def main():

    if os.name=="posix":
       os.system('clear')
    if os.name=="nt":
       os.system('cls')
    openai.api_key = os.getenv("OPENAI_API_KEY") 
    
    global memories
    global pr
    global f
    pr=""
    r = speech_recognition.Recognizer()
    def convert_speech_to_text():
     
        
        with speech_recognition.Microphone() as source:
            audio = r.listen(source)
     
        
        try:
            text = r.recognize_google(audio,language=LANGUAGE_SR_FORMAT, show_all=True)
            return text['alternative'][0]['transcript']
        except:
               pass

    try:
        f=open("memories.json","r")
        memories=json.load(f)
        if len(list(memories))==0:
            
           memories.update(LOL)

        for m in memories:
                    if m=='':
                        continue
                    pr=pr+"Human: "+m+"\nAI:"+memories[m]+"\n"
        
        print("-------------------------")
        print("GPTalk by 0ut0flin3")
        print("-------------------------")
        print(bcolors.OKGREEN+"If you found this software useful please consider a donation: https://github.com/0ut0flin3/GPTalk#donate"+bcolors.ENDC)
        print("-------------------------");print("\n\n")
        print(bcolors.BOLD+"AI Memories loaded\n\n"+bcolors.ENDC);print("\n\n\n")
    except Exception as ex:
           print(ex,"Can't load AI's memories from memories.json file. Be sure that the file is not fully empty. It must have at least two brackets {}")
    f.close()

    while True:
                
                
                q=convert_speech_to_text()
                if q==None:
                   continue
                else:
                        print(bcolors.OKCYAN+"Human: "+bcolors.ENDC+q)
                        print('\n')
                        t1=time.time()
                        if isinstance(q,str):
                            response = openai.Completion.create(
                            model="text-davinci-003",
                            
                            
                            prompt=pr+"Human: "+q+"\nAI:\n",
                            temperature=1,
                            max_tokens=3000,
                            top_p=1,
                            
                            frequency_penalty=0.0,
                            presence_penalty=0.0,
                            stop=[" Human:", " AI:"],
                            
                            )
                        t2=time.time()
                        
                        pr = pr+"Human: "+q+"\nAI: "+response.choices[0].text+"\n"
                        memories.update({q:response.choices[0].text})
                        
                        ff=open("memories.json","w")
                        j=json.dump(memories,ff)
                        ff.close()
                        print(bcolors.HEADER+"AI: "+bcolors.ENDC+response.choices[0].text)
                        print("\n\n["+str(t2-t1)[:4]+" seconds]\n\n")
                        myobj = gTTS(text=response.choices[0].text, lang=LANGUAGE_GTTS_FORMAT, slow=False)
                        myobj.save("answer.mp3")
                        if os.name=="posix":
                           os.system("mpg321 answer.mp3")
                        if os.name=="nt":
                           p = playsound.playsound("answer.mp3")
                        
                        print("If you found this software useful please consider a donation: https://github.com/0ut0flin3/VoiceGPT#donate")
                         
                        print('\n')
                        
                        if q in EXIT:
                           break
                        
if os.path.isfile("memories.json"):
   
    ff=open("memories.json","r")
    mem=json.load(ff)
    if len(mem)>0:
        ccc=input('''Some memories already exist. Do you want to import it? or reset all previous memories?If you import already existing memories, obviously, it will not be possible to re-customize the AI ​aspects again, since they are already imprinted in the memory you will import and different memories would intertwine.Otherwise, if you choose to reset memories, '''+bcolors.WARNING+'''ALL PREVIOUS INTERACTIONS WILL BE ERASED and LOST FOREVER '''+bcolors.ENDC+'''and you can customize a new AI in the next step.If you press ENTER or type anything other than RESET (uppercase), the memories will be imported.(Press ENTER to import / type RESET to reset) >   ''')
        if ccc=="RESET" :
            mem={}
            fff=open("memories.json","w")
            jjj=json.dump(mem,fff)
            fff.close()
            print(bcolors.WARNING+"AI memories have been reset."+bcolors.ENDC);print('\n\n')
            custom_inputs();main()
    else:
         custom_inputs()
main()
