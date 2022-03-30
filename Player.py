class Player:
    def __init(self, name):
        self.name = name
        self.poso = 0
        self.total_time = 0
        self.m_o = 0
        self.daep = 0

    def __str__(self):
        return f"{self.name}, {self.poso}€, {self.total_time}sec, {self.m_o}sec/q, {self.daep}"
