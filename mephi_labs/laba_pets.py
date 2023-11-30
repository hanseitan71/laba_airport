# Импортируем необходимые библиотеки
import json
import random

# Открываем JSON файл и загружаем данные
with open('cars_pet.json', 'r') as file:
    reader = json.load(file)

# Функция для ввода данных пользователя
def Inp(reader):
    try:
        flag = False
        flag2 = False
        n = int(input('Введите id человека: ')) - 1
        keys = list(reader[n].keys())
        if reader[n]['cars']:
            cars = reader[n]['cars']
            flag = True
        if reader[n]['pets']:
            pets = reader[n]['pets']
            flag2 = True
    except:
        print('Вы ошиблись')
        return Inp(reader)
    else:
        if flag and flag2:
            return keys, cars, pets, n
        elif flag and not flag2:
            return keys, cars, [], n
        elif not flag and flag2:
            return keys, [], pets, n
        else:
            return keys, [], [], n

# Получаем данные из функции ввода
key, cars, pets, n = Inp(reader)

# Определение класса Person (Человек)
class Person:
    def __init__(self, id, first_name, last_name, email, gender, cars, pets):
        # Инициализация атрибутов объекта
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.gender = gender
        self.cars = cars
        self.pets = pets

        # Устанавливаем начальное значение пробега для автомобилей
        if self.cars:
            for car in self.cars:
                car['mileage'] = 0

        # Устанавливаем начальный вес для питомцев
        if self.pets:
            for pet in self.pets:
                pet['weight'] = random.randint(10, 50)

    # Метод для вывода информации о питомцах
    def show_pets(self, lst):
        s = ''
        for i in lst:
            s += f"{i['breed']}, his name is {i['name']}, "
        return s[:-2]

    # Метод для вывода информации об автомобилях
    def show_cars(self, lst):
        s = ''
        for i in lst:
            s += f"{i['name']}, the model is {i['model']}, "
        return s[:-2]

    # Метод для формирования строки, описывающей объект Person
    def __str__(self):
        if self.cars is None and self.pets is None:
            return f'My name is {self.first_name} {self.last_name}'
        elif self.cars is None and self.pets is not None:
            return f'My name is {self.first_name} {self.last_name}, I have {self.show_pets(self.pets)}.'
        elif self.cars is not None and self.pets is None:
            return f'My name is {self.first_name} {self.last_name}, I have {self.show_cars(self.cars)}.'
        else:
            return f'My name is {self.first_name} {self.last_name}, I have {self.show_pets(self.pets)}, also I have {self.show_cars(self.cars)}.'

    # Метод для имитации путешествия на автомобиле
    def travell(self, goal, km):
        # Если есть автомобили и их количество больше 0
        if self.cars and len(self.cars) > 0:
            car = random.choice(self.cars)
            print(f'The goal of the travel is {goal}, the distance is {km} km, the car is {car["name"]}, the model is {car["model"]}')
            car_of_travel = Auto(car['name'], car['model'], car['mileage'])
            car_of_travel.mileage_auto(km)
            print(car_of_travel)
        else:
            print("The man go to his work, because he is a poor bitch without a car, and he can't to travell")

    # Метод для выгула питомца
    def go_for_a_walk(self):
        # Если есть питомцы и их количество больше 0
        if self.pets and len(self.pets) > 0:
            pet = random.choice(self.pets)
            print(f'I go for a walk with my {pet["breed"]} {pet["name"]}')
            pet_walk = Pet(pet['name'], pet['breed'], pet['weight'])
            pet_walk.weight_pet(random.randint(1, 3))
            print(pet_walk)
        else:
            print('None pets')

# Определение класса Auto (Автомобиль)
class Auto:
    def __init__(self, name, model, mileage):
        # Инициализация атрибутов объекта
        self.name = name
        self.model = model
        self.mileage = mileage

    # Метод для формирования строки, описывающей объект Auto
    def __str__(self):
        return f'The auto ({self.name} model - {self.model}) can drive, the mileage of the auto = {self.mileage} km'

    # Метод для имитации пробега автомобиля
    def mileage_auto(self, km):
        self.mileage += km

# Определение класса Pet (Питомец)
class Pet:
    def __init__(self, name, breed, weight):
        # Инициализация атрибутов объекта
        self.name = name
        self.breed = breed
        self.weight = weight

    # Метод для формирования строки, описывающей объект Pet
    def __str__(self):
        return f'The {self.breed} {self.name} is going for a walk, his weight = {self.weight}'

    # Метод для изменения веса питомца
    def weight_pet(self, weight):
        self.weight -= weight

# Пример данных
person = Person(reader[n]['id'], reader[n]['first_name'], reader[n]['last_name'], reader[n]['email'],\
                    reader[n]['gender'], cars, pets)

# Выводим информацию о человеке
print(person)

# Вызываем методы для имитации путешествия и выгула питомца
person.travell('sea', random.randint(1,500))
person.go_for_a_walk()


