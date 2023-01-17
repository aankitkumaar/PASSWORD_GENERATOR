# pasword generator
# stroe Password

import random

SMALL = "abcdefghijklmnopqrstuvwxyz"
CAPITAL = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
NUMBER = "123456787890"
SPECIAL = "!@#$%^&*()_+}{|:<>?"

#User Data
arr = []


def validatation(newPass):
    smallFlag = False
    capitalFlag = False
    numberFlag = False
    specialFlag = False
    for i in newPass:
        if i in SMALL:
            smallFlag = True
        if i in CAPITAL:
            capitalFlag = True
        if i in NUMBER:
            numberFlag = True
        if i in SPECIAL:
            specialFlag = True

    if smallFlag == True and capitalFlag == True and numberFlag == True and specialFlag == True:
        return True
    else:
        return False


def generatePass(length, ismail, iscap, isnum, isspc, ):
    password = ""
    if ismail:
        for i in range(length):
            password += SMALL[random.randint(0, len(SMALL) - 1)]

    if iscap:
        for i in range(length):
            password += CAPITAL[random.randint(0, len(CAPITAL) - 1)]

    if isnum:
        for i in range(length):
            password += NUMBER[random.randint(0, len(NUMBER) - 1)]

    if isspc:
        for i in range(length):
            password += SPECIAL[random.randint(0, len(SPECIAL) - 1)]

    # print(password)
    newPass = " "
    for i in range(length):
        newPass += password[random.randint(0, len(password) - 1)]
    if validatation(newPass):
        print(newPass)
        return newPass
    else:
        generatePass(8, True, True, True, True)


def Store_Data(site, username):
    # psd = generatePass(8, True, True, True, True)
    # print(psd)
    arr.append({"website": site, "user": username, "pass": generatePass(8, True, True, True, True)})


Store_Data("www.google.com", "ankit0170")
print(arr)
