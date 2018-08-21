# -*- coding: utf-8 -*-
"""
Created on Tue Aug 21 22:04:03 2018

@author: Natthinee
"""

import requests
import os

def test():
    k = 0
    url = 'https://nonggodaun.plearnjai.com/U2cd26d49ace18bd6cfce4e53160808cbph6yby7u.m4a'
    print (url)
    r = requests.get(url)
    with open('kim'+'.m4a', 'wb') as f:  
        k = f.write(r.content)
    return  str(open('kim.m4a'))
        
        
