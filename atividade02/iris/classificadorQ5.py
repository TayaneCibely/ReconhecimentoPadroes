# 7-NN sem peso
knn_7 = KNeighborsClassifier(n_neighbors=7, metric='euclidean')
knn_7.fit(X_train, y_train)
accuracy_7 = knn_7.score(X_test, y_test)
print(f'Acurácia do 7-NN sem peso: {accuracy_7 * 100:.2f}%')

# 7-NN com peso (pesos inversamente proporcionais à distância)
knn_7_weighted = KNeighborsClassifier(n_neighbors=7, metric='euclidean', weights='distance')
knn_7_weighted.fit(X_train, y_train)
accuracy_7_weighted = knn_7_weighted.score(X_test, y_test)
print(f'Acurácia do 7-NN com peso: {accuracy_7_weighted * 100:.2f}%')
