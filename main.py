import csv
import os
from justdial import justdial_csv
import sys

def readcities(cityfile):
    cities = {}
    with open(cityfile) as citylist:
        cities = citylist.readlines()
        for i in range(len(cities)):
            cities[i] = cities[i].strip()
    return cities
def main(inputfile,cityfile):
    with open(inputfile) as inputfile:
        cities = readcities(cityfile)
        csv_reader = csv.reader(inputfile)
        for row in csv_reader:
            for city in cities:
                url = row[0].format(city)
                filename = row[1] + '-{}.csv'.format(city)
                filename = row[1] + '-{}.csv'.format(city)
                print("URL: {} , filename: {} ".format(url,filename))
                try:
                    justdial_csv(url,filename)
                except:
                    print('There was some error while downloading current data')
                    with open('logfile','a') as logfile:
                        logfile.write('Error occured with URL {} and filename {}'.format(url,filename))

                        
if __name__ == '__main__':
    if sys.argv[2]:
        cityfile = sys.argv[2]
    else:
        print('Usage: python main.py input.csv cities')
        sys.exit(1)
    if sys.argv[1]:
        inputfile = sys.argv[1]
    else:
        print('Usage: python main.py input.csv cities')
        sys.exit(1)
    try:
        os.mkdir('output')
    except:
        print("There was some error creating output directory , delete existing output directory")
    main(inputfile,cityfile)
