# GPTalk

<img src="https://user-images.githubusercontent.com/114559605/213072836-213cd555-68fc-496a-8613-23c8dcf4c06c.png" height="250" width="250">


**[JOIN DISCORD](https://discord.gg/mettNtATzW)** **|** **[TWITTER](https://twitter.com/gptalk1)** **|** **[DONATE](https://github.com/0ut0flin3/GPTalk#donate)**

Interact with GPT-3 using your voice instead of text, in any language.





[REQUIREMENTS](https://github.com/0ut0flin3/GPTalk#requirments)

[INSTALLATION](https://github.com/0ut0flin3/GPTalk#nstallation)

[USAGE](https://github.com/0ut0flin3/GPTalk#usage)

[LIST OF SUPPORTED LANGUAGES](https://github.com/0ut0flin3/GPTalk#languages)



## REQUIREMENTS


-In order to use GPTalk you need to :

-have your OpenAI's Api key inside the OPENAI_API_KEY environment variable.

-install these Python modules: `openai`,`SpeechRecognition`,`gTTS`,`PyAudio` (and also `playsound` if you are on Windows).
 You can also use the `requirements.txt` file to automatically install all the required modules in one shot with `pip install -r requirements.txt`


-install `mpg321` (a mp3 player for linux) only if you are on Linux.


**If you have some mistakes in installing PyAudio read this topic: [https://stackoverflow.com/questions/20023131/cannot-install-pyaudio-gcc-error](https://stackoverflow.com/questions/20023131/cannot-install-pyaudio-gcc-error)**


## INSTALLATION

You can install GPTalk using PIP: `pip install gptalk`

## USAGE

Some examples:

***>>>***`import gptalk.gptalk as gpt3`

***>>>***`app = gpt3.CONFIGURE()`

***>>>***`app.AI_NAME = "Alice"`

***>>>***`app.AI_GENRE = "female"`

***>>>***`app.save() #will create a memories.json file in the same folder. Will be replaced every time you run this command`

***>>>***`app.run()`

Start talking.

Say `goodbye` to quit.

Set language with `app.language=<LANGUAGE_TICKER>`


More examples on the GPTalk Discord Server >> https://discord.gg/mettNtATzW



## LANGUAGES

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


## DONATE

If you found this software useful please consider a donation:


Bitcoin:  `17AnP1zuvLV9cQrGQi6H6qMLeWeujHzAYX`

Monero: `82qjYLZj6XeTGjeUNm9AQVB78hVGStZd8YU1UKuvWz8QKAzFWZpBpEQFho3jrvUCNQPSqC9nYeEN3b7FQ5REPffNSA2WSDH`

Solana: `6RX2ADdcNWZfaUfuGeHg86AYAoMuLF45Lbgfu3oNGh9i`

Litecoin: `ltc1q4ft4ltjnyt8auqq4m5u7raatftu6mt5snst493`

Ethereum: `0xF3A0246690947669A0bf68147Ba82AC8de576a56`

Polygon / MYST : `0x45320b5B2a8f6073f4a92FFDF149861aBade4B4b`



Thank you :-)

