import numpy as np
import matplotlib.pyplot as plt
import urllib.request
import json
import pandas

def getTempAt(data, station):
    cities = list(data['stacja'].values)
    if cities.__contains__(station):
        return data.iloc[cities.index(station)]
    else:
        return "Stacja nie istnieje"

def minmaxaverage(data):
    lowesttemp = {'city': '',
                  'temp': 0}
    highesttemp = {'city': '',
                   'temp': 0}
    sumoftemps = 0
    temps = list(data['temperatura'].values)

    for i in temps:
        sumoftemps = sumoftemps + float(i)
        if lowesttemp.get('temp') > float(i):
            lowesttemp.update({'city': data.iloc[temps.index(i)].get('stacja'),
                               'temp': float(i)})
        if highesttemp.get('temp') < float(i):
            highesttemp.update({'city': data.iloc[temps.index(i)].get('stacja'),
                                'temp': float(i)})

    return [lowesttemp, highesttemp, sumoftemps / len(temps)]

if __name__=="__main__":
    data = urllib.request.urlopen("https://danepubliczne.imgw.pl/api/data/synop")
    data=json.loads(data.read())
    data=pandas.json_normalize(data)

    terminate=False
    while terminate==False:
        print("1. Dane pogodowe w podanym miescie")
        print("2. Najnizsza, najwyzsza i srednia temperatura")
        print("0. Zakoncz")

        option=input(": ")

        if option=='0':
            terminate=True
            break
        if option=='1':
            print(getTempAt(data, input("Wprowadz nazwe stacji: ")))

        if option=='2':
            info=minmaxaverage(data)
            print("Najnizsza temperatura: " + info[0].get('city') + " " + str(info[0].get('temp')))
            print("Najwyzsza temperatura: " + info[1].get('city') + " " + str(info[1].get('temp')))
            print("Srednia temperatura: " + str(info[2]))
