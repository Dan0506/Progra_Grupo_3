#Variables globales
rutas=["Turrialba-San José", "Jaco por pista", "Concepción Abajo", "Turrialba Colectivo", "San José-Alajuela"]
precios=[500, 1000, 3000]
asientosts=[["1","2"],["3","4"],["5","6"],["7","8"],["9","10"]]
asientosj=[["1","2"],["3","4"],["5","6"],["7","8"],["9","10"]]
asientosc=[["1","2"],["3","4"],["5","6"],["7","8"],["9","10"]]
asientostc=[["1","2"],["3","4"],["5","6"],["7","8"],["9","10"]]
asientossa=[["1","2"],["3","4"],["5","6"],["7","8"],["9","10"]]
tiquetes=["Sencillo", "Diario", "Semanal"]
sel=""
ver=False
id=0
total = open("total.txt", "w")
total.close()

#Calcula cuantos asientos están disponibles
def contarAsientos(ruta):
    dis=0
    for i in range(0,len(ruta),1):
            for j in range(0,len(ruta[0]),1):
                if ruta[i][j]!="O":
                    dis+=1
    return dis

#Imprime los asientos de una ruta dada
def printAsientos(ruta):
    print("------------------------------------")    
    for i in range(0,len(ruta),1):
        print(ruta[i][0],ruta[i][1])
    print("------------------------------------")

#Adquiere una cantidad de asientos dada, de una ruta dada, los actualiza a no disponible y los guarda en una factura 
def adquirirAsientos (ruta):
    global id
    sub=0
    iva=0
    tot=0
    factura = open(f"factura{id}.txt", "w")
    factura.close()
    factura = open(f"factura{id}.txt", "a")
    factura.write(f"Ruta: {rutas[int(rutas1)-1]}\n")
    tomado=True
    global ver
    ver1=False
    print("Estos son los asientos disponibles")
    printAsientos(ruta)
    while not ver:
        try:
            sel1=int(input("Digite cuantos asientos desea comprar "))
            ver=True
        except:
            print("\nPor favor seleccione una opción válida\n")
            ver=False
    ver=False
    factura.write(f"Tiquetes x{sel1}\n\n")
    factura.write("*******************************\n\n")
    
    
    for k in range(0,sel1,1):
        while not ver:
            sel2=input("Digite el número del asiento que desea ")
            try:
                for i in range(0,len(ruta),1):
                    for j in range(0,len(ruta[0]),1):
                        if ruta[i][j]==sel2:
                            factura.write(f"Asiento {sel2}\n")
                            while not ver1:
                                tiq=input("\nDigite el número del tipo de tiquete que desea adquirir\n1- Sencillo - 500 colones\n2- Diario - 1000 colones\n3- Semanal - 3000 colones\n\n")
                                if tiq=="1":
                                    factura.write("Sencillo\n")
                                    factura.write("500 CRC\n\n")
                                    sub+=500
                                    ver1=True
                                elif tiq=="2":
                                    factura.write("Diario\n")
                                    factura.write("1000 CRC\n\n")
                                    sub+=1000
                                    ver1=True
                                elif tiq=="3":
                                    factura.write("Semanal\n")
                                    factura.write("3000 CRC\n\n")
                                    sub+=3000
                                    ver1=True
                                else:
                                    print("\nPor favor seleccione una opción válida")
                            ver1=False
                            ruta[i][j]="O"
                            tomado=False
                            ver=True
                if tomado:
                    print("\nAsiento no disponible")
                tomado=True
                print("")
            except:
                print("Por favor seleccione una opción válida\n")
        ver=False
        printAsientos(ruta)
    factura.write("*******************************\n\n")
    iva=sub*0.13
    tot=sub+iva
    
    factura.write(f"Subtotal {sub} CRC\n")
    factura.write(f"IVA - 13% {iva} CRC\n")
    factura.write(f"Total {tot} CRC")
    factura.close()
    id+=1
    total = open("total.txt", "a")
    total.write(str(tot)+"\n")
    total.close()

#Suma las ventas guardadas en un archivo de texto
def sumVentas():
    tv=0
    total = open("total.txt", "r")
    ventas=total.readlines()
    for i in ventas:
        tv+=float(i)
    print(tv)

#Menú principal
while sel!="5":
    sel=input("1. Ver Rutas\n2. Ver precios\n3. Adquirir tiquete(s)\n4. Consultar cantidad de espacios disponibles\n5. Salir\n\n")
    print("")
    if sel=="1":
        print("Estas son las rutas disponibles")
        print("------------------------------------")
        for i in rutas:
            print(i)
        print("------------------------------------")
    elif sel=="2":
        print("Estos son los precios disponibles")
        print("------------------------------------")
        for i in range(0,3,1):
            print (tiquetes[i])
            print (precios[i])
        print("------------------------------------")
    elif sel=="3":
        rutas1=input("Digite el número de la ruta en la que quiere viajar\n1- Turrialba-San José\n2- Jaco por pista\n3- Concepción Abajo\n4- Turrialba Colectivo\n5- San José-Alajuela\n\n")
        if rutas1 == "1":
            adquirirAsientos(asientosts)
        elif rutas1 == "2":
            adquirirAsientos(asientosj)
        elif rutas1 == "3":
            adquirirAsientos(asientosc)
        elif rutas1 == "4":
            adquirirAsientos(asientostc)
        elif rutas1 == "5":
            adquirirAsientos(asientossa)
        else:
            print("\nOpción no válida")
            
    elif sel=="4":
        ruta=input("Digite el número de la ruta que quiere revisar\n1- Turrialba-San José\n2- Jaco por pista\n3- Concepción Abajo\n4- Turrialba Colectivo\n5- San José-Alajuela\n\n")
        if ruta == "1":
            printAsientos(asientosts)
            print("Quedan" ,contarAsientos(asientosts), "asientos disponibles")
        elif ruta == "2":
            printAsientos(asientosj)
            print("Quedan" ,contarAsientos(asientosj), "asientos disponibles")
        elif ruta == "3":
            printAsientos(asientosc)
            print("Quedan" ,contarAsientos(asientosj), "asientos disponibles")
        elif ruta == "4":
            printAsientos(asientostc)
            print("Quedan" ,contarAsientos(asientosj), "asientos disponibles")
        elif ruta == "5":
            printAsientos(asientossa)
            print("Quedan" ,contarAsientos(asientosj), "asientos disponibles")
        else:
            print("\nPor favor seleccione una opción válida")
            
    elif sel=="5":
        print("Que tenga un buen día")
        
    elif sel=="6":
        print("Modo Administrador Desbloqueado\n")
        print("Suma de todas las ventas:")
        sumVentas()
    else:
        print("Selección no válida")
    input()


