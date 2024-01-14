import google.generativeai as genai
import os
import pathlib
import textwrap

from IPython.display import display
from IPython.display import Markdown

def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

genai.configure(api_key=os.environ['PALM_API_KEY'])

# for m in genai.list_models():
#  if 'generateContent' in m.supported_generation_methods:
#    print(m.name)

model = genai.GenerativeModel('gemini-pro')

response = model.generate_content("you act like a mainframe z/OS storage administrator. How to debug IDC30009I message")

to_markdown(response.text)

print(response.text)

# import pprint
# for model in palm.list_models():
#    pprint.pprint(model)
