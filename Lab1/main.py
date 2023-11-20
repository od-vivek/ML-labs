from csv import reader
import math

#Using this function to load files .
def load_csv(filename):
    # Open file in read mode
    file = open(filename,"r")
    
    # Converting the readed file into a list 
    lines = reader(file)
    data = list(lines)
    return data

#Loading data from test csv file
path__test = "winequality-white-Test.csv"
test__data = load_csv(path__test)

#Loading data from train csv file
path__train = "winequality-white-Train.csv"
training__data = load_csv(path__train)

#processing all the data
for i in range(1, len(test__data)):
    resultant = [eval(val) for val in test__data[i][0].split(';')] 
    test__data[i] = resultant

for i in range(1, len(training__data)):
    resultant = [eval(val) for val in training__data[i][0].split(';')] 
    training__data[i] = resultant


#Total length will be length of the test data.
totalLength = len(test__data)
#starting a counter with value 0....
count = 0

#Accuracy for 1-NN
for i in range(1, len(test__data)):
    min_distance = math.inf
    ind = math.inf
    
    for j in range(1, len(training__data)):
        distance_sum = sum(pow((test__data[i][k] - training__data[j][k]), 2) for k in range(0, 11))
        #finding the least minimum distance 
        temp = min_distance
        min_distance = min(math.sqrt(distance_sum), min_distance)
        
        if temp != min_distance:
            ind = j
    #comparing their label and if they match , we increment the counter.
    if test__data[i][11] == training__data[ind][11]:
        count += 1

#accuract for 1NN 
acc_1NN = count / totalLength

#--------------------------------------------------------------------------------------------------------------------------->
# Reset count for 3-NN 

count = 0

#Accuracy for 3-NN
for i in range(1, len(test__data)):
    distances = [(j, sum(pow((test__data[i][k] - training__data[j][k]), 2) for k in range(0, 11))) for j in range(1, len(training__data))]
    distances.sort(key=lambda x: x[1])
    neighbors = [dist[0] for dist in distances[:3]]
    
    #Using this to calculate the least 3 Nearest Neighbours
    vec_min = {}
    for neighbor in neighbors:
        label_class = training__data[neighbor][11]
        if label_class in vec_min:
            vec_min[label_class] += 1
        else:
            vec_min[label_class] = 1
    
    #predict the class with either maximum frequency or random.
    predicted_class = max(vec_min, key=vec_min.get)
    #if it matches , then we know that prediction is correct and we Increment the count.
    if predicted_class == test__data[i][11]:
        count += 1
#calculating accuracy of 3NN by diving it with totalLength length of test data ......
acc_3NN = count / totalLength

#Printing statements.
print("Accuracy of 1-NN is"  , acc_1NN , "and Accuracy of 3-NN is", acc_3NN)
