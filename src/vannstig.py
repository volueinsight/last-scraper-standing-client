from base_loader import BaseLoader

class Vannstig(BaseLoader):

    def parse_data(self, data):
        return sum([int(e[1]) for e in zip(*[l.split(',') for l in data.read().split('\n')]) if e[0] in ['Stordalselva', 'Oselva', 'Litlelva', 'Moaelva', 'Mittetelva']])


Vannstig('vannstig').run()
