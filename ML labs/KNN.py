import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import numpy as np

df = pd.read_csv('UNSW_NB15_training-set.csv')#Загружаем исходную выборку

for column in df.columns:#Смотрим, сколько уникальных значений в каждом столбце датафрейма
    print(df[column].value_counts(dropna=False))

df = df.drop(['id', 'attack_cat', 'proto', 'service', 'state'], axis=1)# Убираем качественные значения и id за ненадобностью
#Вероятно, перевод качественных значений в количественный эквивалент поспособствует большей точности, однако так как уникальных
#значений качественных параметров слишком много, данная задача будет слищком ресурсоемкой

labelless = df.drop(['label'], axis=1)# Записываем датафрейм в labelless, исключая столбец label

min_limit = np.mean(labelless) - 3 * np.std(labelless)# В соответствии с правилом трех сигм устанавливаем нижнюю границу диапазона для каждого параметра
max_limit = np.mean(labelless) + 3 * np.std(labelless)# В соответствии с правилом трех сигм устанавливаем верхнюю границу диапазона для каждого параметра

i = 0#Указатель на значение нижней и верхней границы допустимого диапазона
for column in df.columns:# В этом цикле убираем значения, которые выходят за рамки допустимого диапазона
    if i < 39:
       df = df.loc[(min_limit[i] < df[column]) & (max_limit[i] > df[column])]
    i += 1
# Разделяем исходную выборку на обучающие и тестовые данные
points_train, points_test, labels_train, labels_test = train_test_split(df.iloc[:, :-1], df['label'], test_size=0.25, random_state=0)

ss = StandardScaler()#Используем StandardScaler чтобы масштабировать данные
ss.fit(points_train)
points_train.iloc[:, :] = ss.transform(points_train)
points_test.iloc[:, :] = ss.transform(points_test)

knn = KNeighborsClassifier(n_neighbors=1, metric='euclidean')# Инициализация классификатора
knn.fit(points_train, labels_train)#Обучение классификатора на обучающих данных
pred = knn.predict(points_test)#Создание прогнозных значений для тестовой выборки
print('Score: ', knn.score(points_test, labels_test))# Оценка работы классификатора. 0.92. Не самый идеальный исход, но терпимо

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
anomaly.to_csv('Task 3 anomaly.txt', sep=':')#Записываем аномалии в файл, чтобы было удобнее посмотреть на них позже

t_data.iloc[:, :] = ss.transform(t_data)#Нормализуем значения выборки с помощью StandardScaler
pred = knn.predict(t_data)
print('Result:\n', t_data.assign(predict=pred))
t_data.assign(predict=pred).to_csv('Task 3 result.txt', sep=':')#Выводим полученный результат с найденными значениями label