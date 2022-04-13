import numpy as np
import pandas as pd
import csv
import jieba #chinese segmentizer
from konlpy.tag import Kkma #korean segmentizer
import random
import pickle
from sklearn.neighbors import KNeighborsClassifier

import re
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.preprocessing import LabelEncoder
from sklearn import linear_model
from sklearn.linear_model import LinearRegression
import sklearn.metrics as metrics
from string import punctuation

def predict(sentence):
	"""removes punctuation in new string and predicts its language"""


	x = vectorizer.transform([sentence]).toarray()
	lang = model.predict(x)
	lang = encoder.inverse_transform([round(lang[0])])

	return lang[0]

def stats(y_train,y_test,y_pred):

	"""
	print("Corpus test: ", y_test)
	print("Prédictions : ", [round(x) for x in y_pred])

	print("y axis interception point (b) : ", model.intercept_)
	print("Slope (m) : ", model.coef_)
	"""

	y_true = []
	[y_true.append(y) for x,y in zip(y_test,y_pred) if x == round(y)]
	
	#print("Prédictions correctes: ", [round(x) for x in y_true])

	with open("nearest-neighbors-model-stats.txt", "w") as file:
		file.write(f'Nombre de prédictions correctes: {len(y_true)}\nPourcentage de prédictions correctes : {round((len(y_true)/len(y_pred))*100)}%\nAccuracy score: {model.score(x_test,y_test)}')

if __name__ == '__main__':

	data = pd.read_csv('sentences_CH_KR.tsv', sep='\t')

	print(data["language"].value_counts())

	x,y = np.array([string.lower() if isinstance(string, str) else string for string in data['sentence']]),np.array(data['language'])

	vectorizer = CountVectorizer(analyzer='char', ngram_range=(1,1), max_features=10000)

	# 'fr' = 1, 'en'= 0
	encoder = LabelEncoder()
	y = encoder.fit_transform(y)

	X = vectorizer.fit_transform(x)
	x_train,x_test,y_train,y_test = train_test_split(X,y,test_size=0.1)
	#model = KNeighborsClassifier(n_neighbors=2).fit(x_train,y_train)

	"""attempt at saving the best model possible"""
	"""best_accuracy = 0

	for __ in range(5):

		x_train,x_test,y_train,y_test = train_test_split(X,y,test_size=0.1)
		model = KNeighborsClassifier(n_neighbors=2).fit(x_train,y_train)
		accuracy = model.score(x_test,y_test)
		print("Accuracy :", accuracy)

		if accuracy > best_accuracy:
			best_accuracy = accuracy
			#saving model
			with open("k-nearest-neighbors-model.pickle", "wb") as file:
				pickle.dump(model, file)"""

	pickle_input = open("k-nearest-neighbors-model.pickle", "rb")
	model = pickle.load(pickle_input)

	#y_pred = model.predict(x_test)

	"""write stats into linear-regression-model.txt"""
	#stats(y_train,y_test,y_pred)

	sentence = input("Type a sentence : ")

	print("The sentence is in :", predict(sentence))