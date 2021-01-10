class Bowling:
    jugada = ""

    jugadas_especiales = ["-", "/", "X"]

    def __init__(self, jugada):
        self.jugada = jugada

    @staticmethod
    def simbolo_a_numero(simbolo):
        if simbolo == "X":
            return "10"
        if simbolo == "/":
            return "10"
        if simbolo == "-":
            return "0"

    @staticmethod
    def spike(jugada, contador):
        tiro1 = (jugada[contador+1])

        tiro_anterior = (jugada[contador-1])
        if tiro1 in Bowling.jugadas_especiales:
            tiro1 = Bowling.simbolo_a_numero(tiro1)
        if tiro_anterior == "-":
            tiro_anterior = "0"
        return 10 + int(tiro1) - int(tiro_anterior)

    @staticmethod
    def strike(jugada, contador):
        tiro1 = (jugada[contador+1])
        tiro2 = (jugada[contador+2])
        if tiro1 in Bowling.jugadas_especiales:
            tiro1 = Bowling.simbolo_a_numero(tiro1)
        if tiro2 in Bowling.jugadas_especiales:
            if tiro2 == "/":
                tiro1 = "0"
            tiro2 = Bowling.simbolo_a_numero(tiro2)
        return 10 + int(tiro1) + int(tiro2)

    def suma_puntos(self):
        suma = 0
        contador = -1
        turnos = (len(self.jugada) - self.jugada.count("X")) / \
            2 + self.jugada.count("X")
        for i in self.jugada:
            contador += 1
            if turnos > 10:
                if self.jugada[contador-1] == "/" and len(self.jugada) == contador+1:
                    return suma
                if self.jugada[contador-1] == "X" and len(self.jugada) == contador+2:
                    return suma
            if i not in Bowling.jugadas_especiales:
                suma += int(i)
            elif i == "-":
                pass
            elif i == "/":
                suma += Bowling.spike(self.jugada, contador)
            elif i == "X":
                suma += Bowling.strike(self.jugada, contador)
        return suma


assert Bowling.suma_puntos("5/5/5/5/5/5/5/5/5/5/5") == 150
