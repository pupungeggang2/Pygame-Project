import ast
import asset, UI, data, const, var

def save_init():
    try:
        f = open('Data/data_save.txt', 'r')
        var.save = ast.literal_eval(f.read())
        f.close()

    except:
        f = open('Data/data_save.txt', 'w')
        f.write(str(const.empty_save))
        f.close()
        f = open('Data/data_save.txt', 'r')
        var.save = ast.literal_eval(f.read())
        f.close()

def data_save():
    pass

def data_load():
    pass