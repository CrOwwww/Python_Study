import threading
class A(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    def run(self):
        for i in range(0,10):
            print("I'm A")

threading1 = A()
threading1.start()
