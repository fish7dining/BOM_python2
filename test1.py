

class b:
    def __do__(self, ans):
        ans.pop()

class a:
    def __init__(self):
        self.ans = []

    def add(self, x):
        self.ans.append(x)

    def delete(self):
        print self.ans
        tt = b()
        tt.__do__(self.ans)
        print self.ans


tt = a()
tt.add(1)
tt.add(2)
tt.add(3)
tt.delete()


