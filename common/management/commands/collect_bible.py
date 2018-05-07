from django.core.management.base import BaseCommand
import requests
from bs4 import BeautifulSoup
from pprint import pprint

import time
import random

from common.models import Bible


class Command(BaseCommand):
    bible_index = {
        "1": ("창세기", "창"),
        "2": ("출애굽기", "출"),
        "3": ("레위기", "레"),
        "4": ("민수기", "민"),
        "5": ("신명기", "신"),
        "6": ("여호수아", "수"),
        "7": ("사사기", "삿"),
        "8": ("룻기", "룻"),
        "9": ("사무엘상", "삼상"),
        "10": ("사무엘하", "삼하"),
        "11": ("열왕기상", "왕상"),
        "12": ("열왕기하", "왕하"),
        "13": ("역대상", "대상"),
        "14": ("역대하", "대하"),
        "15": ("에스라", "스"),
        "16": ("느헤미야", "느"),
        "17": ("에스더", "에"),
        "18": ("욥기", "욥"),
        "19": ("시편", "시"),
        "20": ("잠언", "잠"),
        "21": ("전도서", "전"),
        "22": ("아가", "아"),
        "23": ("이사야", "사"),
        "24": ("예레미야", "렘"),
        "25": ("예레미야 애가", "애"),
        "26": ("에스겔", "겔"),
        "27": ("다니엘", "단"),
        "28": ("호세아", "호"),
        "29": ("요엘", "욜"),
        "30": ("아모스", "암"),
        "31": ("오바댜", "옵"),
        "32": ("요나", "욘"),
        "33": ("미가", "미"),
        "34": ("나훔", "나"),
        "35": ("하박국", "합"),
        "36": ("스바냐", "습"),
        "37": ("학개", "학"),
        "38": ("스가랴", "슥"),
        "39": ("말라기", "말"),
        "40": ("마태복음", "마"),
        "41": ("마가복음", "막"),
        "42": ("누가복음", "눅"),
        "43": ("요한복음", "요"),
        "44": ("사도행전", "행"),
        "45": ("로마서", "롬"),
        "46": ("고린도전서", "고전"),
        "47": ("고린도후서", "고후"),
        "48": ("갈라디아서", "갈"),
        "49": ("에베소서", "엡"),
        "50": ("빌립보서", "빌"),
        "51": ("골로새서", "골"),
        "52": ("데살로니가전서", "살전"),
        "53": ("데살로니가후서", "살후"),
        "54": ("디모데전서", "딤전"),
        "55": ("디모데후서", "딤후"),
        "56": ("디도서", "딛"),
        "57": ("빌레몬서", "몬"),
        "58": ("히브리서", "히"),
        "59": ("야고보서", "약"),
        "60": ("베드로전서", "벧전"),
        "61": ("베드로후서", "벧후"),
        "62": ("요한1서", "요일"),
        "63": ("요한2서", "요이"),
        "64": ("요한3서", "요삼"),
        "65": ("유다서", "유"),
        "66": ("요한계시록", "계")
    }
    
    def handle(self, *args, **options):
        for testaments_number in range(1, 67):
            #  testaments_number 성서 구분 ex) 창세기: 1, 출애굽기: 2 .. 요한계시록: 66
            total_chapters = self.find_total_chapter(testaments_number=testaments_number)  # 마지막 장
            testament_name, testament_kr_code = self.bible_index['{}'.format(testaments_number)]
            order = testaments_number
            
            for chapter in range(1, total_chapters + 1):
                url = 'http://www.holybible.or.kr/B_RHV/cgi/bibleftxt.php?VR=GAE&VL={TN}&CN={chapter}&CV=99'.format(TN=testaments_number, chapter=chapter)
                response =requests.get(url)
                response.encoding = 'euc-kr'
                html_doc = response.text
                soup = BeautifulSoup(html_doc, "html.parser")
                
                verses = self.find_text(soup=soup)
                total_verses = len(verses)
                
                for verse_info in verses:
                    if Bible.objects.filter(testament_name=testament_name, order=order, chapter=chapter, verse=verse_info[0]).exists():
                        pass
                    else:
                        Bible.objects.create(
                            testament_name=testament_name,
                            testament_kr_code=testament_kr_code,
                            order=order,
                            chapter=chapter,
                            verse=verse_info[0],
                            contents=verse_info[1],
                            total_chapters=total_chapters,
                            total_verses=total_verses,
                        )
                time.sleep(random.randrange(1, 4))
            
    def find_total_chapter(self, testaments_number):
        # testaments_number 성서 구분 ex) 창세기: 1, 출애굽기: 2 .. 요한계시록: 66
        url = 'http://www.holybible.or.kr/B_RHV/cgi/bibleftxt.php?VR=GAE&VL={TN}&CN={chapter}&CV=99'.format(TN=testaments_number, chapter=1)
        response = requests.get(url)
        response.encoding = 'euc-kr'
        html_doc = response.text
    
        soup = BeautifulSoup(html_doc, "html.parser")
        tags = soup.find_all('td', class_='tk3')
        
        result_set = list()
        for tag in tags:
            text = tag.text
            result_set.append(text.strip())

        index = result_set[2].split('\t\t')
        last_chapter = index[-2].strip()

        return int(last_chapter)
    
    def find_text(self, soup):
        verse_tags = soup.find_all('font', class_='tk4l')
    
        result = list()
        for index, tags in enumerate(verse_tags):
            text = tags.text.strip()
            result.append((index+1, text))
            #  result의 index + 1 이 verse
    
        pprint(result)
        return result