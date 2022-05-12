import csv
import pandas as pd


df_1 = []
df_2 = []
df_2 = pd.read_csv('dwarf_stars.csv')

'''
with open('dwarf_stars.csv','r') as f:
    csv_reader = csv.reader(f)
    for row in csv_reader:
        df_2.append(row)
'''
df_2 = df_2[df_2['Radius'].notna()]

for i in df_2[4]:
    i = float(i)
    i = i * 0.102763

'''
for k in df_2[3]:
    k.to_float()
    k = k * 0.000954588



header_1 = dataset_1[0]
planet_data_1 = dataset_1[1:]
header_2 = dataset_2[0]
planet_data_2 = dataset_2[1:]

headers = header_1 + header_2
planet_data = []

for index,data_row in enumerate(planet_data_1):
    planet_data.append(planet_data_1[index]+planet_data_2[index])

with open('planet_data.csv','a+') as f:
    csv_writer = csv.writer(f)
    csv_writer.writerow(headers)
    csv_writer.writerows(planet_data)
'''