
class Mull:
    def __init__(self, x):
        self.x = x

    def __call__(self, y):
        return y * self.x

mull5 = Mull(5)            
print(mull5(13))