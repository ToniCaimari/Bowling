alert = ['-', '/', 'X']


class Bowling:
    def __init__(self, game):
        self.game = game

    @staticmethod
    def special_sign(sign):
        if sign == 'X':
            return 10
        if sign == '/':
            return 10
        if sign == '-':
            return 0

    @staticmethod
    def spare(game, turn):
        sum_turn = game[turn+1]
        last_turn = game[turn-1]
        if last_turn == '-':
            last_turn = Bowling.special_sign(last_turn)
        return 10 - int(last_turn) + int(sum_turn)

    @staticmethod
    def strike(game, turn):
        multi_strike = 1
        first = 1
        second = 2
        first_sum = game[turn+first]
        second_sum = game[turn+second]
        while first_sum == 'X':
            if multi_strike != 3:
                multi_strike += 1
                first_sum = game[turn+first]
                second_sum = game[turn+second]
                first += 1
                second += 1
                if multi_strike == 3:
                    return 30
        if first_sum in alert:
            if first_sum == '-':
                first_sum = Bowling.special_sign(second_sum)
        if second_sum in alert:
            if second_sum == '/':
                first_sum = 0
                second_sum = Bowling.special_sign(second_sum)
            if second_sum == '-':
                second_sum = Bowling.special_sign(second_sum)
        return (10 * multi_strike) + int(first_sum) + int(second_sum)

    @staticmethod
    def score(game):
        sum = 0
        turn = 0
        for i in game:
            if i in alert:
                if i == 'X':
                    sum += Bowling.strike(game, turn)
                if i == '/':
                    sum += Bowling.spare(game, turn)
                if i == '-':
                    pass
                turn += 1
            else:
                sum += int(i)
                turn += 1
        return sum
