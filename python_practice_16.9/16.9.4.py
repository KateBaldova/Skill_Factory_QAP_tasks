# Команда проекта «Дом питомца» планирует большой корпоратив для своих клиентов. Вам необходимо
# написать программу, которая позволит составить список гостей. В класс «Клиент» добавьте метод, который
# будет возвращать информацию только об имени, фамилии и городе клиента.
#
# Затем создайте список, в который будут добавлены все клиенты, и выведете его в консоль.

class Client:
    def __init__(self, name, surname, city, balance):
        self.name = name
        self.surname = surname
        self.city = city
        self.balance = balance

    def __str__(self):
        return f'"{self.name} {self.surname}. {self.city}. Баланс: {self.balance} руб."'

    def client_list_for_corporate(self):
        return f'{self.name} {self.surname}, г. {self.city}'

client_1 = Client("Иван", "Петров", "Москва", 50)
client_2 = Client("Сергей", "Сидоров", "Санкт-Петербург", 150)

clients = [client_1, client_2]

for client in clients:
    print(client.client_list_for_corporate())