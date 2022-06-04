import json

#function to find the common factors
def had_common(len_shipment, len_driver):
    for i in range(1,min(len_shipment,len_driver)+1):
        if len_shipment%i == len_driver%i == 0:
            return True
    return False

#function to get the ss
def get_ss(shipment, driver):
    ss = 0
    if (len(shipment) % 2) == 0:
        driver_lower = driver.lower()
        for vowel in "aeiou":
            count = driver_lower.count(vowel)
            ss = ss + count
        ss = ss*1.5
    else:
        driver_lower = driver.lower()
        vowels = ['a', 'e', 'i', 'o', 'u']
        for x in driver_lower:
            if x not in vowels and x != ' ':
                ss = ss + 1
    if (had_common(len(shipments), len(drivers))):
        ss = ss + (ss/2)
    return ss
  
#reading data
shipments_json = raw_input("Type the name of the shipments file: ")
f = open(shipments_json)
data = json.load(f)
shipments = []
for element in data['shipments']:
    shipments.append(str(element))
drivers_json = raw_input("Type the name of the drivers file: ")
f = open(drivers_json)
data = json.load(f)
drivers = []
for element in data['drivers']:
    drivers.append(str(element))
#reading data

#getting ss matrix
ss_matrix = []
for shipment in shipments:
    array_shipment = []
    for driver in drivers:
        ss=get_ss(shipment, driver)
        array_shipment.append(ss)
    ss_matrix.append(array_shipment)

#searching for the best path to maximaze ss
path = [-1]; total_ss = 0
for i in range(len(ss_matrix)):
    maxss = 0; maxi = -1;
    for j in range(len(ss_matrix[i])):
        if (j not in path and ss_matrix[i][j] > maxss):
            maxss = ss_matrix[i][j]
            maxi = j
    path.append(maxi)
    total_ss = total_ss + maxss

#printing the results
print("The max ss found is: ", total_ss)
relation_array = []
for i in range(len(path)-1):
    relation_array.append((shipments[i], drivers[path[i+1]]))
print("The final relation is like this: ", relation_array)
f.close()