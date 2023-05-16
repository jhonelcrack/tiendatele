print("Bienvenido ")
print("Marcas: 2.Samsung")
Menu=int(input("A continuación seleccione la marca de dispositivos de las cuales desea ver el catalogo:"))


if Menu==2:
    
    print("Dispositivos")
    print("1.Samsung Galaxy S23 | 2.Samsung Galaxy A22")
    Seleccion=int(input("A continuación seleccione el dispositivo del que desea saber información:"))
   
    if Seleccion==1:
     
        print("Samsung Galaxy S23 | $ 3.412.947 COP")
        print("Caracteristicas: Pantalla Panel Dynamic AMOLED | Procesador Snapdragon 8 Gen 2 for Samsung | Ram 8 GB LPDDR5X | Almacenamiento 512 GB UFS 4.0 | Camara frontal 12 Mpx f/2.2 | Camara trasera Principal de 50 Mpx f/1.8 OISTelefoto de 10 Mpx f/2.4 OIS 3xGran angular de 12 Mpx f/2.2 ")
        Compra=int(input("Desea compralo 1.Si/2.No:"))
        
        if Compra==1:
        
            color=int(input("¿Que color de dispositivo desea? | 1.Negro | 2.Blanco:"))
            
            if color==1:
                print("Ha seleccionado un Samsung Galaxy S23 de color negro por un precio de $ 3.412.947 COP ")
                print("Datos")
                Nombre=input("Digite su nombre completo:")
                Documento=int(input("Digite el numero de documento:"))
                Telefono=int(input("Digite el numero de telefono:"))
                Direccion=input("Digite la direccion de recidencia:")
                Pago=int(input("Seleccione el metodo de pago: 1.Visa | 2.Mastercard | 3.Contra entrega:"))
                if Pago==1:
                    print("Compra exitosa")
                    print("Factura")
                    print("Nombre:",Nombre,"| Documento:",Documento,"| Telefono:",Telefono,"| Direccion:",Direccion,"| Metodo de pago:Visa | Valor pagado: $ 3.412.947 COP ")
                elif Pago==2:
                    print("Compra exitosa")
                    print("Factura")
                    print("Nombre:",Nombre,"| Documento:",Documento,"| Telefono:",Telefono,"| Direccion:",Direccion,"| Metodo de pago:Mastercard | Valor pagado: $ 3.412.947 COP ")
                elif Pago==3:
                    print("Compra exitosa")
                    print("Factura")
                    print("Nombre:",Nombre,"| Documento:",Documento,"| Telefono:",Telefono,"| Direccion:",Direccion,"| Metodo de pago:Contra entrega | Valor pagado: $ 3.412.947 COP ")
                else:
                    print("Valor ingresado no valido")
                
            elif color==2:
                print("Ha seleccionado un Samsung Galaxy S23 de color blanco por un precio de $ 3.412.947 COP ")
                print("Datos")
                Nombre=input("Digite su nombre completo:")
                Documento=int(input("Digite el numero de documento:"))
                Telefono=int(input("Digite el numero de telefono:"))
                Direccion=input("Digite la direccion de recidencia:")
                Pago=int(input("Seleccione el metodo de pago: 1.Visa | 2.Mastercard | 3.Contra entrega:"))
                if Pago==1:
                    print("Compra exitosa")
                    print("Factura")
                    print("Nombre:",Nombre,"| Documento:",Documento,"| Telefono:",Telefono,"| Direccion:",Direccion,"| Metodo de pago:Visa | Valor pagado: $ 3.412.947 COP ")
                elif Pago==2:
                    print("Compra exitosa")
                    print("Factura")
                    print("Nombre:",Nombre,"| Documento:",Documento,"| Telefono:",Telefono,"| Direccion:",Direccion,"| Metodo de pago:Mastercard | Valor pagado: $ 3.412.947 COP ")
                elif Pago==3:
                    print("Compra exitosa")
                    print("Factura")
                    print("Nombre:",Nombre,"| Documento:",Documento,"| Telefono:",Telefono,"| Direccion:",Direccion,"| Metodo de pago:Contra entrega | Valor pagado: $ 3.412.947 COP ")
                else:
                    print("Valor ingresado no valido")
            else:
                print("Valor ingresado no valido")
                
             
        else:
            
            print("Gracias")
            
    elif Seleccion==2:
       
        print("Samsung Galaxy A22 | $ 849.900 COP")
        print("Caracteristicas: Pantalla Super AMOLED de 6,4 pulgadas | Procesador MediaTek Helio G80 | Ram 4 GB | Alamacenamiento 128 GB | Camara frontal 13 megapíxeles, f/2.2 | Camara trasera Principal  48 megapíxeles 8 megapíxeles gran angular, f/2.22 megapíxeles profundidad, f/2.4 2 megapíxeles macro, f/2.4 " )
        Compra=int(input("Desea compralo 1.Si/2.No:"))
       
        if Compra==1:
       
            color=int(input("¿Que color de dispositivo desea? | 1.Blanco | 2.Azul:"))
            
            if color==1:
                print("Ha seleccionado un Samsung Galaxy A22 de color blanco por un precio de 849.900 COP ")
                print("Datos")
                Nombre=input("Digite su nombre completo:")
                Documento=int(input("Digite el numero de documento:"))
                Telefono=int(input("Digite el numero de telefono:"))
                Direccion=input("Digite la direccion de recidencia:")
                Pago=int(input("Seleccione el metodo de pago: 1.Visa | 2.Mastercard | 3.Contra entrega:"))
                if Pago==1:
                    print("Compra exitosa")
                    print("Factura")
                    print("Nombre:",Nombre,"| Documento:",Documento,"| Telefono:",Telefono,"| Direccion:",Direccion,"| Metodo de pago:Visa | Valor pagado: $ 849.900 COP ")
                elif Pago==2:
                    print("Compra exitosa")
                    print("Factura")
                    print("Nombre:",Nombre,"| Documento:",Documento,"| Telefono:",Telefono,"| Direccion:",Direccion,"| Metodo de pago:Mastercard | Valor pagado: $ 849.900 COP ")
                elif Pago==3:
                    print("Compra exitosa")
                    print("Factura")
                    print("Nombre:",Nombre,"| Documento:",Documento,"| Telefono:",Telefono,"| Direccion:",Direccion,"| Metodo de pago:Contra entrega | Valor pagado: $ 849.900 COP ")
                else:
                    print("Valor ingresado no valido")
            elif color==2:
                print("Ha seleccionado un Samsung Galaxy S23 de color azul por un precio de 849.900 COP ")
                print("Datos")
                Nombre=input("Digite su nombre completo:")
                Documento=int(input("Digite el numero de documento:"))
                Telefono=int(input("Digite el numero de telefono:"))
                Direccion=input("Digite la direccion de recidencia:")
                Pago=int(input("Seleccione el metodo de pago: 1.Visa | 2.Mastercard | 3.Contra entrega:"))
                if Pago==1:
                    print("Compra exitosa")
                    print("Factura")
                    print("Nombre:",Nombre,"| Documento:",Documento,"| Telefono:",Telefono,"| Direccion:",Direccion,"| Metodo de pago:Visa | Valor pagado: $ 849.900 COP ")
                elif Pago==2:
                    print("Compra exitosa")
                    print("Factura")
                    print("Nombre:",Nombre,"| Documento:",Documento,"| Telefono:",Telefono,"| Direccion:",Direccion,"| Metodo de pago:Mastercard | Valor pagado: $ 849.900 COP ")
                elif Pago==3:
                    print("Compra exitosa")
                    print("Factura")
                    print("Nombre:",Nombre,"| Documento:",Documento,"| Telefono:",Telefono,"| Direccion:",Direccion,"| Metodo de pago:Contra entrega | Valor pagado: $ 849.900 COP ")
                else:
                    print("Valor ingresado no valido")
            else:
                print("Valor ingresado no valido")
            
        else:
            
            print("Gracias")
    
    else:
        print("El valor ingresado no es valido")

else:
    print("El valor ingresado no es valido")