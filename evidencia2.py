import datetime
import pandas as pd
import csv
import os
folio = 0
datos = []
suma_venta = []
_folio = []
_descripcion = []
_cantidad = []
_precio = []
_fechaprocesada = []
while True:
    print()
    print("-------Menú-------")
    print("[1]. Registrar venta")
    print("[2]. Consultar venta")
    print("[3]. Consultar venta por fecha")
    print("[4]. Salir")
    opcion = int(input("Opcion: "))
    if opcion ==  1:
        while True:
            folio = folio +1
            descripcion = input("Ingresa el articulo: ")
            cantidad = int(input("Ingresa la cantidad del artículo: "))
            precio = float(input("Ingresa el precio: "))
            fecha = input("Fecha de compra (dd/mm/aa): ")
            fechaprocesada = datetime.datetime.strptime(fecha, "%d/%m/%Y").date()
            subtotal = cantidad * precio
            _folio.append(folio)
            _descripcion.append(descripcion)
            _cantidad.append(cantidad)
            _precio.append(precio)
            _fechaprocesada.append(fechaprocesada)
            suma_venta.append(subtotal)
            diccionario = {"articulo":_descripcion, "cantidad": _cantidad, "precio":_precio, "fecha":_fechaprocesada}
            respuesta = int(input("\n ¿Deseas capturar otro registro? \n(1-Si / 0-No): "))
            if respuesta == 0:
                total = sum(suma_venta)
                print("El total de la venta es: ",total)
                resultado = pd.DataFrame(diccionario, index = _folio)
                path = "ventas.csv"
                resultado.to_csv(path, index=True ,mode="a", header=not os.path.isfile(path))
                break
    elif opcion == 2:
        consulta = pd.read_csv("ventas.csv", index_col=0)
        valor=int(input("Qué número de folio quieres consultar?: "))
        print(consulta.loc[valor])
        
    elif opcion == 3:
        consulta = pd.read_csv("ventas.csv", index_col=0)
        fecha_venta=input("Qué fecha de venta quieres consultar? (aa/mm/dd): ")
        print(consulta.loc[consulta["fecha"]== fecha_venta])
    elif opcion == 4:
        print("Muchas gracias, saliendo...")
        break
    else:
        print("Opción incorrecta, elige un número válido")
        


    
    
    
    
    
    
    
    
    
    