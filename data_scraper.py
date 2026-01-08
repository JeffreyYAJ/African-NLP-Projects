from gnews import GNews
import pandas as pd
import os 

data_folder = "data"
try:
    os.mkdir(data_folder)
except FileExistsError:
    pass
google_news = GNews(language = 'fr', country = 'CM')

def collect_data(queries, label):
  articles_list = []
  for q in queries:
    articles = google_news.get_news(q)
    for a in articles:
      articles_list.append({'text': a['title'], 'category': label})
  return articles_list


politics = collect_data(['Politique Cameroun', 'elections Afrique', 'gouvernement'],'Politique')
sports = collect_data(['Football Afrique', 'CAN'], 'Sport')
economy = collect_data(['Bourse Afrique', 'Investissement Afrique','Crise Economique Afrique'], 'Economy')

df = pd.DataFrame(politics + sports + economy)
df.to_csv('data/africa_news.csv', index=False)
print(f"Dataset Created {len(df)} titres")