import os
import pandas as pd
from dotenv import load_dotenv

load_dotenv()

monsters_filename =f"DB/{os.getenv('MONSTERS_FILENAME', 'monsters.csv')}"
print(monsters_filename)

monsters_df = pd.read_csv(monsters_filename)

df_subset = monsters_df.iloc[:, 1:12]

print(df_subset.head())
print(df_subset.columns)




