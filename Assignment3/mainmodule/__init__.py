__author__ = 'chris'
from menus import mainmenu
from menus import collectprovinces
from menus import readlog

result='*'
while(result!='Q'):
    result=mainmenu()
    if result == '1':
        collectprovinces()
    elif result == '2':
        print("this function is not yet working.")
    elif result =='?':
        readlog()