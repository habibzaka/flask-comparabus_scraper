import requests
from bs4 import BeautifulSoup
from tabulate import *
import csv

class ProxyScraper:
    results = []
    id1 = 1
    id2 = 1
    def __init__(self, from_data, to_data):
        self.from_data = from_data
        self.to_data = to_data

    
    def fetch(self, url):
        return requests.get(url)

    def parse(self, html):
        content = BeautifulSoup(html, 'lxml')
        table = content.find('table', class_="prices")
        rows = table.findAll('tr')
        #headers = [header.text for header in rows[0]]
        #results = [headers]
        for row in rows:
            if len(row.findAll('td')):
                self.results.append([data.text for data in row.findAll('td')])

    def to_csv(self):
        with open('liste.csv', 'w') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerows(self.results)
    
    def run(self):
        if self.from_data == 'Lille':
            id1=6
        if self.to_data == 'Lille':
            id2=6
        if self.from_data == 'Paris':
            id1=10
        if self.to_data == 'Paris':
            id2=10
        if self.from_data == 'Lyon':
            id1=704
        if self.to_data == 'Lyon':
            id2=704
        if self.from_data == 'Rennes':
            id1=348
        if self.to_data == 'Rennes':
            id2=348
        if self.from_data == 'Rouen':
            id1=349
        if self.to_data == 'Rouen':
            id2=349
        if self.from_data == 'Toulouse':
            id1=356
        if self.to_data == 'Toulouse':
            id2=356
            
        response = self.fetch('https://www.comparabus.com/fr/bus-' + self.from_data  + '-' + self.to_data + '-' + str(id1) + '-' + str(id2)) 
        self.parse(response.text)
        self.to_csv()

if __name__ == '__main__':
    scraper = ProxyScraper()
    scraper.run()





