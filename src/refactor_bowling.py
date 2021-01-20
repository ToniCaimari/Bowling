class Game_Score:

    def __init__(self, scorecard):
        self.scorecard = list(scorecard)
        self.points = 0
        self.alert = 0
        self.contador_tiradas = 0

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
        suma = 0
        first = Game_Score.values(self.scorecard[self.contador_tiradas+1])
        second = Game_Score.values(self.scorecard[self.contador_tiradas+2])
        if self.scorecard[self.contador_tiradas+2] == '/':
            first = 0
        suma += 10 + first + second
        return suma

    def spare_score(self):
        suma = 0
        previous = Game_Score.values(self.scorecard[self.contador_tiradas-1])
        subsequent = Game_Score.values(self.scorecard[self.contador_tiradas+1])
        suma += 10 - previous + subsequent

        return suma

    def tenth(self):
        suma = 0
        last = self.scorecard[self.contador_tiradas:]
        for i in last:
            if i.isdigit():
                suma += int(i)
            elif i == 'X':
                suma += 10
            elif i == '/':
                if i == self.scorecard[self.contador_tiradas+1]:
                    suma += 10 - Game_Score.values(
                        self.scorecard[self.contador_tiradas])
                else:
                    suma += 10 - Game_Score.values(
                        self.scorecard[self.contador_tiradas+1])
            elif i == '-':
                pass
        return suma

    def final_score(self):
        strike = 'X'
        spare = '/'
        empty = '-'
        for i in self.scorecard:
            if self.alert != 18:
                if i.isdigit():
                    self.points += Game_Score.values(i)
                    self.contador_tiradas += 1
                    self.alert += 1
                elif i == strike:
                    self.points += Game_Score.strike_score(self)
                    self.contador_tiradas += 1
                    self.alert += 2
                elif i == spare:
                    self.points += Game_Score.spare_score(self)
                    self.contador_tiradas += 1
                    self.alert += 1
                elif i == empty:
                    self.contador_tiradas += 1
                    self.alert += 1
            else:
                self.points += Game_Score.tenth(self)
                break

        return self.points
