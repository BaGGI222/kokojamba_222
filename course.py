import requests
from bs4 import BeautifulSoup
from datetime import datetime


def get_course(id):
    return xml.find('valute', {'id': id}).value.text
def get_course_2(Name):
    return xml.find('valute', {'<Name>': Name}).valute.text 


url = 'https://www.cbr.ru/scripts/XML_daily.asp?'
responce = requests.get(url, params={'date_req': datetime.today().strftime('%d/%m/%Y')})

xml = BeautifulSoup(responce.content, 'html.parser')

if __name__ == '__main__':
    print(get_course("R01235"))
    print(get_course("R01239"))
    print(get_course("R01035"))