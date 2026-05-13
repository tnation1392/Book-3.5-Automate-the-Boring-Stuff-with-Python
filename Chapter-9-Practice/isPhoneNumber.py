def _is_phone_number(text):
    if len(text) != 12:
        return False
    for i in range(0,3): #First three chars must be numbers
        if not text[i].isdecimal():
            return False
    if text[3] != '-': #Fourth char must be a dash
        return False
    for i in range(4,7):
        if not text[i].isdecimal(): #Next three chars must be numbers
            return False
    if text[7] != '-': #Eighth char must be a dash
        return False
    for i in range(8,12): #Last four chars must be numbers
        if not text[i].isdecimal():
            return False
    return True
#Test
print('is 415-555-4242 a phone number?', _is_phone_number('415-555-4242'))


