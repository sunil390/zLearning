# Bard

1. https://flows.nodered.org/node/node-red-contrib-bard

## Palm2 

1. Set environment variable PALM_API_KEY in windows with the Bard API Key
2. pip install -q google-generativeai
3. Pyhon Code to call Palm2
```.py
import google.generativeai as palm
import os
palm.configure(api_key=os.environ['PALM_API_KEY'])

#response = palm.generate_text(prompt="The opposite of hot is")
#print(response.result) #  'cold.'

import pprint
for model in palm.list_models():
    pprint.pprint(model)
```
