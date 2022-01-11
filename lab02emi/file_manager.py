class FileManager:
    def __init__(self, file_name):
        self.file_name = file_name

    def read_file(self):
        try:
            with open(self.file_name, "r", encoding="utf-8") as file_reader:
                for linia in file_reader:
                    print(linia, end="")
        except IOError:
            print("Wystapił wyjątek IOError")


    def update_file(self,text_data):  
        with open(self.file_name, "a") as a_file:
            a_file.write(text_data)


