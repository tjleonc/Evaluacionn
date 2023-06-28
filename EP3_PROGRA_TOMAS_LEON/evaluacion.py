import os
os.system("cls")

vectorCodigo = []
vectorNombre = []
vectorCategoria = []
vectorPrecio = []
vectorStock = []

menu = '''
        Menu
1. Registrar producto
2. Buscar producto
3. Listar producto
4. Salir

'''


def Registrar():
    while True:
        try:
            #Permite ingresar los datos de un producto, incluyendo: código numérico de 6 dígitos
            #verificar que el código numérico tenga exactamente 6 dígitos
            cod = input("Ingrese codigo: ")
            if len(cod) != 6 or not cod.isdigit():
                print("El codigo debe contener exactamente 6 digitos numericos")
            else:
                vectorCodigo.append(cod)
                break
        except:
            print("Ha ocurrido una excepcion en codigo.")
    while True:
        try:
            #el nombre del producto tenga entre 2 y 50 caracteres
            nom = input("Ingrese nombre: ")
            if len(nom) > 1 and len(nom) < 51 and nom.isalpha():
                vectorNombre.append(nom)
                break
            else:
                print("Por favor ingrese nombre entre 2 a 50 caracteres.")
        except:
            print("Ha ocurrido una excepcion en nombre.")
    while True:
        try:
            cat = input("Ingrese categoria (Paquete o Sobre): ") #categoria: Sobre o Paquete. REVISAR MAYUSCULAS
            if not cat == 'Paquete' or cat == 'Sobre':
                print("Ha ingresado una categoria erronea")
            else:
                vectorCategoria.append(cat)
                break
        except:
            print("Ha ocurrido excepcion en categoria.")
    while True:
        try:
            precio = int(input("Ingrese precio del producto: "))
            if precio > 0:
                vectorPrecio.append(precio)
                break
            else: 
                print("El precio debe ser mayor a 0.")
        except:
            print("Ha ocurrido una excepcion en precio.")
    while True:
        try:
            stock = int(input("Ingresar stock producto:"))
            if stock > 0:
                vectorStock.append(stock)
                break
            else:
                print("El stock debe ser mayor a 0.")
        except:
            print("Ha ocurrido una excepcion en stock")

def buscar():
    buscar = (input("Ingrese codigo a buscar: "))
    for i in range(len(vectorNombre)):
        if buscar == vectorCodigo[i]:
            print("Codigo               Nombre              Categoria               Precio              stock")
            print(f"{vectorCodigo[i]} {vectorNombre[i]} {vectorCategoria[i] } {vectorPrecio[i]} {vectorStock[i]}")

def listar():
    print("Productos disponibles en venta: ")
    print("Codigo Nombre Precio Stock Stock_Bajo")
    lowstock = 0
    for i in range(len(vectorCodigo)):
        if vectorStock[i] < 5:
            stock = "Si"
            lowstock = lowstock + 1
    else:
        stock = "No"
    print(f"{i+1} {vectorCodigo[i]} {vectorNombre[i]} {vectorCategoria[i] } {vectorPrecio[i]} {vectorStock[i]} {stock}")
    print("-----------------------------------------------------------------------------------------------------------")

while True:
    print(menu)
    try:
        opc = int(input("Ingrese opcion [1-4]: "))
        if opc == 4:
            break
        elif opc == 1:
            Registrar()
        elif opc == 2:
            buscar()
        elif opc == 3:
            listar()
    except:
        print("Ha ocurrido una excepcion en menu.")