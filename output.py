import json

array = [] #creating array

for i in range(1, 101): #1 to 100
    if i % 3 == 0 and i % 5 == 0: 
        array.append("BIGBANG") #if divisible by 3 and 5
    elif i % 3 == 0:
        array.append("BIG") #if divisible by 3
    elif i % 5 == 0:
        array.append("BANG") #if divisible by 5
    else:
        array.append(str(i))

with open("output.json", "w") as output: #open output.json file and write results
    json.dump(array, output)
