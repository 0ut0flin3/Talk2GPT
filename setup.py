import setuptools
setuptools.setup(name='GPTalk',
    version='0.0.4.2',
    author='0ut0flin3',
    description='Interact with GPT-3 using voice as well as text, in any language and with extended features',
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        
                ],
    install_requires=['aiohttp==3.8.3', 'aiosignal==1.3.1', 'async-timeout==4.0.2', 'attrs==22.2.0', 'certifi==2022.12.7', 'charset-normalizer==2.1.1', 'click==8.1.3', 'frozenlist==1.3.3', 'gTTS==2.3.1', 'idna==3.4', 'multidict==6.0.4', 'openai==0.26.1', 'PyAudio==0.2.13', 'requests==2.28.2', 'SpeechRecognition==3.9.0', 'tqdm==4.64.1', 'urllib3==1.26.14', 'yarl==1.8.2'],
    python_requires='>=3'
        )