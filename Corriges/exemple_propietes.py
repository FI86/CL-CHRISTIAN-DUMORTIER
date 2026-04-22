class Temperature:
    def __init__(self, celsius):
        self.__celsius = celsius

    @property
    def celsius(self):
        return self.__celsius

    @celsius.setter
    def celsius(self, valeur):
        if valeur < -273.15:
            raise ValueError("Température doit être >= -273.15 °C")
        else:
            self.__celsius = valeur

    @property
    def fahrenheit(self):
        return self.__celsius * 9/5 + 32

    @fahrenheit.setter
    def fahrenheit(self, valeur):
        if valeur < -459.67:
            raise ValueError("Température doit être >= -459.67 °F")
        else:
            self.__celsius = (valeur - 32) * 5/9


def temp(temp: str, valeur: float) -> None:
    try:
        match temp.upper():
            case "F":
                t.fahrenheit = valeur
            case "C":
                t.celsius = valeur
            case _:
                print("La temperature doit etre en Celsius ou en Fahrenheit.")
    except ValueError as e:
        print(e)
    else:
        match temp.upper():
            case "F":
                print(t.fahrenheit)
            case "C":
                print(t.celsius)
        

if __name__ == "__main__":
    t = Temperature(25)

    print(t.celsius)
    print(t.fahrenheit)

    temp("f", 50)
    temp("c", -300)
