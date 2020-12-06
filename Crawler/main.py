#!/usr/bin/python
#-*- coding:utf-8 -*-
from search_and_download import search_and_download


keyword = ["스테파니 리"]
max_image = 430
    
print("1. start search_and_download!")
    
for i in range(len(keyword)):
    search_term = keyword[i]
    search_and_download(search_term=search_term, number_images=max_image)
    print("{num}: {character} done!".format(num=i+1, character=search_term))
    
# 서달미 150
# 남도산 150
# 한지평 150
# 최원덕 90
# 원인재 100
# 차아현 84
# 이철산 100
# 정사하 100