import csv
import pandas as pd
import numpy as np

iris = pd.read_csv("iris.csv")

iris_list = np.array(iris)

list = []
for flower in iris_list:
    if flower[4] == 'Iris-virginica':
        list.append(flower)

virginica_list = np.array(list)

virginica_sepal_length_std = np.std(virginica_list[:,0])
virginica_sepal_length_mean = np.mean(virginica_list[:,0])

virginica_sepal_width_std = np.std(virginica_list[:,1])
virginica_sepal_width_mean = np.mean(virginica_list[:,1])

virginica_petal_length_std = np.std(virginica_list[:,2])
virginica_petal_length_mean = np.mean(virginica_list[:,2])

virginica_petal_width_std = np.std(virginica_list[:,3])
virginica_petal_width_mean = np.mean(virginica_list[:,3])

total = 0
correct = 0
incorrect = 0

def predict_iris(flower):
    if flower[3] < .75:
        check(flower, 'Iris-setosa')
        return
    verginica_points = 0
    if virginica_sepal_length_mean - virginica_sepal_length_std * 2 < flower[0] < virginica_sepal_length_mean + virginica_sepal_length_std * 2:
        verginica_points +=1
    if virginica_sepal_width_mean - virginica_sepal_width_std * 2 < flower[1] < virginica_sepal_width_mean + virginica_sepal_width_std * 2:
        verginica_points += 1
    if virginica_petal_length_mean - virginica_petal_length_std < flower[2] < virginica_petal_length_mean + virginica_petal_length_std * 2:
        verginica_points +=1.5
    if virginica_petal_width_mean - virginica_petal_width_std < flower[3] < virginica_petal_width_mean + virginica_petal_width_std * 2:
        verginica_points +=1.5
    if verginica_points >= 3:
        check(flower, 'Iris-virginica')
        return
    check(flower, 'Iris-versicolor')
    return

def check(flower, guess):
    if guess == flower[4]:
        global correct
        correct +=1
    else:
        global incorrect
        incorrect +=1
    global total
    total +=1
    return

for flower in iris_list:
    predict_iris(flower)

print(correct)
print(incorrect)
print(correct/total)
print("{} flowers were guessed correctly, {} were incorrect, {}% were correct".format(str(correct), str(incorrect), str(np.round((correct/total) *100, decimals = 2))))
