
import json

class Simple:
    def __init__(self, x, y):
        # setattr(self, '_x', x)    
        # setattr(self, '_y', y)    
        self._x = x
        self._y = y

    # def __getattr__(self, attr):
    #     if attr in ('_x', '_y'):
    #         raise ValueError('Низззя')

    # def __setattr__(self, attr, value):
    #     if attr in ('_x', '_y'):
    #         raise ValueError('Низззя')
    #     else:
    #         setattr(self, attr, value)    

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @x.setter
    def x(self, x):
        print('Мы в функции setter.x')
        if isinstance(x, int):
            self._x = x
        else:
            raise ValueError('Допустимы только int')    

    @y.setter
    def y(self, y):
        print('Мы в функции setter.y')
        if isinstance(y, str):
            self._y = y
        else:
            raise ValueError('Допустимы только int')    



# s = Simple(13, 99)        
# print(s.__dict__)

# s.x = 37
# print(s.x)
# s.y = 'я строка'
# print(s.y)


class WorkerBuilder:
    def __init__(self, d):
        # self.name = list(d.keys())[0]
        # self.status = list(d.keys())[1]
        for key, data in d.items():
            setattr(self, key, data)

w = WorkerBuilder({"name":"Виктор", "status":"Director"})
print(w.__dict__)


# f = open('workers.json', encoding='utf-8')
# ls = json.loads(f.read(), encoding='utf-8')
# print(ls)

# __builtins__

class Wrapper:
    def __init__(self, obj):
        self.wrapped = obj

    def __getattr__(self, attr):
        print('Trace: ', attr)
        return getattr(self.wrapped, attr)

    def __str__(self):
        return repr(self.wrapped)    


x = Wrapper([1,2,3])        
x.append(17)

x.insert(0, 78)
x.pop()

print(x)
