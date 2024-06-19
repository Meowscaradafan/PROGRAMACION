import random


def coinflip():
    if random.choice[(1,2)] == "1":
        print("el apostador te dispara ")

    elif random.choice[(1,2)] == "2":
        print("el apostador se dispara ")




print("Bienvenido a buckshot roulette ")
usuario = input("Cual es tu nombre? ")

while True:
    print("1. Para empezar ")
    print("2. Para terminar ")
    Q1 = input("Que deseas hacer? (1-2)")

    if Q1 == "1":
        print("vamos a jugar, las reglas son simples. Tienes que ganarle al dealer que esta del otro lado, con una escopeta con numero de balas aleatoria y con cargas aleatorias. Hay dos tipos de balas, la real y la descargada. Se te asignara items con diferentes usos para ganarle al dealer. Buena suerte")
        def vidaR1():
            cantidad = [2,3,4]
            eleccion = random.choice(cantidad)
            return eleccion

        vida2players = vidaR1()
        vidajugador = vida2players
        vidaapostador = vida2players

        def balasR1():
            cantidadbalas = [3,4,5]
            eleccionronda = random.choice(cantidadbalas)
            return eleccionronda

        balasRo1 = balasR1()
        def cargasR1():
            if balasRo1 == 3:
               balasreales = random.choice([1,2])
            elif balasRo1 == 4:
                balasreales = random.choice([2])
            elif balasRo1 == 5:
                balasreales = random.choice([2,3])
                return balasreales


            balas = list(range(1, balasRo1 + 1))
            reales = random.sample(balas, balasreales)
            balascargador = [(bala, "real" if bala in reales else "falsa") for bala in balas]
            return balascargador

        balascargador = cargasR1()

          
        
        while True:

            print(f"Tu vida es {vidajugador} y la vida de el apostador es {vidaapostador}")

            print("\nPrimera ronda, la ronda acaba cuando alguno de los 2 pierdan toda su vida\n")

            bebida = "bebida"
            lupa = "lupa"
            cigarros = "cigarros"

            cajaitems = [bebida, lupa, cigarros,]
            inventariojugador = random.choice([bebida, lupa, cigarros])
            inventarioapostador = random.choice([bebida, lupa, cigarros])
     #ordenar balascargador en una lista para que el sistema sepa el
     # orden de las balas para que pueda determinar si es real o falsa
            cargadorsistema = [balascargador]
            disparosjugador = []
            disparosapostador = []
            disparosrondas = []
            apostadoreleccionitems = random.choice([inventarioapostador])

            def coinflipapostador():
              if random.choice[(1,2)] == "1":
                 print("el apostador te dispara ")
                 if cargadorsistema[0][1] == "real":
                     print("bala real")
                     vidajugador = vidajugador - 1
                 elif cargadorsistema[0][1] == "falsa":
                     print("bala falsa")
              elif random.choice[(1,2)] == "2":
                 print("el apostador se dispara ")
                 if cargadorsistema[0][1] == "real":
                     print("bala real")
                     vidaapostador = vidaapostador - 1
                 elif cargadorsistema[0][1] == "falsa":
                     print("bala falsa")

              return vidajugador, vidaapostador

            print(inventariojugador)
            print(inventarioapostador)
            print(cargadorsistema)

            print("se han cargado",balasRo1,"balas\n")
        
            decision1 = input("1) disparar al apostador\n2) dispararte\n3) mostrar items ")
            
            if decision1 == "1":
                disparosjugador.append(balascargador[0][0])
                if disparosjugador[0] == "real":
                    vidaapostador = vidaapostador - 1
                    print("bala real")
                    print("tu vida",vidajugador,"apostador",vidaapostador)
                elif disparosjugador[0] == "falsa":
                    print("bala falsa")
            if decision1 == "2":
                disparosjugador.append(balascargador[0][0])
                if disparosjugador[0] == "real":
                    vidajugador = vidajugador - 1
                    print("bala real")
                    print("tu vida",vidajugador,"apostador",vidaapostador)
                elif disparosjugador[0] == "falsa":
                    print("bala falsa")
                    
                    print("tu vida:",vidajugador,"\nvida apostador:",vidaapostador)
                    break

             


            