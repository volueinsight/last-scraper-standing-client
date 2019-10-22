import csv
from base_loader import BaseLoader


class Eqex(BaseLoader):
    def parse_data(self, data):
        reader = list(csv.reader(data, delimiter=','))
        min_close = 101
        for row in reader:
            if 'close' in row[3]:
                continue
            max_close = min(min_close, float(row[3]))
        return max_close
        
Eqex('eqex').run()
