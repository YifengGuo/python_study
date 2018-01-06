import math


def eval_loop():
    while True:
        s = raw_input()
        if s == 'done':
            break
        print eval(s)
    print 'Done!'
eval_loop()
