class Demo:
    def show(self, *args):
        print("Arguments:", args)

d = Demo()
d.show()
d.show(10)
d.show(10, 20, 30)
#instead of using more arguments we can use this