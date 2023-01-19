# GPTalk 0.0.3.9 (text + speech)

<img src="https://user-images.githubusercontent.com/114559605/213072836-213cd555-68fc-496a-8613-23c8dcf4c06c.png" height="250" width="250">


**[JOIN DISCORD](https://discord.gg/mettNtATzW)** **|** **[TWITTER](https://twitter.com/gptalk1)** **|** **[DONATE](https://github.com/0ut0flin3/GPTalk#donate)**

Interact with GPT-3 using voice as well as text, in any language and with extended features




[REQUIREMENTS](https://github.com/0ut0flin3/GPTalk#requirments)

[INSTALLATION](https://github.com/0ut0flin3/GPTalk#nstallation)

[USAGE](https://github.com/0ut0flin3/GPTalk#usage)

[LIST OF SUPPORTED LANGUAGES](https://github.com/0ut0flin3/GPTalk#languages)



## REQUIREMENTS


-In order to use GPTalk you need to :

-have your OpenAI's Api key inside the OPENAI_API_KEY environment variable.


-install `mpg321` (a mp3 player for linux) only if you are on Linux.




## INSTALLATION 

Install GPTalk using PIP: `pip install  gptalk==0.0.3.9`

Always use `-U` in order to install the latest version available.

Upgrade gptalk from time to time with pip install -U so that you always use the updated and bugfixed version.


## USAGE

In addition to communicating with gpt3 using the text or voice it is also possible to define some aspects of its behavior and personal details, as well as those of gpt3, even yours.

Some examples:

***>>>***`import gptalk.gptalk as gpt3`

***>>>***`app = gpt3.CONFIGURE(<YOUR_API_KEY>)`  # OR: app = gpt3.CONFIGURE(os.getenv('OPENAI_API_KEY'))

***>>>***`app.input_mode = "speech"` # OR 'text'

***>>>***`app.AI_NAME = "Alice"`

***>>>***`app.HUMAN_NAME = "Bob"`

***>>>***`app.AI_GENRE = "female"`

***>>>***`app.AI_AGE = "32"`

***>>>***`app.AI_MOOD = "happy"`

***>>>***`app.AI_SPECIES = "human"`

then, save:


***>>>***`app.save() #will create a memories.json file in the same folder that will also store and remember previous conversations.Every time you run save(), memories.json will be replaced with new. You can just run directly run() in the next step to use already existent`

and,then, run the app:

***>>>***`app.run()`

Start talking ( or typing, depending by the mode you choose) ... As for 'speech mode', gpt-3  should respond in a moment, but several factors can influence (try more times if you fail, move closer to the microphone)


Say `goodbye` to quit.

AVAILABLE PARAMETERS  : `AI_NAME`, `AI_AGE`, `AI_HOBBIES`,` AI_GENRE`, `AI_MOOD`, `AI_SPECIES` , `HUMAN_NAME`, `HUMAN_AGE`, `HUMAN_HOBBIES`,` HUMAN_GENRE`, `HUMAN_MOOD`, `HUMAN_SPECIES`


If you want change speech language (en-US is default) use `app.language=<LANGUAGE_TICKER>` (before run)


Give a feedback, positive or negative,it's very apprecciated >> https://discord.gg/mettNtATzW



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




## DONATE

If you found this software useful please consider a donation:


Bitcoin:  `17AnP1zuvLV9cQrGQi6H6qMLeWeujHzAYX`

Monero: `82qjYLZj6XeTGjeUNm9AQVB78hVGStZd8YU1UKuvWz8QKAzFWZpBpEQFho3jrvUCNQPSqC9nYeEN3b7FQ5REPffNSA2WSDH`

Solana: `6RX2ADdcNWZfaUfuGeHg86AYAoMuLF45Lbgfu3oNGh9i`

Litecoin: `ltc1q4ft4ltjnyt8auqq4m5u7raatftu6mt5snst493`

Ethereum: `0xF3A0246690947669A0bf68147Ba82AC8de576a56`

Polygon / MYST : `0x45320b5B2a8f6073f4a92FFDF149861aBade4B4b`



Thank you :-)

