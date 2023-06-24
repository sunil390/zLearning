# AI Models

## Hugging face 

1. only cpu-> pip3 install torch torchvision torchaudio
2. with CUDA 11.8 -> pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
3. pip3 install transformers
4. Text Summarirization using bart models
```.py
from transformers import pipeline

# smaller model for faster processing
#summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")
# Larger model
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

text = """
Artificial intelligence (AI) is intelligence—perceiving, synthesizing, and inferring information—demonstrated by machines, as opposed to intelligence displayed by humans or by other animals. "Intelligence" encompasses the ability to learn and to reason, to generalize, and to infer meaning.[1] Example tasks in which this is done include speech recognition, computer vision, translation between (natural) languages, as well as other mappings of inputs.[2]
AI applications include advanced web search engines (e.g., Google Search), recommendation systems (used by YouTube, Amazon, and Netflix), understanding human speech (such as Siri and Alexa), self-driving cars (e.g., Waymo), generative or creative tools (ChatGPT and AI art), automated decision-making, and competing at the highest level in strategic game systems (such as chess and Go).[3]
As machines become increasingly capable, tasks considered to require "intelligence" are often removed from the definition of AI, a phenomenon known as the AI effect.[4] For instance, optical character recognition is frequently excluded from things considered to be AI, having become a routine technology.[5]
Artificial intelligence was founded as an academic discipline in 1956, and in the years since it has experienced several waves of optimism,[6][7] followed by disappointment and the loss of funding (known as an "AI winter"),[8][9] followed by new approaches, success, and renewed funding.[7][10] AI research has tried and discarded many different approaches, including simulating the brain, modeling human problem solving, formal logic, large databases of knowledge, and imitating animal behavior. In the first decades of the 21st century, highly mathematical and statistical machine learning has dominated the field, and this technique has proved highly successful, helping to solve many challenging problems throughout industry and academia.[10][11]
The various sub-fields of AI research are centered around particular goals and the use of particular tools. The traditional goals of AI research include reasoning, knowledge representation, planning, learning, natural language processing, perception, and the ability to move and manipulate objects.[a] General intelligence (the ability to solve an arbitrary problem) is among the field's long-term goals.[12] To solve these problems, AI researchers have adapted and integrated a wide range of problem-solving techniques, including search and mathematical optimization, formal logic, artificial neural networks, and methods based on statistics, probability, and economics. AI also draws upon computer science, psychology, linguistics, philosophy, and many other fields."""

summary = summarizer(text, max_length=500, min_length=200, do_sample=False)

print(summary[0]['summary_text'])
```


## Miscellaneous 

1. pip freeze
2. pip cache purge
