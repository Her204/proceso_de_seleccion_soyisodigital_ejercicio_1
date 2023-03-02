Productos = {1:'Pantalones', 2:'Camisas', 3:'Corbatas', 4:'Casacas'}
Precios = {1:200.00, 2:120.00, 3:50.00, 4:350.00}
Stock = {1:50, 2:45, 3:30, 4:15}

# primero separo el array de index del diccionario Stock y utilizo zip para que adhiera 
# los valores fila por fila permitiendome generar un nuevo diccionario que tenga un solo index
# para los tres campos
df = {a[0]:[a[1],a[2],a[3]] for a in zip(Stock.keys(),Productos.values(),Precios.values(),Stock.values())}


# utilizo este funcion para darle el estilo usado en el archivo de configuracion
def print_with_table_style(df,num):
    print("="*num)
    print("Lista de Productos:")
    print("="*num)
    for k,v in df.items():
        sep_1 = len(f"{v[0]}{v[1]}")
        sep_1 = num-15-sep_1
        print(f"{k}   {v[0]}"+" "*sep_1+f"{v[1]}"+f"  {v[2]}")
    print("="*num)


class Programa:
    def __init__(self,df):
        self.df = df
        self.msg = ""

    def insertar(self):
        productos = input("Nombre del producto: ")
        precios = float(input("Precio del producto: "))
        stock = int(input("Cantidad del producto en stock: "))
        if precios <0 or stock <0: 
            self.msg = "El precio y el stock no pueden ser negativos prueba denuevo"
            raise "error"
        self.df[len(df)+1] = [productos,precios,stock]

    def eliminar(self):
        print_with_table_style(self.df,55)
        index = input("Index del producto que se va borrar: ")
        if not index in self.df.keys():
            self.msg = "El index que intentas eliminar no existe en la tabla"
            raise "error"
        self.df.pop(int(index))
        
    def actualizar(self):
        index = input("Index del producto que se va actualizar: ")
        if int(index) not in self.df.keys():
            self.msg = "El record que intentas actualizar no esta registrado intenta denuevo"
            raise "error"
        productos = input("Nombre del producto: ")
        precios = float(input("Precio del producto: "))
        stock = int(input("Cantidad del producto en stock: "))
        if not precios>=0 or not stock >=0:
            self.msg = "El precio y el stock no pueden ser negativos prueba denuevo"
            raise "error"
        self.df[int(index)] = [productos,float(precios),int(stock)]

    def correr(self):
        while True:
            print_with_table_style(self.df,55)
            inpt = input("[1] Agregar, [2] Eliminar, [3] Actualizar, [4] Salir\nElija opcion: ")
            if "1" == inpt:
                try: self.insertar()
                except:
                    print(self.msg)
                    continue
                    
            elif "2" == inpt:
                try: self.eliminar()
                except:
                    print(self.msg)
                    continue
            elif "3" == inpt:
                try: self.actualizar()
                except:
                    print(self.msg)
                    continue
            elif "4" == inpt:
                break
            else:
                print(f"{inpt} no es una opcion valida intenta denuevo por favor: ")
                continue

if __name__ == "__main__":
    Programa(df).correr()
    
