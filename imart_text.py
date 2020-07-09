import unittest


def Score(first_player, second_player, first_name='William', second_name='Tom'):
    Score2str = ('Love', 'Fifteen', 'Thirty', 'Forty')

    if first_player == second_player:
        if first_player == 3:
            return 'Deuce'
        else:
            return '{} All'.format(Score2str[first_player])
    else:
        if first_player >= 3 and second_player >= 3:
            if abs(first_player - second_player) == 1:
                return '{} adv'.format(first_name) if first_player > second_player else '{} adv'.format(second_name)
            else:
                pass
        else:
            return '{} {}'.format(Score2str[first_player], Score2str[second_player])


class ATrst(unittest.TestCase):
    def test_0_0(self):
        return self.assertEqual(Score(0, 0), 'Love All')

    def test_1_0(self):
        return self.assertEqual(Score(1, 0), 'Fifteen Love')

    def test_2_0(self):
        return self.assertEqual(Score(2, 0), 'Thirty Love')

    def test_3_0(self):
        return self.assertEqual(Score(3, 0), 'Forty Love')

    def test_0_1(self):
        return self.assertEqual(Score(0, 1), 'Love Fifteen')

    def test_0_2(self):
        return self.assertEqual(Score(0, 2), 'Love Thirty')

    def test_1_1(self):
        return self.assertEqual(Score(1, 1), 'Fifteen All')

    def test_2_2(self):
        return self.assertEqual(Score(2, 2), 'Thirty All')

    def test_3_3(self):
        return self.assertEqual(Score(3, 3), 'Deuce')

    def test_4_3(self):
        return self.assertEqual(Score(4, 3), 'William adv')

    def test_3_4(self):
        return self.assertEqual(Score(3, 4), 'Tom adv')


if __name__ == '__main__':
    unittest.main()
