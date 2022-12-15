# openai-davinci003-python-speech
A Python script to use OpenAI's text-davinci-003 model using your own voice instead of text.
[requirments-and-how-to-use (PLEASE READ FIRST!)](https://github.com/0ut0flin3/openai-davinci003-python-speech/blob/main/README.md#requirments-and-how-to-use-read-please)
[Start the app](https://github.com/0ut0flin3/openai-davinci003-python-speech/blob/main/README.md#start-the-app)


## REQUIRMENTS and HOW TO USE (READ PLEASE!)
-This script doesn't work on Windows, only work on Linux Ubuntu (tested on Ubuntu 22.10)

-In order to use this script you need to install these Python modules: `openai`,`SpeechRecognition`,`gTTS`,`PyAudio`
**If you have some mistakes in installing PyAudio read this topic: [https://stackoverflow.com/questions/20023131/cannot-install-pyaudio-gcc-error](https://stackoverflow.com/questions/20023131/cannot-install-pyaudio-gcc-error)**

-You need to have your OpenAI's Api key inside the OPENAI_API_KEY environment variable

So, first of all, install required modules:

`pip install openai`

`pip install SpeechRecognition`

`pip install gTTS`

`pip install PyAudio`

**If you have some mistakes in installing PyAudio read this topic: [https://stackoverflow.com/questions/20023131/cannot-install-pyaudio-gcc-error](https://stackoverflow.com/questions/20023131/cannot-install-pyaudio-gcc-error)**

You should now be able to use the app but **FIRST** take a look at the 2 JSON files that come with the script: `speech_language.json` and `memories.json`

###`speech_language.json` : 
contains the language that you want use to speak. You can change it, you can use any language.below the tickers for the languages

```
ar-SA Arabic Saudi Arabia
cs-CZ Czech Czech Republic
da-DK Danish Denmark
de-DE German Germany
el-GR Modern Greek Greece
en-AU English Australia
en-GB English United Kingdom
en-IE English Ireland
en-US English United States
en-ZA English South Africa
es-ES Spanish Spain
es-MX Spanish Mexico
fi-FI Finnish Finland
fr-CA French Canada
fr-FR French France
he-IL Hebrew Israel
hi-IN Hindi India
hu-HU Hungarian Hungary
id-ID Indonesian Indonesia
it-IT Italian Italy
ja-JP Japanese Japan
ko-KR Korean Republic of Korea
nl-BE Dutch Belgium
nl-NL Dutch Netherlands
no-NO Norwegian Norway
pl-PL Polish Poland
pt-BR Portuguese Brazil
pt-PT Portuguese Portugal
ro-RO Romanian Romania
ru-RU Russian Russian Federation
sk-SK Slovak Slovakia
sv-SE Swedish Sweden
th-TH Thai Thailand
tr-TR Turkish Turkey
zh-CN Chinese China
zh-HK Chinese Hong Kong
zh-TW Chinese Taiwan
```

###`memories.json` : 
Initially it is empty, every question and answer given with the AI is added to the file and every time the speeches are added to the prompt automatically
so it will remember what you said.
**IF YOU WANT TO RESET THE MEMORY JUST OVERWRITE ALL THE CONTENT OF THE FILE WITH `{}` (so it must not be completely empty but contain `{}` otherwise it will cause an error)**


## START THE APP
Start the app with `python3 app.py 2>/dev/null` and say something...the AI will reply! **If you say nothing, app could crash! SORRY FOR THAT, WILL FIX**
