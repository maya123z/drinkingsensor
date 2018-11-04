import pandas as pd

def drinking(file):
    data = pd.read_table(file, delimiter=',', header=None).T
    splitdata = data[0].str.split(' ', expand=True)
    splitdata[2] = pd.to_numeric(splitdata[2])
    splitdata = splitdata[pd.notna(splitdata[1])]
    splitdata[3] = splitdata[2].diff()
    unbrok = splitdata[splitdata[1].str.contains('Unbrok')]
    timedrinking = unbrok[3].sum()
    drinkingbouts = unbrok[unbrok[3] >= 500].count()[3]
    return([file, timedrinking, drinkingbouts])

import os

results = list()

for root, dirs, files in os.walk("."):
    for filename in files:
        if 'txt' in filename:
            results.append(drinking(filename))

import datetime

df = pd.DataFrame(results, columns=['File Name', 'Amt Time Drinking', 'DrinkingBouts'])
today = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + '.xlsx'
writer = pd.ExcelWriter(today)
df.to_excel(writer, index=False)
writer.save()