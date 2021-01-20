class Game_Score:

    def __init__(self, scorecard):
        self.scorecard = list(scorecard)
        self.points = 0  # puntos totales a devolver
        self.alert = 0  # localizador del último turno
        self.throw_count = 0  # localizador de cada lanzamiento
        self.strike = 'X'
        self.spare = '/'
        self.empty = '-'

    @staticmethod
    def values(element):  # siempre que queramos revisar el valor de un elemento llamaremos a esta función para evitar revisiones continuas
        if element == 'X':
            return 10
        if element == '/':
            return 10
        if element == '-':
            return 0
        else:
            return int(element)

    def strike_score(self):
        sum_count = 0  # valor acumulado que devuelve el strike
        # primer lanzamiento que se suma al strike
        first = Game_Score.values(self.scorecard[self.throw_count+1])
        # segundo lanzamiento que se suma al strike
        second = Game_Score.values(self.scorecard[self.throw_count+2])
        if self.scorecard[self.throw_count+2] == '/':
            first = 0  # si el segundo lanzamiento resulta ser un spare ignoramos el primer lanzamineto
        sum_count += 10 + first + second
        return sum_count

    def spare_score(self):
        sum_count = 0  # valor acumulado que devuelve el spare
        # restamos el valor del turno anterior que habiamos sumado previamente
        previous = Game_Score.values(self.scorecard[self.throw_count-1])
        # sumamos el lanzamiento siguiente al spare
        subsequent = Game_Score.values(self.scorecard[self.throw_count+1])
        # restamos el valor del turno anterior que habiamos sumado previamente para compensar la diferencia del spare
        sum_count += 10 - previous + subsequent
        return sum_count

    def tenth(self):
        sum_count = 0  # valor acumulado que devuelve el ultimo turno
        # separamos el último turno en una variable que usaremos más adelante junto con la variable 'position'
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
                    last[position-1])  # si encontramos un spare tomaremos en cuenta la posición relativa a la variable 'last' ara localizar el valor a restar a los 10 que sumamos por defecto
            elif i == '-':
                position += 1
                pass
        return sum_count

    def final_score(self):
        for i in self.scorecard:
            if self.alert != 18:  # confirmamos si estamos en el rango del último turno
                if i.isdigit():
                    self.points += Game_Score.values(i)
                    self.throw_count += 1
                    self.alert += 1
                elif i == self.strike:
                    self.points += Game_Score.strike_score(self)
                    self.throw_count += 1
                    self.alert += 2
                elif i == self.spare:
                    self.points += Game_Score.spare_score(self)
                    self.throw_count += 1
                    self.alert += 1
                elif i == self.empty:
                    self.throw_count += 1
                    self.alert += 1
            else:
                self.points += Game_Score.tenth(self)
                break
                # el break es necesario ya que tenth calculará el valor completo del último turno pero el for iniciado en esta función no habrá terminado aún
        return self.points
