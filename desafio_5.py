def invertString(string):
    str_invertida =""
    for i in range(len(string) - 1, -1, -1):
        str_invertida += string[i]
    return str_invertida

string = input("Escreva uma palavra para invertermos as letras ")
string_invertida = invertString(string)
print("String invertida:", string_invertida)