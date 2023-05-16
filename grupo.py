print("REDMI 12 PRO Almacenamiento-1TB, Almacenamiento-1TB,color-Rojo,PRECIO=1.700.000 opcion 1")
print("Realmi 11 Almacenamiento-250gb, color-Negro,azul,PRECIO=1.200.000 opcion 2")
celular=int(input("Escriba que celular le gusta mas "))
if celular == 1:
    info=[]
    tarjeta=[]
    y="REDMI 12 PRO Almacenamiento-1TB, Almacenamiento-1TB,color-Rojo,PRECIO=1.700.000 opcion 1"
    a=input('nombre')
    b=input('apellido')
    c=int(input("cedula"))
    d=input('direccion')
    e=int(input("telefono"))
    f=input('metodo de pago si es efectivo r si no tarjeta t')
    if f == r:
        info.append(a)
        info.append(b)
        info.append(c)
        info.append(d)
        info.append(e)
        info.append(f)
        info.append(y)
        print(info)
        
    elif f == t:
        dep=input("¿Que tipo de tarjeta tiene ahorros o credito?")
        if dep==credito:
            resul=int(input("¿A cuantas cuotas se ara el pago?"))
            valor= (1700000/resul)
            resul.apppend(valor)
            print(resul)
            print(info)
            
        elif dep==ahorros: 
          print(info)
    
elif compra == 2:

        if f == tarjeta:
            dep=input("¿Que tipo de tarjeta tiene ahorros o credito?")
        if dep==credito:
            resul=int(input("¿A cuantas cuotas se ara el pago?"))
            val= (1200000/resul)
            resul.apppend(val)
            print(resul)
            print(info)
            
        elif dep==ahorros: 
          print(info)
    
