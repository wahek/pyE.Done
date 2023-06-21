def file_writing(file_name, data):
    data = data + "\n"
    try:
        with open(file_name+'.txt', "a") as f:
            f.write(data)
    except Exception:
        print('wrong')
