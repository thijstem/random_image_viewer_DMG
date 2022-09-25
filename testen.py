
import pandas as pd


df_sparql = pd.read_csv("manifesten.csv")
df_dmg = df_sparql[df_sparql['1'].str.contains("dmg")]
df_dmg.to_csv("manifestenDMG.csv")
iiifmanifesten = df_dmg['1'].tolist()
print(iiifmanifesten[0])