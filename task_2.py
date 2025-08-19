class Tester:
    def __init__(self, name):  # добавляю self, исправлено присваивание
        self.name = name
        self.deadline = True  # сохраняю как атрибут экземпляра

    def work_hard(self, deadline=True):
        if deadline:  # использую переданный параметр deadline, а не self.deadline
            print(self.name, 'Что ж, ещё часок поработаю!')
        else:
            print(self.name, 'Можно отдыхать')


# Создаём экземпляры
tester_1 = Tester(name='tester_1')
tester_1.work_hard(deadline=False)  # 'tester_1 Можно отдыхать'

tester_2 = Tester(name='tester_2')
tester_2.work_hard(deadline=True)   # 'tester_2 Что ж, ещё часок поработаю!'