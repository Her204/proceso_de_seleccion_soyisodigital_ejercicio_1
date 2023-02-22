Productos = {1:'Pantalones', 2:'Camisas', 3:'Corbatas', 4:'Casacas'}
Precios = {1:200.00, 2:120.00, 3:50.00, 4:350.00}
Stock = {1:50, 2:45, 3:30, 4:15}

df = {a[0]:[a[1],a[2],a[3]] for a in zip(Stock.keys(),Productos.values(),Precios.values(),Stock.values())}

def print_with_table_style(df,num):
    print("="*num)
    print("Lista de Productos:")
    print("="*num)
    for k,v in df.items():
        sep_1 = len(f"{v[0]}{v[1]}")
        sep_1 = num-15-sep_1
        print(f"{k}   {v[0]}"+" "*sep_1+f"{v[1]}"+f"  {v[2]}")
    print("="*num)

while True:
    print_with_table_style(df,55)

    inpt = input("[1] Agregar, [2] Eliminar, [3] Actualizar, [4] Salir\nElija opcion: ")

    if "1" == inpt:
        productos = input("Nombre del producto: ")
        precios = input("Precio del producto: ")
        stock = input("Cantidad del producto en stock: ")
        df[len(df)+1] = [productos,precios,stock]

    elif "2" == inpt:
        print_with_table_style(df,55)
        index = input("Index del producto que se va borrar: ")
        df.pop(int(index))

    elif "3" == inpt:
        index = input("Index del producto que se va actualizar: ")
        if int(index) not in df.keys():
            print("El record que intentas actualizar no esta registrado utiliza la opcion 1")
            continue
        productos = input("Nombre del producto: ")
        precios = input("Precio del producto: ")
        stock = input("Cantidad del producto en stock: ")
        df[int(index)] = [productos,float(precios),int(stock)]

    elif "4" == inpt:
        break
    else:
        print(f"{inpt} no es una opcion valida intenta denuevo por favor: ")
        continue
