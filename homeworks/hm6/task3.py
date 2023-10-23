import re

def count_sentences(text):
    sentences = re.findall(r'[^.!?]+[.!?](?:\s|$)', text)
    return len(sentences)
input_text = "Hello world. Hellow worlds."
sentence_count = count_sentences(input_text)
print("Количество предложений:", sentence_count)
