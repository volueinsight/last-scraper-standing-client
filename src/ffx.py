import csv
from base_loader import BaseLoader

class Ffx(BaseLoader):

    def parse_data(self, data):
        reader = csv.reader(data, delimiter=',')
        closing_sum = 0
        rows = 0
        for row in reader:
            try:
                closing_sum += float(row[3])
                rows += 1
            except ValueError:
                pass
        return closing_sum/rows

Ffx('ffx').run()
