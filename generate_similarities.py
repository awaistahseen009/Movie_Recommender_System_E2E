from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd
import difflib
import pickle
from sklearn.metrics.pairwise import cosine_similarity
try:
    df=pd.read_csv('processed_data_frame.csv')
except Exception as e:
    print('Ensure that you have run the prepare_data.py file first')
    print(e)
all_movies=df['title'].values
tfidf = TfidfVectorizer(max_features=5000,stop_words='english')
embeddings = tfidf.fit_transform(df['tags']).toarray()
similarity = cosine_similarity(embeddings)
pickle.dump(similarity, open('similarities.pkl','wb'))