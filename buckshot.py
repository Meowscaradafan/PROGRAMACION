import random    #para que funcionen los random.choice

def coinflipapostador():
    if random.choice([1,2]) == 1:
        print("el apostador te dispara")
    elif random.choice([1,2]) == 2:
        print("el apostador se dispara")    #este es el 50/50 de el apostador, si decide disparar al jugador o a el

def vidarandom():
    cantidad = [2,3,4]
    eleccion = random.choice(cantidad)
    return eleccion    #aqui definimos la vida de los jugadores

vida2jugadores = vidarandom()
vidajugador = vida2jugadores
vidaapostador = vida2jugadores #aqui le asignamos la vida a ambos jugadores

def balasrandom():
    cantidadbalas = [2,3,4,5]
    eleccionbalas = random.choice(cantidadbalas)
    return eleccionbalas  #aqui definimos la cantidad de balas

balaslistas = balasrandom() #definimos la cantidad de balas a una variable

def cargas():
    if balaslistas == 2:
        reales = 1
    elif balaslistas == 3:
        reales = random.choice([1,2])
    elif balaslistas == 4:
        reales = 2
    elif balaslistas == 5:
        reales = random.choice([2,3])
        return reales   #aqui definimos la cantidad de balas reales entre la cantidad de balas definida anteriormente
cargass = cargas()


def cargas2():
    balas = list(range(1, balaslistas + 1))
    cargadas = random.sample(balas, cargass)
    balascargador = [(bala, "real" if bala in cargadas else "falsa") for bala in balas]
    return balascargador  #aqui tendremos la lista de balas reales y falsas en orden de forma aleatoria en el sistema

balascargadorordenadas = cargas2()  #definimos la lista de balas en una variable
print(balascargadorordenadas)
#aca tendremos un codigo para los 3 items del juego

bebida = "bebida"  #la bebida hara que al que este de turno pueda descargar una bala de la escopeta
lupa = "lupa"  #la lupa hara que el que este de turno sepa que bala es la que biene en el siguiente disparo
cigarros = "cigarros"  #los cigarros hara que el que este de turno se regenere 1 de vida

cajaitems = [bebida, lupa, cigarros]  #esta es la lista de items

inventariojugador = random.choice([bebida, lupa, cigarros])
inventarioapostador = random.choice([bebida, lupa, cigarros]) #estas variables son para que al principio de la ronda se les asigne 1 item a cada jugador

apostadoreleccionitem = random.choice([inventarioapostador]) #aca el apostador escojera el item que tiene en su inventario para usarlo

disparosjugador = []
disparosapostador = [] #estas variables son para que se guarden los disparos de cada jugador en una lista

disparosronda = [] #esta variable hara que la ronda acabe cuando se llegue a la misma cantidad que la variable balaslistas

 #nota
 #hacer un codigo para que el apostador sepa siempre cual es la ultima bala en el cargador
 #hacer un while para la ronda y break para cuando esta acabe cuando la vida de uno de los jugadores lleguen a 0
 #hacer un codigo para que cada vez que se dispare uno mismo, ya sea el jugador o apostador, este pueda disparar otra carga





falsas = cargass - balaslistas


print("Bienvenido a buckshot roulette\n")

usuario = input("Ingresa tu nombre: ")

print(usuario, "tu vida es ",vidajugador,"y la del apostador", vidaapostador)

print("\nprimera ronda, hay", balaslistas,"balas en el cargador")
print("las balas son las siguientes: ",cargass,"cargadas",falsas,"descargadas" )

ronda1 = input("\n1)Disparar al apostador\n2)Dispararte\n3)Usar item")
if ronda1 == "1":
    print("Disparas al apostador\n")
    if balascargadorordenadas[0] == "1. real":
        vidaapostador = vidaapostador - 1
        print("bala real")
        
        


