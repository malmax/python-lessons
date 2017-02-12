
import sys

class BadNumber(Exception):
    def __init__(self, x):
        super().__init__(self)
        self.x = x

    def __str__(self):
        return 'We have a problem! {}'.format(self.x)    


x = 10
try:
    f = open('test')
    for line in f:
        try:
            y = int(line)
            if y == 13:
                raise BadNumber(y)
        except BadNumber as bn:
            print(bn)      
        except ValueError:
            print('Проблемное число')
            sys.exit(13)  
        else:
            try:    
                print(x, y, x / y)
            except ZeroDivisionError as e:
                print(e)
        finally:
            print('Вот это даааа...') 
            
except SystemExit:
    print('Досвидос')
except FileNotFoundError:
    print('Файл не существует')    



# for i in [1, 4, 5, 11, 7, 8]:
#     if i > 0:
#         print(i)
#     else:
#         break        
# else:
#     print('Цикл завершился')        


