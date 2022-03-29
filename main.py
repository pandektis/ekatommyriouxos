from Controller import Controller
from View import View
from Model import Model


def start():
    v = View()
    m = Model()
    c = Controller(v, m)



if __name__ == '__main__':
    start()


