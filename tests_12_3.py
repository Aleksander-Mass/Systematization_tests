import unittest

def freeze_control(func):
    def wrapper(self, *args, **kwargs):
        if self.is_frozen:
            self.skipTest("Тесты в этом кейсе заморожены")
        else:
            return func(self, *args, **kwargs)
    return wrapper


# Класс Runner и тесты RunnerTest с атрибутом is_frozen
class Runner:
    def __init__(self, name):
        self.name = name
        self.distance = 0

    def run(self):
        self.distance += 10

    def walk(self):
        self.distance += 5

    def __str__(self):
        return self.name


class RunnerTest(unittest.TestCase):
    is_frozen = False  # Тесты в этом классе выполняются

    @freeze_control
    def test_walk(self):
        runner = Runner("TestRunner")
        for _ in range(10):
            runner.walk()
        self.assertEqual(runner.distance, 50)

    @freeze_control
    def test_run(self):
        runner = Runner("TestRunner")
        for _ in range(10):
            runner.run()
        self.assertEqual(runner.distance, 100)

    @freeze_control
    def test_challenge(self):
        runner1 = Runner("Runner1")
        runner2 = Runner("Runner2")
        for _ in range(10):
            runner1.run()
            runner2.walk()
        self.assertNotEqual(runner1.distance, runner2.distance)


# Класс Tournament и тесты TournamentTest с атрибутом is_frozen
class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
            for participant in self.participants[:]:
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)
            self.participants.sort(key=lambda p: self.full_distance - p.distance, reverse=True)
        return finishers


class TournamentTest(unittest.TestCase):
    is_frozen = True  # Тесты в этом классе пропущены

    @freeze_control
    def test_race_usain_nik(self):
        runner_usain = Runner("Usain", speed=10)
        runner_nik = Runner("Nick", speed=3)
        tournament = Tournament(90, runner_usain, runner_nik)
        results = tournament.start()
        self.assertTrue(results[max(results)].name == "Nick")

    @freeze_control
    def test_race_andrei_nik(self):
        runner_andrei = Runner("Andrei", speed=9)
        runner_nik = Runner("Nick", speed=3)
        tournament = Tournament(90, runner_andrei, runner_nik)
        results = tournament.start()
        self.assertTrue(results[max(results)].name == "Nick")

    @freeze_control
    def test_race_usain_andrei_nik(self):
        runner_usain = Runner("Usain", speed=10)
        runner_andrei = Runner("Andrei", speed=9)
        runner_nik = Runner("Nick", speed=3)
        tournament = Tournament(90, runner_usain, runner_andrei, runner_nik)
        results = tournament.start()
        self.assertTrue(results[max(results)].name == "Nick")

###    Вывод на консоль:
"""
Ran 6 tests in 0.073s

OK (skipped=3)


Skipped: Тесты в этом кейсе заморожены

Skipped: Тесты в этом кейсе заморожены

Skipped: Тесты в этом кейсе заморожены
"""