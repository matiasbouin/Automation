#! python3

import webbrowser, sys, pyperclip as ppc

sys.argv

if len(sys.argv) > 1:
    address = ' '.join(sys.argv[1:])
else:
    address = ppc.paste()

webbrowser.open('https://www.google.com.ar/maps/place/' +str(address))
    

