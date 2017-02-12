
import time

def deco1(func):
    def decorated(*args, **kwargs):
        print('Сделал красиво')
        res = func(*args, **kwargs)
        return res
    return decorated    


def sleep(sec):
    def deco(func):
        def decorated(*args, **kwargs):
            time.sleep(sec)
            res = func(*args, **kwargs)
            return res
        return decorated  
    return deco      


class Sleep:
    def __init__(self, sec):
        self.sec = sec

    def __call__(self, func):
        def decorated(*args, **kwargs):
            print('я сплюююю....')
            time.sleep(self.sec)
            res = func(*args, **kwargs)
            return res
        return decorated


@sleep(2)
def f1:
    pass
    
@sleep(1)
def f1:
    pass

@sleep(13)
def f1:
    pass

@Sleep(1)
def my_summ(a, b):
    return a + b

print(my_summ(7, 8))

# my_summ = sleep(2)(my_summ)    