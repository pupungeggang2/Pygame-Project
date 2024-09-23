import ast
import const, var

def data_save():
    f = open('Save/save.txt', 'w')
    f.write(str(var.save))
    f.close()

def data_load():
    f = open('Save/save.txt', 'r')
    var.save = ast.literal_eval(f.read())
    f.close()