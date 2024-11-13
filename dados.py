import pandas as pd

# Carregar dados
file_path = "./car.data"
columns = ["buying", "maint", "doors", "persons", "lug_boot", "safety", "class"]
df = pd.read_csv(file_path, names=columns)

# Definir regras de classificação
def classify(row):
    if row['safety'] == 'high' and row['buying'] == 'low':
        return 'v-good'
    elif row['safety'] == 'med' and row['lug_boot'] == 'big':
        return 'good'
    elif row['persons'] == 'more' and row['buying'] == 'med':
        return 'acc'
    elif row['safety'] == 'low':
        return 'unacc'
    else:
        return 'unacc'

# Aplicar regras
df['predicted_class'] = df.apply(classify, axis=1)

# Calcular número de acertos
correct_predictions = sum(df['class'] == df['predicted_class'])
print(f'Número de acertos: {correct_predictions}')

# Calcular acurácia
total_examples = len(df)
accuracy = correct_predictions / total_examples
print(f'Acurácia: {accuracy * 100:.2f}%')
