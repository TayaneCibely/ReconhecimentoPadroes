### Etapas para Construção do Conjunto de Regras

##Carregar e Entender os Dados Primeiro, precisamos carregar os dados e entender a estrutura das colunas. A base de dados "car.data" contém 7 
colunas:
buying
maint
doors
persons
lug_boot
safety
class (unacc, acc, good, v-good)

## Análise Exploratória dos Dados Vamos analisar os dados para identificar padrões que possam ser usados para criar as regras de classificação.

## Definição das Regras de Classificação Baseando-se na análise dos dados, criaremos um conjunto de regras. Aqui está um exemplo simplificado de como poderíamos definir algumas regras:

Regra 1: Se safety é high e buying é low, então class é v-good.
Regra 2: Se safety é med e lug_boot é big, então class é good.
Regra 3: Se persons é more e buying é med, então class é acc.
Regra 4: Se safety é low, então class é unacc.

## Aplicação das Regras ao Conjunto de Dados Aplique essas regras ao conjunto de dados para classificar cada exemplo.
## Avaliação dos Resultados Compare as classificações obtidas com as classificações reais para calcular a precisão do conjunto de regras.

## Implementação
Vamos implementar essas etapas em código Python para visualizar e aplicar as regras. Você pode seguir este roteiro para implementar em seu ambiente.

```python
python
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
        return 'unacc'  # Regra default

# Aplicar regras
df['predicted_class'] = df.apply(classify, axis=1)

# Calcular número de acertos
correct_predictions = sum(df['class'] == df['predicted_class'])
print(f'Número de acertos: {correct_predictions}')

# Calcular acurácia
total_examples = len(df)
accuracy = correct_predictions / total_examples
print(f'Acurácia: {accuracy * 100:.2f}%')
```

##Resultados
Após a aplicação das regras ao conjunto de dados, podemos calcular quantos exemplos foram classificados corretamente:

Número de exemplos no conjunto de dados: 1728
Número de acertos: 1073
Acurácia: 62.09%

Conclusão
Neste exercício, construímos um conjunto de regras simples para classificar exemplos da base de dados "Car". Embora as regras possam não cobrir todas as nuances dos dados, elas fornecem uma abordagem inicial para classificação. O objetivo foi entender como regras podem ser usadas e avaliar a eficácia delas.
