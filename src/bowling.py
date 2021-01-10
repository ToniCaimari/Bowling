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
    def spare(game, throw):
        sum_turn = game[throw+1]
        last_turn = game[throw-1]
        if sum_turn in alert:
            sum_turn = Bowling.special_sign(sum_turn)
        if last_turn in alert:
            last_turn = Bowling.special_sign(last_turn)
        return 10 + int(sum_turn) - int(last_turn)

    @staticmethod
    def strike(game, throw):
        multi_strike = 0
        first = 1
        second = 2
        first_sum = game[throw-1+first]
        second_sum = game[throw-1+second]
        while first_sum == 'X':
            if multi_strike != 3:
                multi_strike += 1
                first_sum = game[throw+first]
                try:
                    second_sum = game[throw+second]
                except:
                    continue

                first += 1
                second += 1
                if multi_strike == 3:
                    return 30
            if multi_strike == 3:
                return 30
        if first_sum in alert:
            # solo puede ser '-' (valor=0) o 'X' (acumulado ya en multi_strike)
            if second_sum not in alert:
                first_sum = second_sum
            if second_sum in alert:
                first_sum = Bowling.special_sign(second_sum)
        else:
            if multi_strike > 1:
                return (10*multi_strike)+int(first_sum)

        if second_sum in alert:
            if second_sum == '/':
                first_sum = 0
                second_sum = Bowling.special_sign(second_sum)
            else:
                second_sum = Bowling.special_sign(second_sum)
        return (10 * multi_strike) + int(first_sum) + int(second_sum)

    @staticmethod
    def turns(game):
        element = 0
        start = 0
        end = 2
        alert = False
        turn_list = []
        count = 0
        for i in game:
            if i != 'X':
                count += 1
                if count > 20:
                    alert = True
            else:
                count += 2
                if count > 20:
                    alert = True
                    break
        for i in game:
            if alert == False:
                while count > 0:
                    if i != 'X':
                        count -= 2
                        turn_list.append(game[start:end])
                        start += 2
                        end += 2
                        element += 2
                        try:
                            i = game[element]
                        except:
                            continue

                    else:
                        count -= 2
                        turn_list.append(game[start])
                        start += 1
                        end += 1
                        element += 1
                        i = game[element]

            if alert == True:
                while count > 4:
                    if i != 'X':
                        count -= 2
                        turn_list.append(game[start:end])
                        start += 2
                        end += 2
                        element += 2
                        try:
                            i = game[element]
                        except:
                            continue
                    else:
                        count -= 2
                        turn_list.append(game[element])
                        start += 1
                        end += 1
                        element += 1
                        i = game[element]
                else:
                    turn_list.append(game[-3:])
                    break
        return turn_list

    @staticmethod
    def score(game):
        turn_list = Bowling.turns(game)
        sum = 0
        turn = 0
        throw = 0
        for i in turn_list:
            turn += 1
            if turn < 10:
                for x in i:
                    if x in alert:
                        if x == 'X':
                            sum += Bowling.strike(game, throw)
                            throw += 1

                        if x == '/':
                            sum += Bowling.spare(game, throw)
                            throw += 1

                        if x == '-':
                            throw += 1
                    else:
                        sum += int(x)
                        throw += 1
            else:
                special_sum = 0
                final_group = [x for x in i]
                for i in final_group:
                    if i in alert:
                        if i == 'X':
                            special_sum += Bowling.special_sign(i)

                        if i == '/':
                            if i == final_group[1]:
                                special_sum += Bowling.special_sign(
                                    i)-special_sum
                            if i != final_group[1]:
                                special_sum += Bowling.special_sign(
                                    i)-int(final_group[1])
                        if i == '-':
                            pass
                    else:
                        special_sum += int(i)
                sum += special_sum

        return sum
