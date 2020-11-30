class Car: #  Класс машина
    def __init__(self, speed, denotes):
        self.speed = speed
        self.denotes = denotes
        print('Car with the maximum speed of', speed, denotes)
class Boat: #  Класс лодка
    def __init__(self, speed):
        self.speed = speed
        print('Boat with the maximum speed of', speed, 'knots')

q = int(input()) #  Вводим количество строк которое нужно проверить на данные
queries = [] #  Пустой список
for _ in range(q):
    args = input().split() #  разбиваем на части
    vehicle_type, params = args[0], args[1:] 
    if vehicle_type == "car": # если есть car в тексте
        max_speed, speed_unit = int(params[0]), params[1]
        vehicle = Car(max_speed, speed_unit)
    elif vehicle_type == "boat": #  если есть Boat в тексте
        max_speed = int(params[0])
        vehicle = Boat(max_speed)
    else:
        raise ValueError("invalid vehicle type") #  Не соответствует первым двум параметрам
