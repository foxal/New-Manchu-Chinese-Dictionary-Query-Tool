# -*- coding: utf-8 -*-
##A script for querying words in 《新滿漢大詞典》. Page number will be returned, and the page in dictionary pdf file will be opend. Searching history is stored in history.txt.
##By Yize
##files used by this script: numlist.csv, settings.ini, history.txt.
##dictnewmanju爲《新滿漢大詞典》所用字母對應的詞序。

dictnewmanju={"a":1, "b":2, "c":3, "d":4, "e":5, "f":6, "g":7, "h":8, "'":9, "i":10, "k":11, "l":12, "m":13, "n":14, "o":15, "p":16, "r":17, "s":18, "t":19, "u":20, "w":21, "y":22, "z":23}
def converttonum(word):
    """Convert a word to number."""
    wordnum=0
    index=6
    ##Convert
    for letter in word:
        ##Ilegal character is treated as 0.
        if letter in dictnewmanju:
            wordnum+=dictnewmanju[letter]*pow(23,index)
        index-=1
    return wordnum

import csv
import time
import subprocess
import ConfigParser

##Read configures from settings.ini
config = ConfigParser.SafeConfigParser({'openpdf': 0, 'savehistory': 1, 'command': '"C:\Program Files (x86)\Foxit Software\Foxit Reader\Foxit Reader.exe" C:\\Users\\adminadmin\\Documents\\課程\\满语初程\\電子詞典製作\\dict_python\\manchudict.pdf /A page='})
config.read('settings.ini')
openpdf = config.get('Section1','openpdf')
cmd = config.get('Section1','command')
savehistory = config.get('Section2','savehistory')

##Read numlist.csv to start searching.
with open('numlist.csv', 'rb') as f:
    reader = csv.reader(f)
    ##while loop for repeated searching.
    while True: 
        print 'Please input a word (press Enter to exit):'
        searchword = raw_input()
        searchwordnum = converttonum(searchword)
        if searchwordnum == 0:
            exit()
        print 'Word represented by number:', searchwordnum
        ##Search
        f.seek(0)
        for row in reader: 
            if float(row[0]) > searchwordnum:
                pagenum = int(row[1])-1
                print 'Word', '"', searchword, '"', 'is most probably on page', pagenum
                ##Write record (word, page number, and system time) to history.txt.
                if savehistory == '1':
                    with open('history.txt', 'a') as fhistory: 
                        historyrecord = searchword + ',' + str(pagenum) + ',' + time.strftime("%d/%m/%Y")+ ' ' + time.strftime("%H:%M:%S") + '\n'
                        fhistory.write(historyrecord)
                ##Open page in dictionary pdf file.
                if openpdf == '1':
                    arg = cmd + str(pagenum)
                    subprocess.call(arg)
                break
        ##Word is on the last page or not found.
        if searchwordnum >= float(row[0]): 
            pagenum = int(row[1])
            print 'Word', searchword, 'is on page', pagenum, '(last page) or cannot be found'
            ##Write record (word, page number, and system time) to history.txt.
            if savehistory == '1':
                with open('history.txt', 'a') as fhistory:
                    historyrecord = searchword + ',' + str(pagenum) + ',' + time.strftime("%d/%m/%Y")+ ' ' + time.strftime("%H:%M:%S") + '\n'
                    fhistory.write(historyrecord)
                ##Open page in dictionary pdf file.
                if openpdf == '1':
                    arg = cmd + str(pagenum)
                    subprocess.call(arg)
