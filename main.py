from Controller import Controller
from View import View
from Model import Model



v = View()
m = Model()
c = Controller(v, m)
# Προς αφαίρεση 2 γραμμές, δοκιμή σύνδεσης View με Controller
print(c)
c.hello("main")




