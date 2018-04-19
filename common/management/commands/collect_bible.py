from django.core.management.base import BaseCommand
import requests
from bs4 import BeautifulSoup
from pprint import pprint


class Command(BaseCommand):
    def handle(self, *args, **options):
        testaments_number = 50  # 성서 구분 ex) 창세기: 1, 출애굽기: 2 .. 요한계시록: 66
        chapter = 1  # 장
        verse = int()
        url = 'http://www.holybible.or.kr/B_RHV/cgi/bibleftxt.php?VR=GAE&VL={TN}&CN={chapter}&CV=99'.format(TN=testaments_number, chapter=chapter)
        response =requests.get(url)
        response.encoding = 'euc-kr'
        html_doc = response.text
        
        soup = BeautifulSoup(html_doc, "html.parser")
        verse_tags = soup.find_all('font', class_='tk4l')
        
        result = list()
        for tags in verse_tags:
            text = tags.text
            result.append(text)
        
        pprint(result)
