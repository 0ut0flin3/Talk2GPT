# GPTalk 0.0.4.4 (text + speech)

Fast GPT-3 client for Windows and Unix that supports both text and speech in any language.


**Here is a video tutorial if you have troubles using Python or GPTalk: https://www.youtube.com/watch?v=jXBpMUv5QB0&t=320s**

**Jan 24,2023: Integrated DALL-E support - Instant generation and preview of images using both text and speech**


<img src="https://user-images.githubusercontent.com/114559605/213072836-213cd555-68fc-496a-8613-23c8dcf4c06c.png" height="250" width="250">


**[JOIN DISCORD](https://discord.gg/mettNtATzW)** **|** **[TWITTER](https://twitter.com/gptalk1)** **|** **[DONATE](https://github.com/0ut0flin3/GPTalk#donate)**



[REQUIREMENTS](https://github.com/0ut0flin3/GPTalk#requirments)

[INSTALLATION](https://github.com/0ut0flin3/GPTalk#nstallation)

[USAGE](https://github.com/0ut0flin3/GPTalk#usage)

[LIST OF SUPPORTED LANGUAGES](https://github.com/0ut0flin3/GPTalk#languages)



## REQUIREMENTS


-In order to use GPTalk you need :

**1)**  Install the following libraries only if you are on Linux\MAC:

LINUX: `apt install mpg321 python3-dev portaudio19-dev` 

MAC: `brew install mpg321 portaudio` Join Discord and ask if you have issues....


**2)** Have an OpenAI's Api Key  ( you can set it in app or put it inside the OPENAI_API_KEY environment variable.)


Should be enough, but if you already have problems in voice detection even after several attempts try these POSSIBLE SOLUTIONS:

on linux: `sudo apt-get python-dev build-essential swig libpulse-dev` ..... then : `sudo pip install pocketsphinx` .... then uninstall and reinstall gptalk

on mac: `brew install swig pulseaudio` ..... then : `sudo pip install pocketsphinx` .... then uninstall and reinstall gptalk



## INSTALLATION 

Install GPTalk using PIP: `pip install  gptalk==0.0.4.4`


Upgrade gptalk from time to time with pip install -U so that you always use the updated and bugfixed version.


## USAGE

In addition to interact with GPT-3 using the text or speech, it is also possible to define some aspects of its behavior and personal details, as well as yours.

BASIC USAGE EXAMPLE:

***>>>***`import gptalk.gptalk as gpt3`

***>>>***`app = gpt3.CONFIGURE(<YOUR_API_KEY>)`  # OR: app = gpt3.CONFIGURE(os.getenv('OPENAI_API_KEY'))

***>>>***`app.language=<LANGUAGE_TICKER>` # only needed for speech mode really, because text mode automatically will translate if you start chatting in a specific lang

***>>>***`app.input_mode = "speech"` # OR 'text'

***>>>***`app.AI_NAME = "Alice"`

***>>>***`app.HUMAN_NAME = "Bob"`

***>>>***`app.AI_GENRE = "female"`

***>>>***`app.AI_AGE = "32"`

***>>>***`app.AI_MOOD = "happy"`

***>>>***`app.AI_SPECIES = "human"`

then, save:


***>>>***`app.save() #will create a memories.json file in the same folder that will store the informations you set in the previous step. will also store and remember conversations with gpt3.Every time you run save(),already existent memories.json will be replaced with new. You can just run directly run() in the next step to use already existent. Don't matter if you do directly run() without save() ,in that case no memories will be used. You can also create your own empty memories.json that must contains at least two brackets {} , (must NOT be fully empty)`

and,then, run the app:

***>>>***`app.run()`

Start talking ( or typing, depending by the mode you choose) ... As for 'speech mode', gpt-3  should respond in seconds, but several factors can influence (try more times if you fail, move closer to the microphone)


Say `goodbye` or `go to sleep` to quit.

AVAILABLE PARAMETERS  : `AI_NAME`, `AI_AGE`, `AI_HOBBIES`,` AI_GENRE`, `AI_MOOD`, `AI_SPECIES` , `HUMAN_NAME`, `HUMAN_AGE`, `HUMAN_HOBBIES`,` HUMAN_GENRE`, `HUMAN_MOOD`, `HUMAN_SPECIES`


If you want change speech language (en-US is default) use `app.language=<LANGUAGE_TICKER>` (before run)


Give a feedback, positive or negative,it's very apprecciated >> https://discord.gg/mettNtATzW

## Generate images

DALL-E image generation is now active using both voice and text.

To activate image mode ask gpt-3 to activate it. It will be active immediately. From that moment the inputs will generate an image that will be immediately displayed in a pop-up.

To exit image mode, tell gpt-3 to disable it and you'll be back to normal use.

You can also choose to display the images directly in the terminal in RGB color format but you will need to set this option before, in the configuration phase, using `app.SHOW_IMAGE_IN_CONSOLE=True`.

## LANGUAGES

```
af-ZA   Afrikaans (South Africa)
ar-AE   Arabic (U.A.E.)
ar-BH   Arabic (Bahrain)
ar-DZ   Arabic (Algeria)
ar-EG   Arabic (Egypt)
ar-IQ   Arabic (Iraq)
ar-JO   Arabic (Jordan)
ar-KW   Arabic (Kuwait)
ar-LB   Arabic (Lebanon)
ar-LY   Arabic (Libya)
ar-MA   Arabic (Morocco)
ar-OM   Arabic (Oman)
ar-QA   Arabic (Qatar)
ar-SA   Arabic (Saudi Arabia)
ar-SY   Arabic (Syria)
ar-TN   Arabic (Tunisia)
ar-YE   Arabic (Yemen)
az-AZ   Azeri (Latin) (Azerbaijan)
az-AZ   Azeri (Cyrillic) (Azerbaijan)
be-BY   Belarusian (Belarus)
bg-BG   Bulgarian (Bulgaria)
bs-BA   Bosnian (Bosnia and Herzegovina)
ca-ES   Catalan (Spain)
cs-CZ   Czech (Czech Republic)
cy-GB   Welsh (United Kingdom)
da-DK   Danish (Denmark)
de-AT   German (Austria)
de-CH   German (Switzerland)
de-DE   German (Germany)
de-LI   German (Liechtenstein)
de-LU   German (Luxembourg)
dv-MV   Divehi (Maldives)
el-GR   Greek (Greece)
en-AU   English (Australia)
en-BZ   English (Belize)
en-CA   English (Canada)
en-CB   English (Caribbean)
en-GB   English (United Kingdom)
en-IE   English (Ireland)
en-JM   English (Jamaica)
en-NZ   English (New Zealand)
en-PH   English (Republic of the Philippines)
en-TT   English (Trinidad and Tobago)
en-US   English (United States)
en-ZA   English (South Africa)
en-ZW   English (Zimbabwe)
es-AR   Spanish (Argentina)
es-BO   Spanish (Bolivia)
es-CL   Spanish (Chile)
es-CO   Spanish (Colombia)
es-CR   Spanish (Costa Rica)
es-DO   Spanish (Dominican Republic)
es-EC   Spanish (Ecuador)
es-ES   Spanish (Castilian)
es-ES   Spanish (Spain)
es-GT   Spanish (Guatemala)
es-HN   Spanish (Honduras)
es-MX   Spanish (Mexico)
es-NI   Spanish (Nicaragua)
es-PA   Spanish (Panama)
es-PE   Spanish (Peru)
es-PR   Spanish (Puerto Rico)
es-PY   Spanish (Paraguay)
es-SV   Spanish (El Salvador)
es-UY   Spanish (Uruguay)
es-VE   Spanish (Venezuela)
et-EE   Estonian (Estonia)
eu-ES   Basque (Spain)
fa-IR   Farsi (Iran)
fi-FI   Finnish (Finland)
fo-FO   Faroese (Faroe Islands)
fr-BE   French (Belgium)
fr-CA   French (Canada)
fr-CH   French (Switzerland)
fr-FR   French (France)
fr-LU   French (Luxembourg)
fr-MC   French (Principality of Monaco)
gl-ES   Galician (Spain)
gu-IN   Gujarati (India)
he-IL   Hebrew (Israel)
hi-IN   Hindi (India)
hr-BA   Croatian (Bosnia and Herzegovina)
hr-HR   Croatian (Croatia)
hu-HU   Hungarian (Hungary)
hy-AM   Armenian (Armenia)
id-ID   Indonesian (Indonesia)
is-IS   Icelandic (Iceland)
it-CH   Italian (Switzerland)
it-IT   Italian (Italy)
ja-JP   Japanese (Japan)
ka-GE   Georgian (Georgia)
kk-KZ   Kazakh (Kazakhstan)
kn-IN   Kannada (India)
ko-KR   Korean (Korea)
kok-IN  Konkani (India)
ky-KG   Kyrgyz (Kyrgyzstan)
lt-LT   Lithuanian (Lithuania)
lv-LV   Latvian (Latvia)
mi-NZ   Maori (New Zealand)
mk-MK   FYRO Macedonian (Former Yugoslav Republic of Macedonia)
mn-MN   Mongolian (Mongolia)
mr-IN   Marathi (India)
ms-BN   Malay (Brunei Darussalam)
ms-MY   Malay (Malaysia)
mt-MT   Maltese (Malta)
nb-NO   Norwegian (Bokm?l) (Norway)
nl-BE   Dutch (Belgium)
nl-NL   Dutch (Netherlands)
nn-NO   Norwegian (Nynorsk) (Norway)
ns-ZA   Northern Sotho (South Africa)
pa-IN   Punjabi (India)
pl-PL   Polish (Poland)
ps-AR   Pashto (Afghanistan)
pt-BR   Portuguese (Brazil)
pt-PT   Portuguese (Portugal)
qu-BO   Quechua (Bolivia)
qu-EC   Quechua (Ecuador)
qu-PE   Quechua (Peru)
ro-RO   Romanian (Romania)
ru-RU   Russian (Russia)
sa-IN   Sanskrit (India)
se-FI   Sami (Northern) (Finland)
se-FI   Sami (Skolt) (Finland)
se-FI   Sami (Inari) (Finland)
se-NO   Sami (Northern) (Norway)
se-NO   Sami (Lule) (Norway)
se-NO   Sami (Southern) (Norway)
se-SE   Sami (Northern) (Sweden)
se-SE   Sami (Lule) (Sweden)
se-SE   Sami (Southern) (Sweden)
sk-SK   Slovak (Slovakia)
sl-SI   Slovenian (Slovenia)
sq-AL   Albanian (Albania)
sr-BA   Serbian (Latin) (Bosnia and Herzegovina)
sr-BA   Serbian (Cyrillic) (Bosnia and Herzegovina)
sr-SP   Serbian (Latin) (Serbia and Montenegro)
sr-SP   Serbian (Cyrillic) (Serbia and Montenegro)
sv-FI   Swedish (Finland)
sv-SE   Swedish (Sweden)
sw-KE   Swahili (Kenya)
syr-SY  Syriac (Syria)
ta-IN   Tamil (India)
te-IN   Telugu (India)
th-TH   Thai (Thailand)
tl-PH   Tagalog (Philippines)
tn-ZA   Tswana (South Africa)
tr-TR   Turkish (Turkey)
tt-RU   Tatar (Russia)
uk-UA   Ukrainian (Ukraine)
ur-PK   Urdu (Islamic Republic of Pakistan)
uz-UZ   Uzbek (Latin) (Uzbekistan)
uz-UZ   Uzbek (Cyrillic) (Uzbekistan)
vi-VN   Vietnamese (Viet Nam)
xh-ZA   Xhosa (South Africa)
zh-CN   Chinese (S)
zh-HK   Chinese (Hong Kong)
zh-MO   Chinese (Macau)
zh-SG   Chinese (Singapore)
zh-TW   Chinese (T)
zu-ZA   Zulu (South Africa)
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


