class Player:
    def __init__(self, name):
        self.name = name
        self.poso = 0
        self.num_questions = 0
        self.total_time = 0
        self.m_o = 0
        self.daep = 0

    def __str__(self):
        return f"{self.name}, {self.poso}€, {self.total_time}sec, {self.m_o}sec/q, {self.daep}"

    def calc_mo(self):
        try:
            self.m_o = self.total_time / self.num_questions
        except ZeroDivisionError as Z:
            self.m_o = 0
