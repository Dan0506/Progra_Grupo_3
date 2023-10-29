rutas=["Turrialba-San José", "Jaco por pista", "Concepción Abajo", "Turrialba Colectivo", "San José-Alajuela"]
precios=[500, 1000, 3000]
asientos=[["1","2"],["3","4"],["5","6"],["7","8"],["9","10"]]
tiquetes=["Sencillo", "Diario", "Semanal"]
sel=""
tomado=True
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
        print("Estos son los asientos disponibles")
        print("------------------------------------")    
        for i in range(0,len(asientos),1):
            print(asientos[i][0],asientos[i][1])
        print("------------------------------------")
        
        sel=input("Digite el número del asiento que desea ")
        for i in range(0,len(asientos),1):
            for j in range(0,len(asientos[0]),1):
                if asientos[i][j]==sel:
                    asientos[i][j]="O"
                    tomado=False
        if tomado:
            print("\nAsiento no disponible")
        tomado=True
        print("")
        print("------------------------------------")  
        for i in range(0,len(asientos),1):
            print(asientos[i][0],asientos[i][1])
        print("------------------------------------")  
    elif sel=="4":
        print("WIP")
    elif sel=="5":
        print("Que tenga un buen día")
    else:
        print("Selección no válida")
    input()


