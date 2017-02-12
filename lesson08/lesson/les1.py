import json

class WorkerBuilder:
    def __init__(self):
        for key, data in d.items():
            setattr(self, key, data)


f = open("les1.json")
ls = json.loads(f.read(), ensure_ascii=False)
print(ls)
