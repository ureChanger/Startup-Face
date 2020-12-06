#!/usr/bin/python
#-*- coding:utf-8 -*-
from download_image import persist_image
import os


target_name = "your keyword"
img_urls = ["img_url"] 

target_folder = os.path.join("images/"+target_name)
    
if not os.path.exists(target_folder):
    os.makedirs(target_folder)
        
for elem in img_urls:
    persist_image(target_folder, elem)