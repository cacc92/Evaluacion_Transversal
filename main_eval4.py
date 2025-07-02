
# persona = {
#     "nombre" : "aqui va un nombre",
#     "tipo_entrada" : "tipo",
#     "codigo": "codigo"
# }

lista_ilumanados = []
lista_fortificados = []
stock_iluminados = 500
stock_fortificados = 500

def buscar_comprador(nombre, lista):
    for elemento in lista:
        if elemento["nombre"].upper() == nombre.upper():
            return True, elemento # Flujo termina
    return False, None

def ingresar_nombre(lista):
    while True:
        nombre = input("Ingrese el nombre del comprador: ")
        flag, usuario = buscar_comprador(nombre, lista)
        if flag: # Pregunto que el usuario exista
            print("‼️ Usuario existente.. ")
            print("Ingrese nuevamente el valor")
            continue
        print("✅ El nombre de usuario es válido")
        return nombre
def ingresar_tipo_entrada(tipos_entrada = []):
    while True:
        tipo = input(f"Ingrese el tipo de entrada solamente se permiten valores {tipos_entrada}: ").upper()
        if tipo in tipos_entrada:
            print("✅ El tipo de entrada es correcto")
            return tipo
    
        print("‼️ El tipo de entrada no es válido!! ") 
        continue

def ingresar_codigo(largo, cantidad_mayusculas, cantidad_numeros):
    while True:
        codigo = input("Ingresa el código: ")
        if " " in codigo:
            print("‼️ El código posee espacios en blanco. No es válido")
            continue
        if len(codigo) < largo:
            print("‼️ El código no posee la cantidad mínima de caracteres. No es válido")
            continue
        contador_mayusculas = 0
        contador_numeros = 0
        for caracter in codigo:
            if caracter in "QWERTYUIOPASDFGHJKLÑZXCVBNM":
                contador_mayusculas +=1
            if caracter in "1234567890":
                contador_numeros +=1
        if contador_numeros >= cantidad_numeros and contador_mayusculas >= cantidad_mayusculas:
            print("✅ El código esta correctamente ingresado")
            return codigo
        else:
            print("‼️ El código no posee la cantidad mínima mayúsculas o numeros. No es válido")
            continue

def comprar_entrada(lista, stock, tipos_entrada, largo, mayusculas, numeros):
    if stock > 0:
        comprador = {
            "nombre" : ingresar_nombre(lista),
            "tipo_entrada" : ingresar_tipo_entrada(tipos_entrada),
            "codigo": ingresar_codigo(largo, mayusculas, numeros)
        }
        lista.append(comprador)
        stock -= 1
        return lista, stock
    else:
        print("‼️ No se posee entradas disponibles para vender")
        return lista, stock

def mostrar_stock(stock_fortificados, stock_iluminados):
    print(f"El stock de fortiicados es: {stock_fortificados}")
    print(f"El stock de iluminados es: {stock_iluminados}")

while True:
    print("TOTEM AUTOSERVICIO CONCIERTOS ROCK AND CHILE")
    print("1.- Comprar entrada a 'los Fortificados'")
    print("2.- Comprar entrada a 'los Iluminados'")
    print("3.- Stock de entradas para ambos conciertos")
    print("4.- Salir.")

    try:
        opc = int(input("Ingrese una opción: "))
    except Exception as e:
        print("‼️ La opción ingresada no es válida")
        continue

    if opc == 1:
        lista_fortificados, stock_fortificados = comprar_entrada(
            lista=lista_fortificados,
            stock=stock_fortificados,
            tipos_entrada=["G","V"],
            largo=6,
            mayusculas=1,
            numeros=1
        )
        print(lista_fortificados)
    elif opc == 2:
        lista_ilumanados, stock_iluminados = comprar_entrada(
            lista=lista_ilumanados,
            stock=stock_iluminados,
            tipos_entrada=["CV","PAL"],
            largo=5,
            mayusculas=3,
            numeros=1
        )
    elif opc == 3:
        mostrar_stock(stock_fortificados, stock_iluminados)
    elif opc == 4:
        break
    else: 
        print("‼️ La opción ingresada no es válida")
tipo = ingresar_tipo_entrada(["G", "V"])
tipo = ingresar_tipo_entrada(["CV", "PAL"])