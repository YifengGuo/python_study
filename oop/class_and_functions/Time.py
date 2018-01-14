class MyTime(object):
    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second

    def __str__(self):
        return '%.2d:%.2d:%.2d' %(self.hour, self.minute, self.second)

def is_after(t1, t2):
    if t1.hour > t2.hour:
        return True
    elif t1.hour == t2.hour:
        if t1.minute > t2.minute:
            return True
        elif t1.minute == t2.minute:
            if t1.second > t2.second:
                return True
            else:
                return False
        else:
            return False
    else:
        return False

t1 = MyTime(8,59,30)
t2 = MyTime(9,30,30)

print is_after(t1, t2)