import nltk
import numpy as np
import random
import string

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load the article
article = """
Dampak dari masalah kesehatan jiwa akibat
pandemi COVID-19 berupa masalah gangguan
tidur (Watamura & Koppels, 2020;Morgül et al.,
2020; Yeasmin et al., 2020), penurunan
kesejahteraan pada anak dan orang tua, serta
tingkat kebahagian pada anak (Cusinato et al.,
2020), meningkatnya kekerasan pada anak yang
dilakukan oleh orang tua maupun anggota
keluarga lainnya (Calvano et al., 2021; Cusinato
et al., 2020; Watamura & Koppels, 2020), dan
kekerasan pada orang tua maupun pasangan
(Calvano et al., 2021).
Pandemic COVID-19 memiliki dampak yang
signifikan terhadap kesehatan mental bagi orang
tua dan anak bahkan sampai mempengaruhi
perubahan fungsi keluarga. Masala kesehatan
mental selama masa pandemic harus diatasi
dengan baik dan benar supaya tidak
menimbulkan PTSD setelah masa pandemik
selesai. Dari semua artikel yang didapat hampir
semunya menggunakan penelitian kuantitatif
sehingga peneliti menyarankan kepada peneliti
selanjutkan untuk menggunakan metode
kualitatif atau mixed metode. Jika ingin
menggunakan metode peneliti menyarankan
menggunakan design kuasi ekperimen yang bertujuan untuk mengatasi dan mencegah terjadi.
"""

# Preprocess the data
nltk.download('punkt')  # Download required nltk data

sent_tokens = nltk.sent_tokenize(article)  # Convert the article into a list of sentences
word_tokens = nltk.word_tokenize(article)  # Convert the article into a list of words

lemmer = nltk.stem.WordNetLemmatizer()

def LemTokens(tokens):
    return [lemmer.lemmatize(token.lower()) for token in tokens]

remove_punct_dict = dict((ord(punct), None) for punct in string.punctuation)

def LemNormalize(text):
    return LemTokens(nltk.word_tokenize(text.lower().translate(remove_punct_dict)))

# Greeting messages
GREETING_INPUTS = ["hello", "hi", "greetings", "sup", "what's up"]
GREETING_RESPONSES = ["hi", "hey", "*nods*", "hi there", "hello"]

def greeting(sentence):
    for word in sentence.split():
        if word.lower() in GREETING_INPUTS:
            return random.choice(GREETING_RESPONSES)

# Generate response
def generate_response(user_input):
    bot_response = ''
    sent_tokens.append(user_input)

    tfidf_vectorizer = TfidfVectorizer(tokenizer=LemNormalize, stop_words='english')
    tfidf_matrix = tfidf_vectorizer.fit_transform(sent_tokens)

    vals = cosine_similarity(tfidf_matrix[-1], tfidf_matrix)
    idx = vals.argsort()[0][-2]
    flat = vals.flatten()
    flat.sort()
    score = flat[-2]

    if score == 0:
        bot_response = bot_response + "I apologize, but I don't understand."
    else:
        bot_response = bot_response + sent_tokens[idx]

    sent_tokens.remove(user_input)

    return bot_response

# Main conversation loop
print("ChatBot: I am your chatbot. How can I help you today?")

while True:
    user_input = input("User: ")
    user_input = user_input.lower()

    if user_input != 'bye':
        if user_input in ['thanks', 'thank you']:
            print("ChatBot: You're welcome!")
            break
        else:
            if greeting(user_input) is not None:
                print("ChatBot: " + greeting(user_input))
            else:
                print("ChatBot: " + generate_response(user_input))
    else:
        print("ChatBot: Goodbye! Have a nice day!")
        break
