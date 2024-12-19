class RedactorFile:
    def __init__(self, name_file):
        self.name_file = name_file
        self.db = self.file_data()

    def file_data(self):
        db = []
        try:
            with open(self.name_file, "r", encoding="utf-8") as file:
                for i in file:
                    line = i.strip().split(' - ')
                    db.append(line)
                return db
        except FileNotFoundError:
            return []
    
    def saving_file(self):
        with open(self.name_file, 'w', encoding='utf-8') as file:
            for product, price in self.db:
                file.write(f"{product} - {price}\n")
    def showing_file(self):
        print("Имя - цена")
        for item in self.db:
            print(f"{item[0]} - {item[1]}\n")
        
    def add_product(self, product, price):
        self.db.append([product, price])
        self.saving_file()
        print(f"Добавлен: {product} - {price}")

    def update_product(self, product, price):
        for item in self.db:
            if item[0] == product:
                item[1] = price
                self.saving_file()
                print(f"Обновлен: {product} - {price}")
                return
        print(f"Продукт по имени {product} не найден!")

    def delete_item(self, product):
        new_db = []
        for item in self.db:
            if item[0] != product:
                new_db.append(item)
        self.db = new_db
        self.saving_file()
        print(f"Удалено: {product}")

    def total_sum(self):
        cnt = 0
        for item in self.db:
            cnt += int(item[1])
        print(f"Общая сумма: {cnt}")    
    
while True:
    name_file = input("Напишите имя файла которого хотите отредактировать: ")
    object = RedactorFile(name_file)
    function = input("Меню:\n1)Посмотреть\n2)Добавить\n3)Изменить\n4)Удалить\n5)Сумма\n6)Выход\nВыберите действия которые вы хотите сделать: ").lower()
    if function == "посмотреть":
        object.showing_file()
    elif function == "добавить":
        object.add_product(input("Имя продукта: "), input("Цена: "))
    elif function == "изменить":
        object.update_product(input("Имя продукта: "), input("Новая цена: "))
    elif function == "удалить":
        object.delete_item(input("Имя продукта: "))
    elif function == "сумма":
        object.total_sum()
    elif function == "выход":
        break
    else:
        print("Неправильно вели команду или имя файла")
