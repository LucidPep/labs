import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import tree
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier
import numpy as np

df = pd.read_csv('UNSW_NB15_training-set.csv')# Открываем исходный файл

df = df.drop(['id', 'attack_cat', 'proto', 'service', 'state'], axis=1)# Убираем качественные значения и id за ненадобностью

labelless = df.drop(['label'], axis=1)
min_limit = np.mean(labelless) - 3 * np.std(labelless)# В соответствии с правилом трех сигм устанавливаем нижнюю границу диапазона для каждого параметра
max_limit = np.mean(labelless) + 3 * np.std(labelless)# В соответствии с правилом трех сигм устанавливаем верхнюю границу диапазона для каждого параметра

i = 0#Указатель на значение нижней и верхней границы допустимого диапазона
for column in df.columns:# В этом цикле убираем значения, которые выходят за рамки допустимого диапазона
    if i < 39:
       df = df.loc[(min_limit[i] < df[column]) & (max_limit[i] > df[column])]
    i += 1

# Разделяем исходную выборку на обучающие и тестовые данные
points_train, points_test, labels_train, labels_test = train_test_split(df.iloc[:, :-1], df['label'], test_size=0.25, random_state=0)

Decision_Tree = DecisionTreeClassifier(criterion='entropy', max_depth=5)# Инициализация классификатора
Decision_Tree.fit(points_train, labels_train)# Обучение классификатора
pred = Decision_Tree.predict(points_test)#Создание прогнозных значений для тестовой выборки
print('Score: ', Decision_Tree.score(points_test, labels_test))

# Классификация новых данных на основе обученного классификатора
pre_testing_data = pd.read_csv('UNSW_NB15_testing-set.csv')# Загружаем выборку, для которой будем искать значение label с помощью обученного классификатора
pre_testing_data = pre_testing_data.drop(['id', 'attack_cat', 'proto', 'service', 'state', 'label'], axis=1)#Избавляемся в новой выборке от ненужных параметров
t_data = pre_testing_data.copy(deep=True)# Создаем копию новой выборки. К копии применяем классификатор, а оригинал нужен для последующего выявления аномалий

j = 0
for column in t_data.columns:# Как и выше, здесь убираем значения, выходящие за рамки допустимого диапазона
    if j < 38:
        t_data = t_data.loc[(min_limit[j] < t_data[column]) & (max_limit[j] > t_data[column])]
    j += 1

# Проверяем наличие отклонений полученной обработанной выборки от оригинальной. Найденные отклонения считаем аномалиями
anomaly = pre_testing_data[~pre_testing_data.apply(tuple, 1).isin(t_data.apply(tuple, 1))]
print('Anomaly:\n', anomaly)
anomaly.to_csv('Task 4 anomaly.txt', sep=':')#Записываем аномалии в файл, чтобы было удобнее посмотреть на них позже

pred = Decision_Tree.predict(t_data)
print('Result:\n', t_data.assign(predict=pred))
t_data.assign(predict=pred).to_csv('Task 4 result.txt', sep=':')#Выводим полученный результат с найденными значениями label

plt.subplots(figsize=(30, 30))# Задаем размер рисунка
tree.plot_tree(Decision_Tree)# Строим его
plt.savefig('Task 4 tree.png')# И сохраняем его в файл