import csv
from base_loader import BaseLoader

class NordSnooker(BaseLoader):

    def parse_data(self, data):
        reader = csv.reader(data, delimiter=',')
        total = 0
        for row in reader:
            for col in row:
                try:
                    total += float(col)
                except ValueError:
                    pass
        return total

NordSnooker('nordsnooker').run()
