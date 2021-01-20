class Game_Score:

    def __init__(self, scorecard):
        self.scorecard = list(scorecard)
        self.points = 0
        self.alert = 0
        self.throw_count = 0

    @staticmethod
    def values(element):
        if element == 'X':
            return 10
        if element == '/':
            return 10
        if element == '-':
            return 0
        else:
            return int(element)

    def strike_score(self):
        sum_count = 0
        first = Game_Score.values(self.scorecard[self.throw_count+1])
        second = Game_Score.values(self.scorecard[self.throw_count+2])
        if self.scorecard[self.throw_count+2] == '/':
            first = 0
        sum_count += 10 + first + second
        return sum_count

    def spare_score(self):
        sum_count = 0
        previous = Game_Score.values(self.scorecard[self.throw_count-1])
        subsequent = Game_Score.values(self.scorecard[self.throw_count+1])
        sum_count += 10 - previous + subsequent
        return sum_count

    def tenth(self):
        sum_count = 0
        last = self.scorecard[self.throw_count:]
        position = 0
        for i in last:
            if i.isdigit():
                sum_count += int(i)
                position += 1
            elif i == 'X':
                sum_count += 10
                position += 1
            elif i == '/':
                sum_count += 10 - Game_Score.values(
                    last[position-1])
            elif i == '-':
                position += 1
                pass
        return sum_count

    def final_score(self):
        strike = 'X'
        spare = '/'
        empty = '-'
        for i in self.scorecard:
            if self.alert != 18:
                if i.isdigit():
                    self.points += Game_Score.values(i)
                    self.throw_count += 1
                    self.alert += 1
                elif i == strike:
                    self.points += Game_Score.strike_score(self)
                    self.throw_count += 1
                    self.alert += 2
                elif i == spare:
                    self.points += Game_Score.spare_score(self)
                    self.throw_count += 1
                    self.alert += 1
                elif i == empty:
                    self.throw_count += 1
                    self.alert += 1
            else:
                self.points += Game_Score.tenth(self)
                break
        return self.points
