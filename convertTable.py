import pandas as pd
import os
import datetime as dt


file = os.path.join("Resources","cities.csv")

file_df = pd.read_csv(file, encoding="ISO-8859-1")

# reformat the date column
file_df['date'] = pd.to_datetime(file_df['date'])
file_df['date'] = file_df['date'].dt.date

file_df.set_index('city_id', inplace=True)

file_df.to_html('table.html', index=False)
