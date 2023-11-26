rutas=["Turrialba-San José", "Jaco por pista", "Concepción Abajo", "Turrialba Colectivo", "San José-Alajuela"]
precios=[500, 1000, 3000]
asientosts=[["1","2"],["3","4"],["5","6"],["7","8"],["9","10"]]
asientosj=[["1","2"],["3","4"],["5","6"],["7","8"],["9","10"]]
asientosc=[["1","2"],["3","4"],["5","6"],["7","8"],["9","10"]]
asientostc=[["1","2"],["3","4"],["5","6"],["7","8"],["9","10"]]
asientossa=[["1","2"],["3","4"],["5","6"],["7","8"],["9","10"]]
tiquetes=["Sencillo", "Diario", "Semanal"]
sel=""


def contarAsientos(ruta):
    dis=0
    for i in range(0,len(ruta),1):
            for j in range(0,len(ruta[0]),1):
                if ruta[i][j]!="O":
                    dis+=1
    return dis

def printAsientos(ruta):
    print("------------------------------------")    
    for i in range(0,len(ruta),1):
        print(ruta[i][0],ruta[i][1])
    print("------------------------------------")
    
def adquirirAsientos (ruta):
    tomado=True
    ver=False
    ver1=False
    print("Estos son los asientos disponibles")
    printAsientos(ruta)
    sel1=int(input("Digite cuantos asientos desea comprar "))
    for k in range(0,sel1,1):
        while not ver:
            sel2=input("Digite el número del asiento que desea ")
            for i in range(0,len(ruta),1):
                for j in range(0,len(ruta[0]),1):
                    if ruta[i][j]==sel2:
                        while not ver1:
                            tiq=input("Digite el número del tipo de tiquete que desea adquirir\n1- Sencillo - 500 colones\n2- Diario - 1000 colones\n3- Semanal - 3000 colones\n")
                            if tiq=="1":
                                print("Muy bien")
                                ver1=True
                            elif tiq=="2":
                                print("Muy bien")
                                ver1=True
                            elif tiq=="3":
                                print("Muy bien")
                                ver1=True
                            else:
                                print("Muy mal")
                        ver1=False
                        ruta[i][j]="O"
                        tomado=False
                        ver=True
            if tomado:
                print("\nAsiento no disponible")
            tomado=True
            print("")
        ver=False
        printAsientos(ruta) 
    


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
        ruta=input("Digite el número de la ruta en la que quiere viajar\n1- Turrialba-San José\n2- Jaco por pista\n3- Concepción Abajo\n4- Turrialba Colectivo\n5- San José-Alajuela\n")
        if ruta == "1":
            adquirirAsientos(asientosts)
        elif ruta == "2":
            adquirirAsientos(asientosj)
        elif ruta == "3":
            adquirirAsientos(asientosc)
        elif ruta == "4":
            adquirirAsientos(asientostc)
        elif ruta == "5":
            adquirirAsientos(asientossa)
            
    elif sel=="4":
        ruta=input("Digite el número de la ruta que quiere revisar\n1- Turrialba-San José\n2- Jaco por pista\n3- Concepción Abajo\n4- Turrialba Colectivo\n5- San José-Alajuela\n")
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
        
    elif sel=="5":
        print("Que tenga un buen día")
    else:
        print("Selección no válida")
    input()


