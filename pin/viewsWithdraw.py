from pin import viewsHome, viewsPass
from django.shortcuts import render
from django.http import HttpResponse

global pinEntered
pinEntered = ['_','_','_','_']

global error 
error = ""

global success 
success = ""

# Create your views here.
def returnRender(request):
    return render(request, 'withdraw.html', {
        'first': pinEntered[0],
        'second': pinEntered[1],
        'third': pinEntered[2],
        'fourth': pinEntered[3],
        'error': error,
        'success': success
    })

def index():
    count = pinEntered.count('_')

    if count == 4:
        return 0
    elif count == 3:
        return 1
    elif count == 2:
        return 2
    elif count == 1:
        return 3
    elif count == 0:
        return -1                    

def one(request):
    global error
    global success
    success = ""

    i = index()

    if i != -1:
        pinEntered[i] = '1'
        error = ""
    else:
        error = "AMOUNT IS FULL!"
    return returnRender(request)

def two(request):
    global error
    global success
    success = ""

    i = index()

    if i != -1:
        pinEntered[i] = '2'
        error = ""
    else:
        error = "AMOUNT IS FULL!"

    return returnRender(request)

def three(request):
    global error
    global success
    success = ""

    i = index()

    if i != -1:
        pinEntered[i] = '3'
        error = ""
    else:
        error = "AMOUNT IS FULL!"

    return returnRender(request)

def four(request):
    global error
    global success
    success = ""

    i = index()

    if i != -1:
        pinEntered[i] = '4'
        error = ""
    else:
        error = "AMOUNT IS FULL!"

    return returnRender(request)

def five(request):
    global error
    global success
    success = ""

    i = index()

    if i != -1:
        pinEntered[i] = '5'
        error = ""
    else:
        error = "AMOUNT IS FULL!"

    return returnRender(request)

def six(request):
    global error
    global success
    success = ""

    i = index()

    if i != -1:
        pinEntered[i] = '6'
        error = ""
    else:
        error = "AMOUNT IS FULL!"

    return returnRender(request)

def seven(request):
    global error
    global success
    success = ""

    i = index()

    if i != -1:
        pinEntered[i] = '7'
        error = ""
    else:
        error = "AMOUNT IS FULL!"

    return returnRender(request)

def eight(request):
    global error
    global success
    success = ""

    i = index()

    if i != -1:
        pinEntered[i] = '8'
        error = ""
    else:
        error = "AMOUNT IS FULL!"

    return returnRender(request)

def nine(request):
    global error
    global success
    success = ""

    i = index()

    if i != -1:
        pinEntered[i] = '9'
        error = ""
    else:
        error = "AMOUNT IS FULL!"

    return returnRender(request)

def zero(request):
    global error
    global success
    success = ""

    i = index()

    if i != -1:
        pinEntered[i] = '0'
        error = ""
    else:
        error = "AMOUNT IS FULL!"

    return returnRender(request)

def clear(request):
    global pinEntered
    pinEntered = ['_', '_', '_', '_']

    global error
    error = ""

    global success
    success = ""

    return returnRender(request)

def enter(request):
    global pinEntered
    global success
    global error
    
    if pinEntered.count('_') < 4:
        withdrawed = ""

        for i in pinEntered:
            if i != "_":
                withdrawed += i

        balance = int (viewsHome.getBalance(viewsPass.card_number))
        withdrawed = int(withdrawed)

        if balance >= withdrawed:
            total = int(balance) - int(withdrawed)

            viewsHome.updateBalance(viewsPass.card_number, str(total))

            success = "AMOUNT IS WITHDRAWED SUCCESSFULLY!"
            pinEntered = ['_','_','_','_'] 
            error = ""
            return returnRender(request)

        else:
            success = ""
            error = "YOUR ACCOUNT BALANCE HAS ONLY $" + str(balance) +"!"
            return returnRender(request)

    else:
        success = ""
        error = "AMOUNT IS MISSING!"
        return returnRender(request)

def twoZero(request):
    global error
    global success
    success = ""

    if pinEntered.count('_') >= 2:
        error = ""
        i = index()
        pinEntered[i] = '0'
        i = index()
        pinEntered[i] = '0'
    else:
        error = "AMOUNT IS FULL!"

    return returnRender(request)

def threeZero(request):
    global error
    global success
    success = ""

    if pinEntered.count('_') >= 3:
        error = ""
        i = index()
        pinEntered[i] = '0'
        i = index()
        pinEntered[i] = '0'
        i = index()
        pinEntered[i] = '0'
    else:
        error = "AMOUNT IS FULL!"    

    return returnRender(request)

def back(request):
    return render(request, 'pinEnter.html')























