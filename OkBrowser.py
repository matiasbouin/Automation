#! python3

'''
Daily browser setup automation
'''

import webbrowser, sys

sys.argv

webbrowser.open('https://www.udemy.com')
webbrowser.open('https://www.hackerrank.com')
webbrowser.open('https://www.github.com')
webbrowser.open('https://www.gmail.com')

                

for i in sys.argv[1:]:
    webbrowser.open('https://www.'+i+'.com')
    print('Ok just oppened https://www.'+i+'.com')

