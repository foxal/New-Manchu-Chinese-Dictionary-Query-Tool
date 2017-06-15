New-Manchu-Chinese-Dictionary-Query-Tool
==========

> Hitoshi Kuribayashi launched a online dictionary ([満洲語辞典](http://hkuri.cneas.tohoku.ac.jp/guide/p06/)) in early 2017 which provides item and full text search of 新滿漢大詞典 and 滿漢大辞典. There are also other searchable electronic Manchu-Chinese dictionaries such as the Anami dictionary on iOS. Therefore, this tool becomes less useful now. 


This tool provides fast querying for the A Comprehensive Manchu-Chinese Dictionary (《新滿漢大詞典》). 

For a beginner who does not know the meaning of most words in Manchu texts, it can be quite time-consuming to look up those words in a paper-based dictionary.  Even a scholar with considerable ability in reading Manchu may encounter new words in Manchu primary resources. Written in python, this small tool can save a lot of time by telling the user the location of a word in the two dictionaries, or presenting the exact page directly to the user (a PDF reader is required for this function).

基本使用方法：
運行dict.exe，輸入要查找的單詞。拉丁轉寫暫時遵循《新滿漢大詞典》的規定（不是很好，有待改進）。

功能：
1、顯示單詞所在頁數（pdf文件頁數，非詞典內頁數）。由於下列原因，該頁數不一定完全準確：單詞可能不存在，在上一頁中也有該單詞的詞條內容，索引錯誤，或詞典內容錯誤。
2、使用第三方的pdf瀏覽軟件打開該單詞所在頁。
3、保存查詢記錄（單詞，頁數，查詢時間）

請使用settings.ini開啓或關閉功能2與功能3。若無法正確設置使用第三方pdf瀏覽軟件，則關閉功能2。設置方法詳見settings.ini文件內註釋。

By Yize Hu, yizehu@gmail.com, 27/5/2014. Written with python 2.7.
