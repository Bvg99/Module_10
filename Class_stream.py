import threading
import time


class Knight(threading.Thread):
    def __init__(self, name, skill, *args, **kwargs):
        super(Knight, self).__init__(*args, **kwargs)
        self.name = name
        self.skill = skill

    def run(self):
        enemies = 100
        days = 0
        print(f"{self.name}, на нас напали!")
        while enemies > 0:
            days += 1
            enemies -= self.skill
            print(f"{self.name}, сражается {days} день(дня), осталось {enemies} воинов.")
            time.sleep(1)
        print(f"{self.name} одержал победу спустя {days} дня(дней)!")


knight1 = Knight("Sir Lancelot", 10)
knight2 = Knight("Sir Galahad", 20)

knight1.start()
knight2.start()

knight1.join()
knight2.join()

print("Все битвы закончились!")