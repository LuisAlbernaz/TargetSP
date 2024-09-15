def inverter_string(string):
    string_invertida = ""
    
    for i in range(len(string) - 1, -1, -1):
        string_invertida += string[i].lower()
    
    return string_invertida

string_usuario = input("Digite uma string para inverter: ")

resultado = inverter_string(string_usuario)
print(f"String invertida: {resultado}")
