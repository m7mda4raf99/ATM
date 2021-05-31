from pin import viewsHome
from django.shortcuts import render
from django.http import HttpResponse

global pinEntered
pinEntered = ['_','_','_','_']

global error
error = ""

global card_number
card_number = ""

# Create your views here.
def returnRender(request):
    return render(request, 'pinPass.html', {
        'first': pinEntered[0],
        'second': pinEntered[1],
        'third': pinEntered[2],
        'fourth': pinEntered[3],
        'error': error
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

    i = index()

    if i != -1:
        pinEntered[i] = '1'
        error = ""
    else:
        error = "PASSWORD IS FULL!"    
    return returnRender(request)

def two(request):
    global error

    i = index()

    if i != -1:
        pinEntered[i] = '2'
        error = ""
    else:
        error = "PASSWORD IS FULL!"     

    return returnRender(request)

def three(request):
    global error 

    i = index()

    if i != -1:
        pinEntered[i] = '3'
        error = ""
    else:
        error = "PASSWORD IS FULL!" 

    return returnRender(request)

def four(request):
    global error
    
    i = index()

    if i != -1:
        pinEntered[i] = '4'
        error = ""
    else:
        error = "PASSWORD IS FULL!"     

    return returnRender(request)

def five(request):
    global error
    
    i = index()

    if i != -1:
        pinEntered[i] = '5'
        error = ""
    else:
        error = "PASSWORD IS FULL!"     

    return returnRender(request)

def six(request):
    global error
    
    i = index()

    if i != -1:
        pinEntered[i] = '6'
        error = ""
    else:
        error = "PASSWORD IS FULL!"     

    return returnRender(request)

def seven(request):
    global error
    
    i = index()

    if i != -1:
        pinEntered[i] = '7'
        error = ""
    else:
        error = "PASSWORD IS FULL!"     
    
    return returnRender(request)

def eight(request):
    global error
    
    i = index()

    if i != -1:
        pinEntered[i] = '8'
        error = ""
    else:
        error = "PASSWORD IS FULL!"     
    
    return returnRender(request)

def nine(request):
    global error
    
    i = index()

    if i != -1:
        pinEntered[i] = '9'
        error = ""
    else:
        error = "PASSWORD IS FULL!"     
    
    return returnRender(request)

def zero(request):
    global error

    i = index()

    if i != -1:
        pinEntered[i] = '0'
        error = ""
    else:
        error = "PASSWORD IS FULL!"     
    
    return returnRender(request)

def clear(request):
    global pinEntered
    pinEntered = ['_','_','_','_']

    global error
    error = ""

    return returnRender(request)

def enter(request):
    global error 
    global card_number

    i = index()

    if i == -1:
        password = "" 
        for i in pinEntered:
            password += i


        # if password is correct 
        if viewsHome.checkPass(card_number, password):
            return render(request, 'pinEnter.html')          

        # if password is not correct 
        else:
            error = "PASSWORD IS INCORRECT!"
            return returnRender(request)
    else: 
        error = "PASSWORD IS MISSING!"
        return returnRender(request)
            

























