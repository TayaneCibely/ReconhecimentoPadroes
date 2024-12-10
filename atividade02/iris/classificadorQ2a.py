import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from scipy.spatial.distance import euclidean

# Carregar a base de dados Iris
iris = load_iris()
df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
df['target'] = iris.target

# Selecionar três exemplos aleatórios de cada classe
df_sampled = df.groupby('target').sample(n=3, random_state=42)

# Construir a matriz de distância
def calcular_distancias(df):
    distancias = []
    for i, row_i in df.iterrows():
        dist_row = []
        for j, row_j in df.iterrows():
            dist_row.append(euclidean(row_i[:-1], row_j[:-1]))
        distancias.append(dist_row)
    return pd.DataFrame(distancias)

df_distancias = calcular_distancias(df_sampled)
print(df_distancias
