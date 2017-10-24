def read_file(filename):
    file = open(filename, "r")
    data = file.read()
    file.close()
    return data

def write_file(data, filename):
    file = open(filename, "w")
    file.write(data)
    file.close()
