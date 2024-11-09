###     Часть 1. TestSuit.
# 1. Создайте модуль suite_12_3.py для описания объекта TestSuite. Укажите на него переменной с произвольным названием.

import unittest
from tests_12_3 import RunnerTest, TournamentTest

# 2. Добавьте тесты RunnerTest и TournamentTest в этот TestSuit.
# Создание TestSuite, добавление тестов из RunnerTest и TournamentTest
test_suite = unittest.TestSuite()
test_suite.addTests(unittest.TestLoader().loadTestsFromTestCase(RunnerTest))
test_suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TournamentTest))

# 3. Создайте объект класса TextTestRunner, с аргументом verbosity=2.
# Запуск TestSuite с использованием TextTestRunner
runner = unittest.TextTestRunner(verbosity=2)
runner.run(test_suite)

### Вывод на консоль:
"""
test_challenge (tests_12_3.RunnerTest.test_challenge) ... ok
test_run (tests_12_3.RunnerTest.test_run) ... ok
test_walk (tests_12_3.RunnerTest.test_walk) ... ok
test_race_andrei_nik (tests_12_3.TournamentTest.test_race_andrei_nik) ... skipped 'Тесты в этом кейсе заморожены'
test_race_usain_andrei_nik (tests_12_3.TournamentTest.test_race_usain_andrei_nik) ... skipped 'Тесты в этом кейсе заморожены'
test_race_usain_nik (tests_12_3.TournamentTest.test_race_usain_nik) ... skipped 'Тесты в этом кейсе заморожены'

----------------------------------------------------------------------
Ran 6 tests in 0.000s

OK (skipped=3)
"""