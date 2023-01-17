# GPTalk

**[JOIN DISCORD](https://discord.gg/mettNtATzW)** **|** **[TWITTER](https://twitter.com/gptalk1)** **|** **[DONATE](https://github.com/0ut0flin3/GPTalk#donate)**

Interact with GPT using your own voice instead of text.

**...Constantly updated with new features...**






[REQUIRMENTS & HOW-TO-USE (PLEASE READ FIRST!)](https://github.com/0ut0flin3/openai-davinci003-python-speech/blob/main/README.md#requirments-and-how-to-use-read-please)

[Install dependencies Windows](https://github.com/0ut0flin3/openai-davinci003-python-speech/blob/main/README.md#for-windows)

[Install dependencies Linux](https://github.com/0ut0flin3/openai-davinci003-python-speech/blob/main/README.md#for-linux)

THEN

[Start the app](https://github.com/0ut0flin3/openai-davinci003-python-speech/blob/main/README.md#start-the-app)


## REQUIRMENTS and HOW TO USE (READ PLEASE!)


-In order to use this script you need to :

-have your OpenAI's Api key inside the OPENAI_API_KEY environment variable

-install these Python modules: `openai`,`SpeechRecognition`,`gTTS`,`PyAudio` (and also `playsound` if you are on Windows)


-install `mpg321` (a mp3 player for linux) only if you are on Linux



So, first of all, install all required packages\modules:

## FOR LINUX:

`sudo apt install mpg321 python3-dev portaudio19-dev`
 
`pip install openai`

`pip install SpeechRecognition`

`pip install gTTS`

`pip install PyAudio`

## FOR WINDOWS:

`pip install openai`

`pip install SpeechRecognition`

`pip install gTTS`

`pip install PyAudio`

`pip install playsound`

\\\\\\\\\\\\\\\\\\
\\\\\\\\\\\\\\\\\\\\\\\\\\\

**If you have some mistakes in installing PyAudio read this topic: [https://stackoverflow.com/questions/20023131/cannot-install-pyaudio-gcc-error](https://stackoverflow.com/questions/20023131/cannot-install-pyaudio-gcc-error)**



You should now be able to use the app with `python3 app.py 2>/dev/null` but **FIRST** take a look at the 2 JSON files that come with the script: `speech_language.json` and `memories.json`

### speech_language.json : 
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

### memories.json : 
Initially it is empty, every question and answer given with the AI is added to the file and every time the speeches are added to the prompt automatically
so it will remember what you said.
**IF YOU WANT TO RESET THE MEMORY JUST OVERWRITE ALL THE CONTENT OF THE FILE WITH `{}` (so it must not be completely empty but contain `{}` otherwise it will cause an error)**


## START THE APP
Start the app with `python3 app.py 2>/dev/null` on Linux
or `python app.py` on Windows
and say something...the AI will reply (with voice too)! 

## DONATE

If you found this software useful please consider a donation:


Bitcoin:  `17AnP1zuvLV9cQrGQi6H6qMLeWeujHzAYX`

Monero: `82qjYLZj6XeTGjeUNm9AQVB78hVGStZd8YU1UKuvWz8QKAzFWZpBpEQFho3jrvUCNQPSqC9nYeEN3b7FQ5REPffNSA2WSDH`

Solana: `6RX2ADdcNWZfaUfuGeHg86AYAoMuLF45Lbgfu3oNGh9i`

Litecoin: `ltc1q4ft4ltjnyt8auqq4m5u7raatftu6mt5snst493`

Ethereum: `0xF3A0246690947669A0bf68147Ba82AC8de576a56`

Polygon / MYST : `0x45320b5B2a8f6073f4a92FFDF149861aBade4B4b`



Thank you :-)
