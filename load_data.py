import pandas as pd
from sqlalchemy import create_engine
df = pd.read_csv('Spotify_Youtube.csv')
engine = create_engine('postgresql://django:djangopass@127.0.0.1:5432/django')
df.to_sql('spotify_youtube', engine, if_exists='append', index=False)