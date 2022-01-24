import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn import tree
from sklearn.naive_bayes import GaussianNB
import numpy as np

df = pd.read_csv('payment_fraud.csv')# Открываем исходный файл
print(df)
df = df.drop(['paymentMethod'], axis=1)# Убираем качественные значения и id за ненадобностью

labelless = df.drop(['label'], axis=1)
print(labelless)
min_limit = np.mean(labelless) - 3 * np.std(labelless)# В соответствии с правилом трех сигм устанавливаем нижнюю границу диапазона для каждого параметра
max_limit = np.mean(labelless) + 3 * np.std(labelless)# В соответствии с правилом трех сигм устанавливаем верхнюю границу диапазона для каждого параметра
print(max_limit, min_limit)
i = 0#Указатель на значение нижней и верхней границы допустимого диапазона
print(df.columns)
for column in df.columns:
    if i < 4:
        df = df.loc[(min_limit[i] < df[column]) & (max_limit[i] > df[column])]
    i += 1

# Разделяем исходную выборку на обучающие и тестовые данные
points_train, points_test, labels_train, labels_test = train_test_split(df.iloc[:, :-1], df['label'], test_size=0.25, random_state=0)

ss = StandardScaler()#Используем StandardScaler чтобы масштабировать данные
ss.fit(points_train)
points_train.iloc[:, :] = ss.transform(points_train)
points_test.iloc[:, :] = ss.transform(points_test)

naive = GaussianNB()# Инициализация наивного байесовского классификатора
naive.fit(points_train, labels_train)# Обучение на обучающей выборке
pred = naive.predict(points_test)# Создание прогнозных значений для тестовой выборки
print('Score: ', naive.score(points_test, labels_test))# Вывод оценки точности классификатора

# Классификация новых данных на основе обученного классификатора
pre_testing_data = pd.read_csv('payment_fraud_2.csv')# Загружаем выборку, для которой будем искать значение label с помощью обученного классификатора
pre_testing_data = pre_testing_data.drop(['paymentMethod', 'label'], axis=1)#Избавляемся в новой выборке от ненужных параметров
t_data = pre_testing_data.copy(deep=True)# Создаем копию новой выборки. К копии применяем классификатор, а оригинал нужен для последующего выявления аномалий

j = 0
for column in t_data.columns:# Как и выше, здесь убираем значения, выходящие за рамки допустимого диапазона
    if j < 3:
        t_data = t_data.loc[(min_limit[j] < t_data[column]) & (max_limit[j] > t_data[column])]
    j += 1

# Проверяем наличие отклонений полученной обработанной выборки от оригинальной. Найденные отклонения считаем аномалиями
anomaly = pre_testing_data[~pre_testing_data.apply(tuple, 1).isin(t_data.apply(tuple, 1))]
print('Anomaly:\n', anomaly)
anomaly.to_csv('Task 5 anomaly.txt', sep=':')#Записываем аномалии в файл, чтобы было удобнее посмотреть на них позже

pred = naive.predict(t_data)
print('Result:\n', t_data.assign(predict=pred))
t_data.assign(predict=pred).to_csv('Task 5 result.txt', sep=':')#Выводим полученный результат с найденными значениями label