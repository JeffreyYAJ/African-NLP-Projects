

import nltk
nltk.download('stopwords')
nltk.download('punkt')

import pandas as pd
from nltk.corpus import stopwords
import string
import re
import os 

data_folder = "data"
try:
    os.mkdir(data_folder)
except FileExistsError:
    pass

french_stopwords = set(stopwords.words('french'))

def clean_text(text):
    if not isinstance(text, str):
      return ""
    text =text.lower()
    text = re.sub(f"[{string.punctuation}]", "", text)

    text = re.sub(r'\d+', '', text)

    words = text.split()
    cleaned_words= [w for w in words if w not in french_stopwords]

    return " ".join(cleaned_words)

df = pd.read_csv('data/africa_news.csv')
df['clean_text'] = df['text'].apply(clean_text)
df.to_csv('data/africa_news_cleaned.csv', index=False)
print("Dataset cleaned")