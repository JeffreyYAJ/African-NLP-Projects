from gnews import GNews
import pandas as pd

google_news = GNews(language='fr', country='CM') # Focus sur le Cameroun

def collect_data(queries, label):
    all_articles = []
    for q in queries:
        articles = google_news.get_news(q)
        for art in articles:
            all_articles.append({'text': art['title'], 'category': label})
    return all_articles

# On définit nos classes pour le NLP
politics = collect_data(['politique Cameroun', 'élections Afrique', 'gouvernement'], 'Politique')
sports = collect_data(['Lions Indomptables', 'CAN 2025', 'Football Afrique'], 'Sport')
economy = collect_data(['Bourse Afrique', 'Économie Cameroun', 'Investissement'], 'Economie')

# Création du Dataset
df = pd.DataFrame(politics + sports + economy)
df.to_csv('african_news_dataset.csv', index=False)
print(f"Dataset créé avec {len(df)} titres !")