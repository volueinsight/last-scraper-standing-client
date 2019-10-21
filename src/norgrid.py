import csv
from base_loader import BaseLoader


class Norgrid(BaseLoader):
    def parse_data(self, data):
        reader = list(csv.reader(data, delimiter=','))
        total = 0
        for row in reader[-25:-1]:
            for col in row[:3]:
                try:
                    total += float(col)
                except ValueError:
                    pass
        return total
        
Norgrid('norgrid').run()
