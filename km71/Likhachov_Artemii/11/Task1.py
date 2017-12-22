#!/usr/bin/python

import os

a = None

def input_checking_X(c):
    try:
        if c.isdigit() and int(c) != 0:
            return True
        else:
            try:
                if float(c)!=0:
                    return True
                else:
                    return False
            except:
                return False
    except:
        pass
        return False

def test_input_checking_X():
    print("Testing input_checking_X()...", end="")
    assert(input_checking_X('5') == True)
    assert(input_checking_X('0') == False)
    assert(input_checking_X(None) == False)
    assert(input_checking_X('3.2') == True)
    assert(input_checking_X('a') == False)
    print("Passed!")

def input_checking_I(b):
    try:
        if b.isdigit() and int(b)>=1:
            return True
        else:
            return False
    except:
        pass
        return False

def test_input_checking_I():
    print("Testing input_checking_I()...", end="")
    assert(input_checking_I('5') == True)
    assert(input_checking_I('0') == False)
    assert(input_checking_I(None) == False)
    assert(input_checking_I('1') == True)
    assert(input_checking_I('3.2') == False)
    assert(input_checking_I('-3.2') == False)
    assert(input_checking_I('a') == False)
    print("Passed!")

def correct_answer(k):
    if k in ('y', 'n'):
        return True
    return False

def test_correct_answer():
    print("Testing correct_answer()...", end="")
    assert(correct_answer(5) == False)
    assert(correct_answer(None) == False)
    assert(correct_answer(3.2) == False)
    assert(correct_answer('y') == True)
    assert(correct_answer('n') == True)
    assert(correct_answer('a') == False)
    print("Passed!")

def restart(q):
    if q == 'y':
        while not correct_answer(a):
            clr = input('\nWould you like to clear the shell? (y/n)\nInput correctly your answer!\n')
            if correct_answer(clr):
                break
            continue
        if clr == 'y':
            os.system('cls')
            return True
        if clr == 'n':
            print('')
            return True
    if q == 'n':  
        print('Atremii Likhachov KM-71')
        return False
'''
def test_restart():
    print("Testing restart()...", end="")
    assert(restart(None) == False)
    assert(restart('y') == False)
    assert(restart('y') == True)
    assert(restart('n') == True)
    assert(restart('n') == False)
    print("Passed!")
'''
def program():
    while not restart(a):
        print('Task 16. Sum of some different numbers')
        while not input_checking_X(a):
            X = input('Input term: ')
            if input_checking_X(X):
                while not input_checking_I(a):
                    N = input('Input last index number: ')
                    if input_checking_I(N):
                        try:
                            SUM = 0
                            for i in range(1, int(N)+1):
                                SUM+=pow(float(X),i)
                            print('Your answer: ', int(SUM))
                            break
                        except:
                            pass 
                            print('Your answer: ', int(SUM))
                            break
                        break
                    else:
                        print('Invalid data. Try again.')
                    continue
                break
            else:
                 print('Invalid data. Try again.')
            continue
        while not correct_answer(a):
            ans = input('\nWould you like to restart the program? (y/n)\nInput correctly your answer!\n')
            if correct_answer(ans):
                break
            continue
        if restart(ans):
            continue
        break



test_input_checking_X()
test_input_checking_I()
test_correct_answer()
program()

