import requests
from io import StringIO
from time import sleep
GAME_URL =  'http://localhost:8000'
TEAM_TOKEN = 'lrmphfgtkf'
SLEEP_TIME = 10

class BaseLoader:
    """This is the base scraper class. It is not very useable on its own
    but should be used as a parent class.
    Args:
        name (str): Name of the source in the api. To see a list visit {GAME_URL}/datasource
    """

    def __init__(self, name):
        self.name = name
        self.data_endpoint = f'{GAME_URL}/api/datasource/{self.name}/data'
        self.desc_endpoint = f'{GAME_URL}/api/datasource/{self.name}/current?format=json'
        self.history_endpoint = f'{GAME_URL}/api/datasource/{self.name}/history'
        print(f'Data is available here: {self.data_endpoint}')
        print(f'Historic descriptions are available here: {self.history_endpoint}')

    def get_description(self):
        res = requests.get(self.desc_endpoint)
        try:
            j = res.json()
            return j.get('desc')
        except Exception as e:
            return res.text

    def get_data(self):
        return requests.get(self.data_endpoint).text

    def send_result(self, result):
        data = {'result': result, 'access_token': TEAM_TOKEN}
        response = requests.post(self.data_endpoint,
                                 data=data)
        print(response.text)
        return response.text == 'Correct!'

    def parse_data(self, data):
        raise NotImplementedError('Needs to be implemented and called on a child class')

    def run(self):
        correct = True
        while correct:
            desc = self.get_description()
            print('Current description:')
            print(desc)
            f = StringIO(self.get_data())
            result = self.parse_data(f)
            print(f'Calculated result:{result}')
            correct = self.send_result(result)
            if correct:
                print(f'Correct result! Trying again in {SLEEP_TIME} seconds')
                sleep(SLEEP_TIME)
        print('Loader broke due to incorrectness in the data. Restart the script when you want to try again. \nGood luck!')
