def parse_name(data: str):
    data = '<' + data + '>'
    data = data.replace(' ', '><')
    return data


def get_name(data: str):
    my_str = ''
    for char in data:
        if not char == ' ':
            my_str += char
        else:
            return my_str
