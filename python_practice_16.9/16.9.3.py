# В проекте «Дом питомца» добавим новую услугу — электронный кошелек. Необходимо создать класс «Клиент»,
# который будет содержать данные о клиентах и их финансовых операциях. О клиенте известна следующая
# информация: имя, фамилия, город, баланс.
# Далее сделайте вывод о клиентах в консоль в формате:
# «Иван Петров. Москва. Баланс: 50 руб.»

class Client:
    def __init__(self, name, surname, city, balance):
        self.name = name
        self.surname = surname
        self.city = city
        self.balance = balance

    def __str__(self):
        return f'"{self.name} {self.surname}. {self.city}. Баланс: {self.balance} руб."'

client_1 = Client("Иван", "Петров", "Москва", 50)

print(client_1)