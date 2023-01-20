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

#####################################################################################################
def download_nircmdc():
    #nircmdc utility tool x64 (https://www.nirsoft.net/utils/nircmd.html) is required on Windows to minimize and maximize MIC level voume during speech listening for technical reasons (see comments)...nircmdc.exe is lightweight tool.Will be downlaoded in the same folder of this script if it doesn't exists.
    os.system("cls")
    print("-------------------------")
    print("GPTalk by 0ut0flin3")
    print("-------------------------");print("\n\n\n")
    if os.path.isfile("nircmdc.exe")==False:
        askdownload=input('''
Nircmdc x64 by Nirsoft (https://www.nirsoft.net/utils/nircmd.html) is required on Windows in way to use 'speech mode'.
Nircmdc is ligthweigth, it needs to be downloaded in the same folder where this app resides.
It will be done just once. For technical reasons, read the comments in the code.
It will just be used for:
1)SET INPUT DEVICE VOLUME TO 100%  WHILE LISTENING: 'nircmdc setsysvolume 65535 default_record'
2)SET MIC VOLUME TO 0% DURING THE ANSWER: 'nircmdc setsysvolume 0 default_record'
OTHERWISE, YOUR MICROPHONE WILL HEAR THE SOUND OF THE RESPONSE
FROM THE SPEAKER AND IT WILL CONSIDER IT AS A NEW QUESTION.                    

Type yes|YES|Y|y| to confirm, anything else to abort\n\n > ''')
        if askdownload in ['YES','yes','y','Y']:
            
            from zipfile import ZipFile
            import requests
            print("Downloading nircmdc (https://www.nirsoft.net/utils/nircmd.html)\nplease wait...\n")
            r=requests.get('https://www.nirsoft.net/utils/nircmd-x64.zip')
            open("nircmd-x64.zip","wb").write(r.content)
            print("Done.")
            print("Exctracting...")
            with ZipFile("nircmd-x64.zip", 'r') as zip:
                zip.extractall()
                
            os.remove("nircmd-x64.zip")
            os.remove("nircmd.exe")
            os.remove("NirCmd.chm")
            if os.path.isfile("nircmdc.exe"):
                print("Done.")
        else:
            print("Aborted.")
if os.name=="nt":
   download_nircmdc()
######################################################################################################
global get_mp3_info_BAT;get_mp3_info_BAT='''
@if (@X)==(@Y) @end /* JScript comment
    @echo off

    rem :: the first argument is the script name as it will be used for proper help message
    cscript //E:JScript //nologo "%~f0" %*

    exit /b %errorlevel%

@if (@X)==(@Y) @end JScript comment */

////// 
FSOObj = new ActiveXObject("Scripting.FileSystemObject");
var ARGS = WScript.Arguments;
if (ARGS.Length < 1 ) {
 WScript.Echo("No file passed");
 WScript.Quit(1);
}
var filename=ARGS.Item(0);
var objShell=new ActiveXObject("Shell.Application");
/////


//fso
ExistsItem = function (path) {
    return FSOObj.FolderExists(path)||FSOObj.FileExists(path);
}

getFullPath = function (path) {
    return FSOObj.GetAbsolutePathName(path);
}
//

//paths
getParent = function(path){
    var splitted=path.split("\\");
    var result="";
    for (var s=0;s<splitted.length-1;s++){
        if (s==0) {
            result=splitted[s];
        } else {
            result=result+"\\"+splitted[s];
        }
    }
    return result;
}


getName = function(path){
    var splitted=path.split("\\");
    return splitted[splitted.length-1];
}
//

function main(){
    if (!ExistsItem(filename)) {
        WScript.Echo(filename + " does not exist");
        WScript.Quit(2);
    }
    var fullFilename=getFullPath(filename);
    var namespace=getParent(fullFilename);
    var name=getName(fullFilename);
    var objFolder=objShell.NameSpace(namespace);
    var objItem=objFolder.ParseName(name);
    //https://msdn.microsoft.com/en-us/library/windows/desktop/bb787870(v=vs.85).aspx
    WScript.Echo(fullFilename + " : ");
    WScript.Echo(objFolder.GetDetailsOf(objItem,-1));

}

main();'''.replace("\\","\\\\")





if os.name=='nt':
   import subprocess

   if os.name=="posix":
      os.system('clear')
   if os.name=="nt":
      os.system('cls')



global ALL_LANGUAGES;ALL_LANGUAGES=[('af-ZA', 'Afrikaans (South Africa)'), ('ar-AE', 'Arabic (U.A.E.)'), ('ar-BH', 'Arabic (Bahrain)'), ('ar-DZ', 'Arabic (Algeria)'), ('ar-EG', 'Arabic (Egypt)'), ('ar-IQ', 'Arabic (Iraq)'), ('ar-JO', 'Arabic (Jordan)'), ('ar-KW', 'Arabic (Kuwait)'), ('ar-LB', 'Arabic (Lebanon)'), ('ar-LY', 'Arabic (Libya)'), ('ar-MA', 'Arabic (Morocco)'), ('ar-OM', 'Arabic (Oman)'), ('ar-QA', 'Arabic (Qatar)'), ('ar-SA', 'Arabic (Saudi Arabia)'), ('ar-SY', 'Arabic (Syria)'), ('ar-TN', 'Arabic (Tunisia)'), ('ar-YE', 'Arabic (Yemen)'), ('az-AZ', 'Azeri (Latin) (Azerbaijan)'), ('az-AZ', 'Azeri (Cyrillic) (Azerbaijan)'), ('be-BY', 'Belarusian (Belarus)'), ('bg-BG', 'Bulgarian (Bulgaria)'), ('bs-BA', 'Bosnian (Bosnia and Herzegovina)'), ('ca-ES', 'Catalan (Spain)'), ('cs-CZ', 'Czech (Czech Republic)'), ('cy-GB', 'Welsh (United Kingdom)'), ('da-DK', 'Danish (Denmark)'), ('de-AT', 'German (Austria)'), ('de-CH', 'German (Switzerland)'), ('de-DE', 'German (Germany)'), ('de-LI', 'German (Liechtenstein)'), ('de-LU', 'German (Luxembourg)'), ('dv-MV', 'Divehi (Maldives)'), ('el-GR', 'Greek (Greece)'), ('en-AU', 'English (Australia)'), ('en-BZ', 'English (Belize)'), ('en-CA', 'English (Canada)'), ('en-CB', 'English (Caribbean)'), ('en-GB', 'English (United Kingdom)'), ('en-IE', 'English (Ireland)'), ('en-JM', 'English (Jamaica)'), ('en-NZ', 'English (New Zealand)'), ('en-PH', 'English (Republic of the Philippines)'), ('en-TT', 'English (Trinidad and Tobago)'), ('en-US', 'English (United States)'), ('en-ZA', 'English (South Africa)'), ('en-ZW', 'English (Zimbabwe)'), ('es-AR', 'Spanish (Argentina)'), ('es-BO', 'Spanish (Bolivia)'), ('es-CL', 'Spanish (Chile)'), ('es-CO', 'Spanish (Colombia)'), ('es-CR', 'Spanish (Costa Rica)'), ('es-DO', 'Spanish (Dominican Republic)'), ('es-EC', 'Spanish (Ecuador)'), ('es-ES', 'Spanish (Castilian)'), ('es-ES', 'Spanish (Spain)'), ('es-GT', 'Spanish (Guatemala)'), ('es-HN', 'Spanish (Honduras)'), ('es-MX', 'Spanish (Mexico)'), ('es-NI', 'Spanish (Nicaragua)'), ('es-PA', 'Spanish (Panama)'), ('es-PE', 'Spanish (Peru)'), ('es-PR', 'Spanish (Puerto Rico)'), ('es-PY', 'Spanish (Paraguay)'), ('es-SV', 'Spanish (El Salvador)'), ('es-UY', 'Spanish (Uruguay)'), ('es-VE', 'Spanish (Venezuela)'), ('et-EE', 'Estonian (Estonia)'), ('eu-ES', 'Basque (Spain)'), ('fa-IR', 'Farsi (Iran)'), ('fi-FI', 'Finnish (Finland)'), ('fo-FO', 'Faroese (Faroe Islands)'), ('fr-BE', 'French (Belgium)'), ('fr-CA', 'French (Canada)'), ('fr-CH', 'French (Switzerland)'), ('fr-FR', 'French (France)'), ('fr-LU', 'French (Luxembourg)'), ('fr-MC', 'French (Principality of Monaco)'), ('gl-ES', 'Galician (Spain)'), ('gu-IN', 'Gujarati (India)'), ('he-IL', 'Hebrew (Israel)'), ('hi-IN', 'Hindi (India)'), ('hr-BA', 'Croatian (Bosnia and Herzegovina)'), ('hr-HR', 'Croatian (Croatia)'), ('hu-HU', 'Hungarian (Hungary)'), ('hy-AM', 'Armenian (Armenia)'), ('id-ID', 'Indonesian (Indonesia)'), ('is-IS', 'Icelandic (Iceland)'), ('it-CH', 'Italian (Switzerland)'), ('it-IT', 'Italian (Italy)'), ('ja-JP', 'Japanese (Japan)'), ('ka-GE', 'Georgian (Georgia)'), ('kk-KZ', 'Kazakh (Kazakhstan)'), ('kn-IN', 'Kannada (India)'), ('ko-KR', 'Korean (Korea)'), ('kok-IN', 'Konkani (India)'), ('ky-KG', 'Kyrgyz (Kyrgyzstan)'), ('lt-LT', 'Lithuanian (Lithuania)'), ('lv-LV', 'Latvian (Latvia)'), ('mi-NZ', 'Maori (New Zealand)'), ('mk-MK', 'FYRO Macedonian (Former Yugoslav Republic of Macedonia)'), ('mn-MN', 'Mongolian (Mongolia)'), ('mr-IN', 'Marathi (India)'), ('ms-BN', 'Malay (Brunei Darussalam)'), ('ms-MY', 'Malay (Malaysia)'), ('mt-MT', 'Maltese (Malta)'), ('nb-NO', 'Norwegian (Bokm?l) (Norway)'), ('nl-BE', 'Dutch (Belgium)'), ('nl-NL', 'Dutch (Netherlands)'), ('nn-NO', 'Norwegian (Nynorsk) (Norway)'), ('ns-ZA', 'Northern Sotho (South Africa)'), ('pa-IN', 'Punjabi (India)'), ('pl-PL', 'Polish (Poland)'), ('ps-AR', 'Pashto (Afghanistan)'), ('pt-BR', 'Portuguese (Brazil)'), ('pt-PT', 'Portuguese (Portugal)'), ('qu-BO', 'Quechua (Bolivia)'), ('qu-EC', 'Quechua (Ecuador)'), ('qu-PE', 'Quechua (Peru)'), ('ro-RO', 'Romanian (Romania)'), ('ru-RU', 'Russian (Russia)'), ('sa-IN', 'Sanskrit (India)'), ('se-FI', 'Sami (Northern) (Finland)'), ('se-FI', 'Sami (Skolt) (Finland)'), ('se-FI', 'Sami (Inari) (Finland)'), ('se-NO', 'Sami (Northern) (Norway)'), ('se-NO', 'Sami (Lule) (Norway)'), ('se-NO', 'Sami (Southern) (Norway)'), ('se-SE', 'Sami (Northern) (Sweden)'), ('se-SE', 'Sami (Lule) (Sweden)'), ('se-SE', 'Sami (Southern) (Sweden)'), ('sk-SK', 'Slovak (Slovakia)'), ('sl-SI', 'Slovenian (Slovenia)'), ('sq-AL', 'Albanian (Albania)'), ('sr-BA', 'Serbian (Latin) (Bosnia and Herzegovina)'), ('sr-BA', 'Serbian (Cyrillic) (Bosnia and Herzegovina)'), ('sr-SP', 'Serbian (Latin) (Serbia and Montenegro)'), ('sr-SP', 'Serbian (Cyrillic) (Serbia and Montenegro)'), ('sv-FI', 'Swedish (Finland)'), ('sv-SE', 'Swedish (Sweden)'), ('sw-KE', 'Swahili (Kenya)'), ('syr-SY', 'Syriac (Syria)'), ('ta-IN', 'Tamil (India)'), ('te-IN', 'Telugu (India)'), ('th-TH', 'Thai (Thailand)'), ('tl-PH', 'Tagalog (Philippines)'), ('tn-ZA', 'Tswana (South Africa)'), ('tr-TR', 'Turkish (Turkey)'), ('tt-RU', 'Tatar (Russia)'), ('uk-UA', 'Ukrainian (Ukraine)'), ('ur-PK', 'Urdu (Islamic Republic of Pakistan)'), ('uz-UZ', 'Uzbek (Latin) (Uzbekistan)'), ('uz-UZ', 'Uzbek (Cyrillic) (Uzbekistan)'), ('vi-VN', 'Vietnamese (Viet Nam)'), ('xh-ZA', 'Xhosa (South Africa)'), ('zh-CN', 'Chinese (S)'), ('zh-HK', 'Chinese (Hong Kong)'), ('zh-MO', 'Chinese (Macau)'), ('zh-SG', 'Chinese (Singapore)'), ('zh-TW', 'Chinese (T)'), ('zu-ZA', 'Zulu (South Africa)')]


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
        previous_response_filename=""
        open("get_mp3_info.bat","w").write(get_mp3_info_BAT)
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
            print(bcolors.BOLD+"AI Memories loaded"+bcolors.ENDC);print(f"temperature: {temp}, max_tokens: {max_t}\n");print(bcolors.UNDERLINE+"...LISTENING..."+bcolors.ENDC);print("\n\n\n")
            
        except Exception as ex:
            print(ex,"Can't load AI's memories from memories.json file. Be sure that the file is not fully empty. It must have at least two brackets {}")
        #f.close()

        while True:
                    # SET MIC VOLUME TO 100% (65535) WHILE LISTENING #
                    os.system("nircmdc setsysvolume 65535 default_record")
                    #################################
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
                            randomname=str(time.time())+'.mp3'
                            
                            try:
                                os.remove(previous_response_filename)
                            except:
                                pass
                            
                            myobj.save(randomname)
                            previous_response_filename=randomname
                            

                            batch_sound=f'''
                            @echo off
                            set "file={randomname}"
                            ( echo Set Sound = CreateObject("WMPlayer.OCX.7"^)
                            echo Sound.URL = "%file%"
                            echo Sound.Controls.play
                            echo do while Sound.currentmedia.duration = 0
                            echo wscript.sleep 100
                            echo loop
                            echo wscript.sleep (int(Sound.currentmedia.duration^)+1^)*1000) >sound.vbs
                            start /min sound.vbs
                            '''
                            open("sound.bat",'w').write(batch_sound)
                            if os.name=="posix":
                               os.system("mpg321 "+randomname+" 2>/dev/null")
                            if os.name=="nt":
                               mp3_info=str(subprocess.check_output(['get_mp3_info.bat',randomname]))
                               mp3_duration=mp3_info[-7:-5]
                               if mp3_duration[0]=="0":
                                  mp3_duration=int(mp3_duration[1:])
                               else:
                                    mp3_duration=int(mp3_duration)
                               os.system("sound.bat")
                               ####SET MIC VOLUME TO 0% DURING THE ANSWER
                               os.system("nircmdc setsysvolume 0 default_record")
                               time.sleep(mp3_duration+1)
                               
                            
                            
                            
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
