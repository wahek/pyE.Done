import FileWork
import Parser
import inputData
import sys


try:
    input_data = inputData.InputData.console_input()
    valid = inputData.InputData.check_input(input_data)
except KeyboardInterrupt as e:
    print(e)
    print('Попробуйте снова')
    sys.exit()

if valid:
    parse_string = Parser.parse_name(input_data)
    file_name = Parser.get_name(input_data)
    FileWork.file_writing(file_name, parse_string)


