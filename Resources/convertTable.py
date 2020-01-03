import pandas as pd
import os

file = os.path.join("cities.csv")

file_df = pd.read_csv(file, encoding="ISO-8859-1")

file_df.set_index('City_ID', inplace=True)

file_df.to_html('table.html')
