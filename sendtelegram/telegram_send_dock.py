import requests
from datetime import date


def send_document(filename):
    current_datetime = date.today()
    token = '5695102982:AAFSOmvjR1wrEAjw30Ej0ZFwOknp8jFb07w'
    chat_id = -835180486
    url = 'https://api.telegram.org/bot{}/sendDocument'.format(token)
    data = {'chat_id': chat_id, 'caption': 'Domains check {}'.format(current_datetime)}
    with open(filename, 'rb') as f:
        files = {'document': f}
        response = requests.post(url, data=data, files=files)
        print(response.json())
