__author__ = 'chris'
from mainmodule.menus import mainmenu
from mainmodule.menus import collectprovinces


result=mainmenu()
if result == '1':
    collectprovinces()
elif result == '2':
    print("this function is not yet working.")
elif result =='?':
    print("this function is not yet working.")
elif result =='Q':
    print("Bye now, come back soon!.")