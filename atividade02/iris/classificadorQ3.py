from sklearn.neighbors import KNeighborsClassifier

# Dividir o conjunto de dados em treinamento e teste
X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.5, random_state=42)

# Treinar o classificador k-NN
knn = KNeighborsClassifier(n_neighbors=1, metric='euclidean')
knn.fit(X_train, y_train)

# Avaliar o classificador
accuracy = knn.score(X_test, y_test)
print(f'Acurácia do 1-NN: {accuracy * 100:.2f}%')
