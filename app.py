import streamlit as st
from rake_nltk import Rake
from nltk.corpus import stopwords
import string
import nltk

nltk.download("stopwords")


text_list = [
    "review_1.txt",
    "review_2.txt",
    "review_3.txt"
]

text_data =[]

for text in text_list:
    with open(text, "r") as file:
        data = file.read().replace("\n", "")
        text_data.append(data.replace(u"\xa0", u" "))


all_text = text_data[0] + text_data[1] + text_data[2]

# Uses stopwords for english from NLTK, and all puntuation characters by
# default
r = Rake(
    stopwords= stopwords.words('english'),
    punctuations=string.punctuation,
    min_length=2,
    include_repeated_phrases=False
)

# Extraction given the text.
r.extract_keywords_from_text(all_text)

# To get keyword phrases ranked highest to lowest.
keyphrase_list =r.get_ranked_phrases()

st.header("Keyphrases Analysis")

selected_keyphrases = st.multiselect("Select keyphrases", keyphrase_list[:10], default=None)

selected_sentences = []

all_sentences = all_text.split(".")
for sentence in all_sentences:
    for selected_keyphrase in selected_keyphrases:
        if selected_keyphrase in sentence:
            selected_sentences.append(sentence)

st.write(selected_sentences)

