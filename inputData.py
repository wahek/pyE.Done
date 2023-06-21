class InputData:

    @staticmethod
    def console_input():
        input_data = input('Введите Фамилия Имя Отчество номер телефона через пробел:\n')
        return input_data

    @staticmethod
    def check_number(my_str, i):
        number = my_str[i + 1:]
        try:
            num = int(number)
            return True
        except ValueError:
            print("Введён некорректный номер")
            return False

    @staticmethod
    def check_name(my_str: str, i):
        new_str = my_str[:i].replace(" ", "")
        if new_str.isalpha():
            return True
        else:
            print('В имени могут содержаться только буквы')
            return False

    @staticmethod
    def check_input(my_str):
        index = 0
        count = 0
        for i in range(len(my_str)):
            if my_str[i] == " ":
                count += 1
                if count == 3:
                    index = i
        if count == 3:
            if InputData.check_number(my_str, index) and InputData.check_name(my_str, index):
                return True
            else:
                return False
        else:
            raise KeyboardInterrupt('Формат данных неправильный\nПример: Maurin Ivan Pavlovich 89564872254')

