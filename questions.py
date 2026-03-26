import random

Diccpalabras = {
    "conceptos generales": ["programa", "funcion"],
    "lenguajes de programacion": ["python"],
    "estructuras": ["bucle", "variable"],
    "tipos de dato": ["cadena", "entero", "lista"]
}

print("¡Bienvenido al Ahorcado!")
print()

print("Categorias disponibles:")
for clave in Diccpalabras:
    print(f"- {clave}") 

eleccionDelUsuario = input("seleccioná una categoria: ").lower()
while eleccionDelUsuario not in Diccpalabras:
    print("Categoria invalida, proba de nuevo.")
    eleccionDelUsuario = input("Elegi una categoria: ").lower()

palabras_disponibles = random.sample(Diccpalabras[eleccionDelUsuario], len(Diccpalabras[eleccionDelUsuario]))



i=0
puntaje=0
seguir= True

while seguir:
    print ('nueva partida, puntaje actual: ',puntaje)
    guessed = []
    attempts = 6
    word = palabras_disponibles[i]
    i+=1
    while attempts > 0:
        progress = ""
        
        for letter in word:
            if letter in guessed:
                    progress += letter + " "
            else:
                    progress += "_ "

        print(progress)

        # Verificar si el jugador ya adivinó la palabra completa
        if "_" not in progress:
            print("¡Ganaste!")
            puntaje+=6
            print(f"Puntaje: {puntaje}")
            break

        print(f"Intentos restantes: {attempts}")
        print(f"Letras usadas: {', '.join(guessed)}")

        letter = input("Ingresá una letra: ")
        valido = len(letter) == 1 and (letter >= 'a' and letter <= 'z' )


        if not valido: 
            print("error, letra no valida")
        elif letter in guessed:
            print("Ya usaste esa letra.")
        elif letter in word:
            guessed.append(letter)
            print("¡Bien! Esa letra está en la palabra.")
        else:
            guessed.append(letter)
            attempts -= 1
            puntaje-=1
            print("Esa letra no está en la palabra.")

        print()

    else:
        print(f"¡Perdiste! La palabra era: {word}")
        puntaje=0
        print(f"Puntaje: {puntaje}")


    opcion = input("Presiona 1 para terminar el juego, otra tecla para seguir jugando ")
    seguir = opcion != "1" 