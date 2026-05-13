import re

phone_re = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phone_re.search('My number is 415-555-4242.')

mo.group(1)  # Returns the first group of the matched text
'415'
print(mo.group(2))  # Returns the second group of the matched text
'555-4242'
print(mo.group(0))  # Returns the full matched text
'415-555-4242'
print(mo.group())  # Also returns the full matched text
'415-555-4242'

mo.groups()
#('415', '555-4242')
area_code, main_number = mo.groups()
print(area_code)
'415'
print(main_number)
'555-4242'
