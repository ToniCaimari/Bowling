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
        if sum_turn in alert:
            sum_turn = Bowling.special_sign(sum_turn)
        if last_turn == '-':
            last_turn = Bowling.special_sign(last_turn)
        return 10 + int(sum_turn) - int(last_turn)

    @staticmethod
    def strike(game, contador):
        first_sum = game[contador+1]
        second_sum = game[contador+2]
        if first_sum in alert:
            first_sum = Bowling.special_sign(first_sum)
        if second_sum in alert:
            if second_sum == "/":
                first_sum = "0"
            second_sum = Bowling.special_sign(second_sum)
        return 10 + int(first_sum) + int(second_sum)

    @staticmethod
    def score(game):
        sum = 0
        contador = -1
        turn = (len(game)-game.count('X')) / 2 + game.count('X')
        for i in game:
            contador += 1
            if turn > 10:
                if game[contador-1] == '/' and len(game) == contador+1:
                    return sum
                if game[contador-1] == 'x' and len(game) == contador+2:
                    return sum
            if i not in alert:
                sum += int(i)
            if i == '-':
                pass
            if i == '/':
                sum += Bowling.spare(game, contador)
            if i == 'X':
                sum += Bowling.strike(game, contador)
        return sum


assert Bowling.score("5/5/5/5/5/5/5/5/5/5/5") == 150
