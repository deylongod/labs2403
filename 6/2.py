class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def get_info(self):
        return f'Марка: {self.make} \nМодель: {self.model}'


v = Vehicle('Daewoo', 'Matiz')
print(v.get_info())


print()


class Car(Vehicle):
    def __init__(self, make, model, fuel_type):
        super().__init__(make, model)
        self.fuel_type = fuel_type

    def get_info(self):
        info = super().get_info()
        return f'{info} \nТип топлива: {self.fuel_type}'


c = Car('Lada', 'Oka', 'Плов')
print(c.get_info())
