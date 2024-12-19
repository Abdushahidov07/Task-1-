class RedactorFile:
    def __int__(self, name_file):
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
            for product, price  in self.db:
                file.write(f"{product} - {price}\n")
     