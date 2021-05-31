from pin import viewsHome, viewsWithdraw, viewsDeposit, viewsPass
from django.urls import path

urlpatterns = [
    path('', viewsHome.home, name = 'home'),
    path('one', viewsHome.one, name='one'),
    path('two', viewsHome.two, name='two'),
    path('three', viewsHome.three, name='three'),
    path('four', viewsHome.four, name='four'),
    path('five', viewsHome.five, name='five'),
    path('six', viewsHome.six, name='six'),
    path('seven', viewsHome.seven, name='seven'),
    path('eight', viewsHome.eight, name='eight'),
    path('nine', viewsHome.nine, name='nine'),
    path('clear', viewsHome.clear, name='clear'),
    path('zero', viewsHome.zero, name='zero'),
    path('enter', viewsHome.enter, name='enter'),
    path('onePass', viewsPass.one, name='one'),
    path('twoPass', viewsPass.two, name='two'),
    path('threePass', viewsPass.three, name='three'),
    path('fourPass', viewsPass.four, name='four'),
    path('fivePass', viewsPass.five, name='five'),
    path('sixPass', viewsPass.six, name='six'),
    path('sevenPass', viewsPass.seven, name='seven'),
    path('eightPass', viewsPass.eight, name='eight'),
    path('ninePass', viewsPass.nine, name='nine'),
    path('clearPass', viewsPass.clear, name='clear'),
    path('zeroPass', viewsPass.zero, name='zero'),
    path('enterPass', viewsPass.enter, name='enter'),
    path('withdraw', viewsHome.withdraw, name='withdraw'),
    path('deposit', viewsHome.deposit, name='deposit'),
    path('balance', viewsHome.balance, name='balance'),
    path('oneWithdraw', viewsWithdraw.one, name='oneWithdraw'),
    path('twoWithdraw', viewsWithdraw.two, name='twoWithdraw'),
    path('threeWithdraw', viewsWithdraw.three, name='threeWithdraw'),
    path('fourWithdraw', viewsWithdraw.four, name='fourWithdraw'),
    path('fiveWithdraw', viewsWithdraw.five, name='fourWithdraw'),
    path('sixWithdraw', viewsWithdraw.six, name='sixWithdraw'),
    path('sevenWithdraw', viewsWithdraw.seven, name='sevenWithdraw'),
    path('eightWithdraw', viewsWithdraw.eight, name='eightWithdraw'),
    path('nineWithdraw', viewsWithdraw.nine, name='nineWithdraw'),
    path('zeroWithdraw', viewsWithdraw.zero, name='zeroWithdraw'),
    path('twoZeroWithdraw', viewsWithdraw.twoZero, name='twoZeroWithdraw'),
    path('threeZeroWithdraw', viewsWithdraw.threeZero, name='threeZeroWithdraw'),
    path('clearWithdraw', viewsWithdraw.clear, name='clearWithdraw'),
    path('enterWithdraw', viewsWithdraw.enter, name='enterWithdraw'),
    path('backWithdraw', viewsWithdraw.back, name='backWithdraw'),
    path('oneDeposit', viewsDeposit.one, name='oneDeposit'),
    path('twoDeposit', viewsDeposit.two, name='twoDeposit'),
    path('threeDeposit', viewsDeposit.three, name='threeDeposit'),
    path('fourDeposit', viewsDeposit.four, name='fourDeposit'),
    path('fiveDeposit', viewsDeposit.five, name='fourDeposit'),
    path('sixDeposit', viewsDeposit.six, name='sixDeposit'),
    path('sevenDeposit', viewsDeposit.seven, name='sevenDeposit'),
    path('eightDeposit', viewsDeposit.eight, name='eightDeposit'),
    path('nineDeposit', viewsDeposit.nine, name='nineDeposit'),
    path('zeroDeposit', viewsDeposit.zero, name='zeroDeposit'),
    path('twoZeroDeposit', viewsDeposit.twoZero, name='twoZeroDeposit'),
    path('threeZeroDeposit', viewsDeposit.threeZero, name='threeZeroDeposit'),
    path('clearDeposit', viewsDeposit.clear, name='clearDeposit'),
    path('enterDeposit', viewsDeposit.enter, name='enterDeposit'),
    path('backDeposit', viewsDeposit.back, name='backDeposit')
    
]

