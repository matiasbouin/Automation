#! python3

'''
Steps: Copy text to the clipboard, execute this program, copy new values
from the clipboard to wherever you need to.

Once executed, this program will read the
text previously copied in the clipboard, then 
extract all numbers and e-mails and copy them
back to the clipboard for later use.

Also displays a message with the respective values.

'''

import pyperclip as ppc
import re

text = ppc.paste()


number_pattern = re.compile(r'''(
                (\W{1})?                       #Symbol
                (\d{2}|\d{3}|\d{4})?     #International area code
                (\s|-|\.)?                        #Space  
                (\d{2}|\d{4})?              #National area code 
                (\s|-|\.)?
                (\d{4})                         #First 4 numbers
                (\s|-|\.)?           
                (\d{4})                         #Last 4 numbers
                )''', re.VERBOSE)


mail_pattern = re.compile(r'''(
                (\w+)                           #First part of mail address
                (@)                              #@
                (\w+)                           #Seconds part of mail address
                (.com)                         #.com 
                (.\w{2})?                     #Optional 
                )''',re.VERBOSE | re.I)


number_search = number_pattern.findall(text)
mail_search = mail_pattern.findall(text)


numbers = [x[0] for x in number_search]
mails = [x[0] for x in mail_search]


values = ' '.join(numbers) + '\n' + '\n'.join(mails)


ppc.copy(values)


if number_search == []:
    print ('No phone numbers were found')
else:
    print ('Your numbers are:\n', numbers)
    print ('\nYour numbers are now stored in the clipboard')


print('\n--------\n')    


if mail_search == []:
    print ('No mails were found')
else:
    print ('Your mails are:\n', mails)
    print ('\nYour mails are now stored in the clipboard')



