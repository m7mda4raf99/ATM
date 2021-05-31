from pin import viewsDeposit, viewsPass, viewsWithdraw
from django.shortcuts import render
from django.http import HttpResponse

import cv2
import mediapipe
import numpy as np
import win32api
from win32api import GetSystemMetrics
import csv

from threading import Thread

###################### HOME #############################

global pinEntered
pinEntered = ['_', '_', '_', '_']

global error
error = ""

# Create your views here.


def returnRender(request):
    return render(request, 'pinHome.html', {
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


def hand_recognition():
    screenWidth = GetSystemMetrics(0)
    screenHeight = GetSystemMetrics(1)

    drawingModule = mediapipe.solutions.drawing_utils
    handsModule = mediapipe.solutions.hands

    capture = cv2.VideoCapture(0)

    # ENABLING FULLSCREEN
    cv2.namedWindow('Test hand', cv2.WND_PROP_FULLSCREEN)
    cv2.setWindowProperty(
        'Test hand', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

    # SETTING CAPTURE RESOLUTION TO THE MAXIMUM
    capture.set(3, screenWidth)
    capture.set(4, screenHeight)
    frameWidth = capture.get(cv2.CAP_PROP_FRAME_WIDTH)
    frameHeight = capture.get(cv2.CAP_PROP_FRAME_HEIGHT)

    with handsModule.Hands(static_image_mode=False, min_detection_confidence=0.7,
                           min_tracking_confidence=0.7, max_num_hands=1) as hands:

        while (True):
            ret, frame = capture.read()

            results = hands.process(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

            if results.multi_hand_landmarks != None:
                for handLandmarks in results.multi_hand_landmarks:
                    for point in handsModule.HandLandmark:

                        # GETTING LOCATION OF THE INDEX FINGERTIP
                        normalizedLandmark = handLandmarks.landmark[8]

                        pixelCoordinatesLandmark = drawingModule._normalized_to_pixel_coordinates(
                            normalizedLandmark.x, normalizedLandmark.y, frameWidth, frameHeight)

                        # CHANGING MOUSE CURSOR LOCATION TO BE SAME AS THE FINGERTIP
                        if pixelCoordinatesLandmark != None:

                            ratioWidth = screenWidth / frameWidth
                            ratioHeight = screenHeight / frameHeight

                            x = screenWidth - \
                                int(pixelCoordinatesLandmark[0] * ratioWidth)
                            y = int(pixelCoordinatesLandmark[1] * ratioHeight)

                            win32api.SetCursorPos((x, y))

                        cv2.circle(frame, pixelCoordinatesLandmark,
                                   5, (0, 0, 255), -1)

            # FLIPPING THE IMAGE HORIZONTALLY
            frame_flip = cv2.flip(frame, 1)

            cv2.imshow('Test hand', frame_flip)

            # CLOSING WINDOW WHEN PRESSING ESC
            if cv2.waitKey(1) == 27:
                break

    cv2.destroyAllWindows()
    capture.release()


def create():
    csv_writer = csv.writer(open('users.csv', 'w'), delimiter=',')
    csv_writer.writerow(['card_number', 'password', 'balance'])
    csv_writer.writerow(['1234', '1234', '5000'])
    csv_writer.writerow(['5678', '5678', '2000'])

# return list of users, each is also a list


def getUsers():
    users = []
    for row in csv.reader(open('users.csv', 'r'), delimiter=','):
        if len(row) > 0:
            users.append(row)
    return users

# give a list of users to overwrite data


def updateUsers(users):
    csv_writer = csv.writer(open('users.csv', 'w'), delimiter=',')
    for i in users:
        csv_writer.writerow(i)

# return True if user exists


def searchUser(card_number):
    users = getUsers()

    for user in users:
        if user[0] == card_number:
            return True

    return False

# return True if password is correct


def checkPass(card_number, password):
    users = getUsers()

    for user in users:
        if user[0] == card_number:
            if user[1] == password:
                return True

    return False

# return the balance of a user


def getBalance(card_number):
    users = getUsers()

    for user in users:
        if user[0] == card_number:
            return user[2]
    return None


def updateBalance(card_number, new_balance):
    users = getUsers()

    for user in users:
        if user[0] == card_number:
            user[2] = new_balance

    updateUsers(users)


def home(request):
    Thread(target = hand_recognition).start()
    # create()

    global pinEntered
    pinEntered = ['_', '_', '_', '_']

    return returnRender(request)


def one(request):
    global error

    i = index()

    if i != -1:
        pinEntered[i] = '1'
        error = ""
    else:
        error = "CARD NUMBER IS FULL!"
    return returnRender(request)


def two(request):
    global error

    i = index()

    if i != -1:
        pinEntered[i] = '2'
        error = ""
    else:
        error = "CARD NUMBER IS FULL!"

    return returnRender(request)


def three(request):
    global error

    i = index()

    if i != -1:
        pinEntered[i] = '3'
        error = ""
    else:
        error = "CARD NUMBER IS FULL!"

    return returnRender(request)


def four(request):
    global error

    i = index()

    if i != -1:
        pinEntered[i] = '4'
        error = ""
    else:
        error = "CARD NUMBER IS FULL!"

    return returnRender(request)


def five(request):
    global error

    i = index()

    if i != -1:
        pinEntered[i] = '5'
        error = ""
    else:
        error = "CARD NUMBER IS FULL!"

    return returnRender(request)


def six(request):
    global error

    i = index()

    if i != -1:
        pinEntered[i] = '6'
        error = ""
    else:
        error = "CARD NUMBER IS FULL!"

    return returnRender(request)


def seven(request):
    global error

    i = index()

    if i != -1:
        pinEntered[i] = '7'
        error = ""
    else:
        error = "CARD NUMBER IS FULL!"

    return returnRender(request)


def eight(request):
    global error

    i = index()

    if i != -1:
        pinEntered[i] = '8'
        error = ""
    else:
        error = "CARD NUMBER IS FULL!"

    return returnRender(request)


def nine(request):
    global error

    i = index()

    if i != -1:
        pinEntered[i] = '9'
        error = ""
    else:
        error = "CARD NUMBER IS FULL!"

    return returnRender(request)


def zero(request):
    global error

    i = index()

    if i != -1:
        pinEntered[i] = '0'
        error = ""
    else:
        error = "CARD NUMBER IS FULL!"

    return returnRender(request)


def clear(request):
    global pinEntered
    pinEntered = ['_', '_', '_', '_']

    global error
    error = ""

    return returnRender(request)


def enter(request):
    global error

    i = index()

    if i == -1:
        card_number = ""
        for i in pinEntered:
            card_number += i

        # if card number exists
        if searchUser(card_number):
            viewsPass.card_number = card_number
            viewsPass.pinEntered = ['_', '_', '_', '_']

            return render(request, 'pinPass.html', {
                'first': "_",
                'second': "_",
                'third': "_",
                'fourth': "_",
                'error': ""
            })
        # if card number doesn't exist
        else:
            error = "THIS CARD NUMBER DOESN'T EXIST!"
            return returnRender(request)

    else:
        error = "CARD NUMBER IS MISSING!"
        return returnRender(request)

###################### OPTIONS #############################

def withdraw(request):
    viewsWithdraw.pinEntered = ['_', '_', '_', '_']
    viewsWithdraw.success = ""
    viewsWithdraw.error = ""

    return render(request, 'withdraw.html', {
        'first': '_',
        'second': '_',
        'third': '_',
        'fourth': '_',
        'error': '',
        'success': ''
    })

def deposit(request):
    viewsDeposit.pinEntered = ['_', '_', '_', '_']
    viewsDeposit.success = ""
    viewsDeposit.error = ""

    return render(request, 'deposit.html', {
        'first': '_',
        'second': '_',
        'third': '_',
        'fourth': '_',
        'error': '',
        'success': ''
    })

def balance(request):
    balance = getBalance(viewsPass.card_number)   
     
    return render(request, 'balance.html',{
        'balance': balance
    })
