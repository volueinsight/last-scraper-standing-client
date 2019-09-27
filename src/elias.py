import csv
from base_loader import BaseLoader

class Elias(BaseLoader):

    def parse_data(self, data):
        reader = csv.reader(data, delimiter=',')
        diff = 0
        rows = 0
        for row in reader:
            try:
                diff = float(row[0]-row[1])
                rows += 1
            except ValueError:
                pass
        return diff/rows

Elias('elias').run()
