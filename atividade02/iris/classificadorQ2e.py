python
import matplotlib.pyplot as plt

# Selecionar duas características para plotar
x = df['sepal length (cm)']
y = df['sepal width (cm)']
classes = df['target']

plt.figure(figsize=(10, 6))
plt.scatter(x[classes==0], y[classes==0], color='red', label='Setosa')
plt.scatter(x[classes==1], y[classes==1], color='green', label='Versicolor')
plt.scatter(x[classes==2], y[classes==2], color='blue', label='Virginica')
plt.legend()
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Sepal Width (cm)')
plt.title('Diagrama de Dispersão das Classes Iris')
plt.show()
