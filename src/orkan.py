import csv
from base_loader import BaseLoader


class Orkan(BaseLoader):

    def parse_data(self, data):
        reader = csv.reader(data, delimiter=',')
        result = 0
        for row in reader:
            if row[-1] != 'hurricane':
                continue

            try:
                production_values = [float(row[i]) for i in (0, 1, 2)]
                result = min([result] + production_values)
            except ValueError:
                pass

        return result


Orkan('orkan').run()
