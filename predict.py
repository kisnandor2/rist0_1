from dataSplitting import *

from sklearn import svm
from sklearn.metrics import classification_report, confusion_matrix

data = loadData()
splittedData = splitDataIntoLabelsAndImages(data)
training, validation = getTrainingAndValidationSetExactly(splittedData)

trainingData, trainingLabels = formatDataForClassifier(training)

clf = svm.SVC(gamma=0.001, C=100.)
clf.fit(trainingData, trainingLabels)

validationData, validationLabels = formatDataForClassifier(validation)
predictedLabels = clf.predict(validationData)

target_names = str(list(range(0,10))).replace(']', '').replace('[','').split(',') #TODO: don't be too lazy
print("Classification report:")
print(classification_report(validationLabels, predictedLabels, target_names=target_names))

print("Confusion matrix:")
print(confusion_matrix(validationLabels, predictedLabels, labels=list(range(0,10))))

# As you can see, in most of the cases the prediction is correct
# The only quite big error/confusion is at RandomSort-QuickSort
# in 27 cases the Incresing RandomSort looks like Increasing Quick and 
# in 37 cases the Decreasing RandomSort looks like Decreasing QuickSort
# Also, predicting the label 4(Increasing HeapSort) is 100% accurate