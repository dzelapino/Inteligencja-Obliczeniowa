from cProfile import label
import csv
import pandas as pd
import matplotlib.pyplot as pyplot

with open('miasta.csv', 'r') as miasta:
    csvreader = csv.reader(miasta)
    header = []
    header = next(csvreader)
    rows = []
    for row in csvreader:
        rows.append(row)
    miasta.close()

# print(header)
# print(rows)

miasta = pd.read_csv('miasta.csv')
# print(miasta)
# print(miasta.values)
# print(miasta["Gdansk"].values)

# dataToAdd = '\n2010,460,555,405'
# with open('miasta.csv', 'a') as miasta:
#     miasta.write(dataToAdd)
#     miasta.close()

# pyplot.plot(miasta["Rok"].values, miasta["Gdansk"].values, color='red')
# pyplot.suptitle('Population of Gdansk')
# pyplot.xlabel('Year')
# pyplot.ylabel('Population')
# pyplot.show()

pyplot.plot(miasta["Rok"].values, miasta["Gdansk"].values,
            color='green', label='Danzig')
pyplot.plot(miasta["Rok"].values, miasta["Poznan"].values,
            color='blue', label='Posen')
pyplot.plot(miasta["Rok"].values, miasta["Szczecin"].values,
            color='red', label='Stettin')
pyplot.suptitle('Population in Polish cities')
pyplot.xlabel('Year')
pyplot.ylabel('Population')
pyplot.legend(loc='best')
pyplot.show()
