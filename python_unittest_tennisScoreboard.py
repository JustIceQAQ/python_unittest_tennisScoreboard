import unittest


def tennisScoreboard(a, b):
    ScoreList = ('0', '15', '30', '40')
    if a == 3 and b == 3:
        return 'Deuce'
    elif a >= 3 and b >= 3:
        if a - b == 1:
            return 'A:Advantage'
        elif b - a == 1:
            return 'B:Advantage'
        elif a - b >= 2:
            return 'A:Winner'
        elif b - a >= 2:
            return 'B:Winner'
        elif a - b == 0:
            return 'Deuce'
    elif a >= 4:
        return 'A:Winner'
    elif b >= 4:
        return 'B:Winner'

    return f'{ScoreList[a]}-{ScoreList[b]}'


class AssertTest(unittest.TestCase):
    def test_0_0(self):
        self.assertEqual(tennisScoreboard(0, 0), '0-0')

    def test_1_0(self):
        self.assertEqual(tennisScoreboard(1, 0), '15-0')

    def test_2_0(self):
        self.assertEqual(tennisScoreboard(2, 0), '30-0')

    def test_3_0(self):
        self.assertEqual(tennisScoreboard(3, 0), '40-0')

    def test_4_0(self):
        self.assertEqual(tennisScoreboard(4, 0), 'A:Winner')

    def test_0_1(self):
        self.assertEqual(tennisScoreboard(0, 1), '0-15')

    def test_0_2(self):
        self.assertEqual(tennisScoreboard(0, 2), '0-30')

    def test_0_3(self):
        self.assertEqual(tennisScoreboard(0, 3), '0-40')

    def test_0_4(self):
        self.assertEqual(tennisScoreboard(0, 4), 'B:Winner')

    def test_1_1(self):
        self.assertEqual(tennisScoreboard(1, 1), '15-15')

    def test_2_2(self):
        self.assertEqual(tennisScoreboard(2, 2), '30-30')

    def test_3_3(self):
        self.assertEqual(tennisScoreboard(3, 3), 'Deuce')

    def test_5_3(self):
        self.assertEqual(tennisScoreboard(5, 3), 'A:Winner')

    def test_3_5(self):
        self.assertEqual(tennisScoreboard(3, 5), 'B:Winner')

    def test_4_3(self):
        self.assertEqual(tennisScoreboard(4, 3), 'A:Advantage')

    def test_3_4(self):
        self.assertEqual(tennisScoreboard(3, 4), 'B:Advantage')

    def test_4_4(self):
        self.assertEqual(tennisScoreboard(4, 4), 'Deuce')


if __name__ == '__main__':
    unittest.main()
