import datetime
class CalendarioModel:
    def hoy(self):
        d = datetime.date.today()
        return d.day, d.strftime("%A")
    def pesca(self):
        return [(x, "Alto" if x % 2 == 0 else "Bajo") for x in range(1, 31)]
