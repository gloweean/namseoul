from django.core.management.base import BaseCommand
import requests
from bs4 import BeautifulSoup
from pprint import pprint

import time
import random

from common.models import Bible


class Command(BaseCommand):
    bible_index = {
        "1": ("Genesis", "Gen"),
        "2": ("Exodus", "Exo"),
        "3": ("Leviticus", "Lev"),
        "4": ("Numbers", "Num"),
        "5": ("Deuteronomy", "Deu"),
        "6": ("Joshua", "Jos"),
        "7": ("Judges", "Jdg"),
        "8": ("Ruth", "Rut"),
        "9": ("1Samuel", "1sa"),
        "10": ("2Samuel", "2sa"),
        "11": ("1Kings", "1ki"),
        "12": ("2Kings", "2ki"),
        "13": ("1Chronicles", "1ch"),
        "14": ("2Chronicles", "2ch"),
        "15": ("Ezra", "Ezr"),
        "16": ("Nehemiah", "Neh"),
        "17": ("Esther", "Est"),
        "18": ("Job", "Job"),
        "19": ("Psalms", "Psa"),
        "20": ("Proverbs", "Pro"),
        "21": ("Ecclesiastes", "Ecc"),
        "22": ("Song of Solomon", "Sol"),
        "23": ("Isaiah", "Isa"),
        "24": ("Jeremiah", "Jer"),
        "25": ("Lamentations", "Lam"),
        "26": ("Ezekiel", "Eze"),
        "27": ("Daniel", "Dan"),
        "28": ("Hosea", "Hos"),
        "29": ("Joel", "Joe"),
        "30": ("Amos", "Amo"),
        "31": ("Obadiah", "Oba"),
        "32": ("Jonah", "Jon"),
        "33": ("Micah", "Mic"),
        "34": ("Nahum", "Nah"),
        "35": ("Habakkuk", "Hab"),
        "36": ("Zephaniah", "Zep"),
        "37": ("Haggai", "Hag"),
        "38": ("Zechariah", "Zec"),
        "39": ("Malachi", "Mal"),
        "40": ("Matthew", "Mat"),
        "41": ("Mark", "Mar"),
        "42": ("Luke", "Luk"),
        "43": ("John", "Joh"),
        "44": ("The Acts", "Act"),
        "45": ("Romans", "Rom"),
        "46": ("1Corinthians", "1co"),
        "47": ("2Corinthians", "2co"),
        "48": ("Galatians", "Gal"),
        "49": ("Ephesians", "Eph"),
        "50": ("Philippians", "Phi"),
        "51": ("Colossians", "Col"),
        "52": ("1Thessalonian", "1th"),
        "53": ("2Thessalonian", "2th"),
        "54": ("1Timothy", "1ti"),
        "55": ("2Timothy", "2ti"),
        "56": ("Titus", "Tit"),
        "57": ("Philemon", "Phm"),
        "58": ("Hebrews", "Heb"),
        "59": ("James", "Jam"),
        "60": ("1Peter", "1pe"),
        "61": ("2Peter", "2pe"),
        "62": ("1John", "1jo"),
        "63": ("2John", "2jo"),
        "64": ("3John", "3jo"),
        "65": ("Jude", "Jud"),
        "66": ("Revelation", "Rev")
    }
    
    def handle(self, *args, **options):
        for testaments_number in range(1, 67):
            #  testaments_number 성서 구분 ex) 창세기: 1, 출애굽기: 2 .. 요한계시록: 66
            total_chapters = self.find_total_chapter(testaments_number=testaments_number)  # 마지막 장
            testament_name, testament_en_code = self.bible_index['{}'.format(testaments_number)]
            order = testaments_number
            
            for chapter in range(1, total_chapters + 1):
                url = 'http://www.holybible.or.kr/B_NIV/cgi/bibleftxt.php?VR=NIV&VL={TN}&CN={chapter}&CV=99'.format(TN=testaments_number, chapter=chapter)
                response =requests.get(url)
                response.encoding = 'euc-kr'
                html_doc = response.text
                soup = BeautifulSoup(html_doc, "html.parser")
                
                verses = self.find_text(soup=soup)
                total_verses = len(verses)

    def find_total_chapter(self, testaments_number):
        # testaments_number 성서 구분 ex) 창세기: 1, 출애굽기: 2 .. 요한계시록: 66
        url = 'http://www.holybible.or.kr/B_NIV/cgi/bibleftxt.php?VR=NIV&VL={TN}&CN={chapter}&CV=99'.format(TN=testaments_number, chapter=1)
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
            result.append((index + 1, text))
            #  result의 index + 1 이 verse
    
        pprint(result)
        return result