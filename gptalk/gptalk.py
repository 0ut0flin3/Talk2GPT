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
import sys
if os.name=='nt':
   
   if os.name=="posix":
      os.system('clear')
   if os.name=="nt":
      os.system('cls')



global ALL_LANGUAGES;ALL_LANGUAGES=[('ar-SA', 'Arabic Saudi Arabia'), ('cs-CZ', 'Czech Czech Republic'), ('da-DK', 'Danish Denmark'), ('de-DE', 'German Germany'), ('el-GR', 'Modern Greek Greece'), ('en-AU', 'English Australia'), ('en-GB', 'English United Kingdom'), ('en-IE', 'English Ireland'), ('en-US', 'English United States'), ('en-ZA', 'English South Africa'), ('es-ES', 'Spanish Spain'), ('es-MX', 'Spanish Mexico'), ('fi-FI', 'Finnish Finland'), ('fr-CA', 'French Canada'), ('fr-FR', 'French France'), ('he-IL', 'Hebrew Israel'), ('hi-IN', 'Hindi India'), ('hu-HU', 'Hungarian Hungary'), ('id-ID', 'Indonesian Indonesia'), ('it-IT', 'Italian Italy'), ('ja-JP', 'Japanese Japan'), ('ko-KR', 'Korean Republic of Korea'), ('nl-BE', 'Dutch Belgium'), ('nl-NL', 'Dutch Netherlands'), ('no-NO', 'Norwegian Norway'), ('pl-PL', 'Polish Poland'), ('pt-BR', 'Portuguese Brazil'), ('pt-PT', 'Portuguese Portugal'), ('ro-RO', 'Romanian Romania'), ('ru-RU', 'Russian Russian Federation'), ('sk-SK', 'Slovak Slovakia'), ('sv-SE', 'Swedish Sweden'), ('th-TH', 'Thai Thailand'), ('tr-TR', 'Turkish Turkey'), ('zh-CN', 'Chinese China'), ('zh-HK', 'Chinese Hong Kong'), ('zh-TW', 'Chinese Taiwan')]


class apikey():
    def init(self, APIKEY):
        APIKEY=self.APIKEY
        openai.api_key=APIKEY
global set_APIKEY;set_APIKEY=apikey()
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
class CONFIGURE():
    def __init__(self,API_KEY,language='en-US',input_mode='speech',TEMPERATURE=1,MAX_TOKENS=3000,AI_NAME='AI', HUMAN_NAME='Human', AI_GENRE='undefined', HUMAN_HOBBIES='undefined', AI_HOBBIES='undefined',AI_SPECIES='undefined',AI_AGE='undefined',AI_MOOD='normal',HUMAN_AGE='undefined',HUMAN_GENRE='undefined',HUMAN_SPECIES='undefined',HUMAN_MOOD='undefined'):
        self.AI_NAME=AI_NAME
        self.HUMAN_NAME=HUMAN_NAME
        self.AI_GENRE=AI_GENRE
        self.HUMAN_HOBBIES=HUMAN_HOBBIES
        self.AI_HOBBIES=AI_HOBBIES
        self.AI_SPECIES=AI_SPECIES
        self.AI_AGE=AI_AGE
        self.AI_MOOD=AI_MOOD
        self.HUMAN_AGE=HUMAN_AGE
        self.HUMAN_GENRE=HUMAN_GENRE
        self.HUMAN_SPECIES=HUMAN_SPECIES
        self.HUMAN_MOOD=HUMAN_MOOD
        self.API_KEY=API_KEY
        self.language=language
        if TEMPERATURE<1.1:
           self.TEMPERATURE=TEMPERATURE
        if isinstance(MAX_TOKENS,int) and MAX_TOKENS<4098:
           self.MAX_TOKENS=MAX_TOKENS
        if input_mode in ['speech','text']:
           self.input_mode=input_mode
        else:
            print(f"'{input_mode}' is not a valid value for 'input_mode' so is been set automatically to 'speech' (default)\nAvailable values are: 'speech','text'\n'input_mode'")

        l=[x[0] for x in ALL_LANGUAGES]
        if self.language in l:
        
            
            print(bcolors.OKGREEN+"language '"+self.language+"' has been set up."+bcolors.ENDC)
        else:
            print(bcolors.WARNING+"Language '"+self.language+"' is not a valid language."+bcolors.ENDC)    
    def save(self):    
        try:
            AI_CONFIG={f"Your name is {self.AI_NAME}, you are {self.AI_SPECIES}, your genre is {self.AI_GENRE}, your age is {self.AI_AGE}, your hobbies are: {self.AI_HOBBIES}.Reply to questions with an {self.AI_MOOD} tone. My name is {self.HUMAN_NAME}, I\'m not a human, I am {self.HUMAN_SPECIES}, my genre is {self.HUMAN_GENRE}, my age is {self.HUMAN_AGE}, my hobbies are {self.HUMAN_HOBBIES}, today i am in a {self.HUMAN_MOOD} mood":f"Ok, my name is {self.AI_NAME}, i am {self.AI_SPECIES}, my genre is {self.AI_GENRE}, my age is {self.AI_AGE}, my hobbies are: {self.AI_HOBBIES}. I will reply to questions with an {self.AI_MOOD} tone. your name is {self.HUMAN_NAME}, you are not a human, you are {self.HUMAN_SPECIES}, your genre is {self.HUMAN_GENRE}, your age is {self.HUMAN_AGE}, your hobbies are {self.HUMAN_HOBBIES},today you are in a {self.HUMAN_MOOD} mood"}
            m=open("memories.json","w")
            
            jjj=json.dump(AI_CONFIG,m)
            #m.close()
        except Exception as ex:
            print(ex)
    def run(self):
        gptalk(self.API_KEY,self.input_mode,self.language,self.language[:2],self.AI_NAME,self.HUMAN_NAME,self.TEMPERATURE,self.MAX_TOKENS)
    


print("-------------------------")
print("GPTalk by 0ut0flin3")
print("-------------------------")
print(bcolors.OKGREEN+"If you found this software useful please consider a donation: https://github.com/0ut0flin3/GPTalk#donate"+bcolors.ENDC)
print("-------------------------");print("\n\n\n")


         
    

              
     

# WRITTEN BY 0UT0FLIN3 (github.com/0ut0flin3)#### 0UT0FLIN3@PROTONMAIL.COM ####
###SPECIAL THANKS <3 TO: https://github.com/openai/openai-python, https://github.com/Uberi/speech_recognition, https://github.com/pndurette/gTTS
# DONATE BTC: 17AnP1zuvLV9cQrGQi6H6qMLeWeujHzAYX 

#REQUIREMENTS: YOU NEED TO INSTALL MPG321 MP3 PLAYER IF YOU'RE USING LINUX#










def gptalk(apik,inpmod,l1,l2,ainame,humanname,temp,max_t):
    
    

    openai.api_key = apik
    
    global memories
    global pr
    global f
    pr=""
    if inpmod not in ['speech','text']:
        print("No valid input_mode selected. Available modes: 'text', 'speech'")
    if inpmod=='speech':
        if os.name=='nt':
            try:
                from pygame import mixer,quit
            except Exception as exxx:
                print(exxx)
        r = speech_recognition.Recognizer()
        def convert_speech_to_text():
        
            
            with speech_recognition.Microphone() as source:
                audio = r.listen(source)
        
            
            try:
                text = r.recognize_google(audio,language=l1, show_all=True)
                if text==[]:
                   pass
                return text['alternative'][0]['transcript']
            except:
                pass

        try:
            f=open("memories.json","r")
            memories=json.load(f)
            for m in memories:
                pr=pr+"Human: "+m+"\nAI:"+memories[m]+"\n"
            
            print("-------------------------")
            print("GPTalk [speech mode] by 0ut0flin3")
            print("-------------------------")
            print(bcolors.OKGREEN+"If you found this software useful please consider a donation: https://github.com/0ut0flin3/GPTalk#donate"+bcolors.ENDC)
            print("-------------------------");print("\n\n")
            print(bcolors.BOLD+"AI Memories loaded\n\n"+bcolors.ENDC);print(f"temperature: {temp}, max_tokens: {max_t}");print("\n\n\n")
            
        except Exception as ex:
            print(ex,"Can't load AI's memories from memories.json file. Be sure that the file is not fully empty. It must have at least two brackets {}")
        #f.close()

        while True:
                    
                    
                    q=convert_speech_to_text()
                    if q==None:
                       continue
                    else:
                            
                            print(bcolors.OKCYAN+humanname+": "+bcolors.ENDC+q)
                            print('\n')
                            t1=time.time()
                            if isinstance(q,str):
                                try:
                                    response = openai.Completion.create(
                                    model="text-davinci-003",
                                    
                                    
                                    prompt=pr+"Human: "+q+"\nAI:\n",
                                    temperature=temp,
                                    max_tokens=max_t,
                                    top_p=1,
                                    
                                    frequency_penalty=0.0,
                                    presence_penalty=0.0,
                                    stop=[" Human:", " AI:"],
                                    
                                    )
                                except Exception as exx:
                                    print(exx)


                            t2=time.time()
                            
                            pr = pr+"Human: "+q+"\nAI: "+response.choices[0].text+"\n"
                            memories.update({q:response.choices[0].text})
                            
                            ff=open("memories.json","w")
                            j=json.dump(memories,ff)
                            ff.close()
                            print(bcolors.HEADER+ainame+": "+bcolors.ENDC+response.choices[0].text)
                            print("\n\n["+str(t2-t1)[:4]+" seconds]\n\n")
                            myobj = gTTS(text=response.choices[0].text, lang=l2, slow=False)
                            myobj.save("answer.mp3")
                            
                            if os.name=="posix":
                               os.system("mpg321 answer.mp3 2>/dev/null")
                            if os.name=="nt":
                               mixer.init()
                               mixer.music.load("answer.mp3")
                               mixer.music.play()
                               while mixer.music.get_busy():
                                     pass
                               quit()
                               os.remove('answer.mp3')


                            
                            
                            
                            print('\n')
                            
                            if q in EXIT:
                               break


    if inpmod=='text':

        pr=""
        try:
            f=open("memories.json","r")
            memories=json.load(f)
            for m in memories:
                pr=pr+"Human: "+m+"\nAI:"+memories[m]+"\n"
            
            print("-------------------------")
            print("GPTalk [text mode] by 0ut0flin3")
            print("-------------------------")
            print(bcolors.OKGREEN+"If you found this software useful please consider a donation: https://github.com/0ut0flin3/GPTalk#donate"+bcolors.ENDC)
            print("-------------------------");print("\n\n")
            print(bcolors.BOLD+"AI Memories loaded\n\n"+bcolors.ENDC);print(f"temperature: {temp}, max_tokens: {max_t}");print("\n\n\n")
            
        except Exception as ex:
            print(ex,"Can't load AI's memories from memories.json file. Be sure that the file is not fully empty. It must have at least two brackets {}")
        while True:
            q=input(bcolors.OKCYAN+humanname+": "+bcolors.ENDC)
            print('\n')
            t1=time.time()
                                
            try:
                
                response = openai.Completion.create(
                model="text-davinci-003",
                
                
                prompt=pr+"Human: "+q+"\nAI:\n",
                temperature=temp,
                max_tokens=max_t,
                top_p=1,
                
                frequency_penalty=0.0,
                presence_penalty=0.0,
                stop=[" Human:", " AI:"],
                
                )
            except Exception as exx:
                print(exx)


            t2=time.time()
        
            pr = pr+"Human: "+q+"\nAI: "+response.choices[0].text+"\n"
            memories.update({q:response.choices[0].text})
        
            ff=open("memories.json","w")
            j=json.dump(memories,ff)
            ff.close()
            print(bcolors.HEADER+ainame+": "+bcolors.ENDC+response.choices[0].text)
            print("\n\n["+str(t2-t1)[:4]+" seconds]\n\n")
