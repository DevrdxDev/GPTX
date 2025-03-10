#!/data/data/com.termux/files/usr/bin/python3

import openai
import os
from time import sleep
import sys

# Check if any command line arguments are provided
if len(sys.argv) < 2:
    print("Usage: ask < Question >")
    sys.exit(1)

# Combine all command line arguments (excluding the script name) into a single string
askx = ' '.join(sys.argv[1:])

API = ''

try:
    openai.api_key = (API) 

    response = openai.Completion.create(
                            model='gpt-3.5-turbo-instruct',
                            prompt=askx,
                            max_tokens=3048,
                            top_p=1.0,
    presence_penalty=0.0)

    print( response.choices[0].text + "\n") # type:ignore
except Exception as e:
    print(e)
