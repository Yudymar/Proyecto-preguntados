# Bienvenidos al juego estilo preguntados de Yudy
# Las reglas son simples: 
# Dos jugadores elegirán 5 yudypreguntas al azar de categorías de su elección, cada pregunta tiene 4 opciones a escoger.
# El límite para repetir categorías es de 2 veces
# El jugador que más aciertos tenga gana
# El juego termina cuando ambos jugadores hayan respondido sus 5 preguntas
# ¡Comencemos!

import csv
import random

# Aqui estarán todas las funciones a utilizar
# -------------------------

def nombre_jugador():
    
    while True:
        score = 0
        score_1 = 0
        preguntas_respondidas = 0
        respuestas_usadas = []
        preguntas_respondidas_1 = 0
        categorias_elegidas = []
        categorias_elegidas_1 = []    
        cant_preguntas = 5

        # Definimos al primer jugador 
        jugador = input('Ingresa tu nombre por favor:\n')
        while jugador == "":
            print("No puedes ingresar un nombre vacío. Prueba otra vez.")
            jugador = input('Ingresa tu nombre por favor:\n')
        print("Bienvenido", jugador)
        
        while preguntas_respondidas < cant_preguntas:
            
            categoria = elige_categoria(categorias_elegidas)
            categorias_elegidas.append(categoria)
            preguntas = elegir_pregunta(categoria, respuestas_usadas)
            respuestas_usadas.append(preguntas[1])

            pregunta = preguntas[0]
            print(pregunta)
            respuestas = listar_respuestas(preguntas[1])
            for i in range(len(respuestas)):
                if i % 2 == 0:
                    print(respuestas[i], ":", respuestas[i+1])
            respuesta =str(input("Ingresa la letra de tu respuesta:\n"))
            
            
            while respuesta == "":
                print("No puedes ingresar una respuesta vacía. Prueba de nuevo.")
                respuesta = str(input("Ingresa la letra de tu respuesta:\n"))
            
            while respuesta not in ["a", "b", "c", "d"]:
                print("No puedes ingresar una respuesta que no sea a, b, c, d")
                respuesta = str(input("Ingresa la letra de tu respuesta:\n"))

            validate = repuesta_correcta(preguntas[1], respuesta)

            if validate == 1:            
                print("Respuesta correcta")            
                score = score + 1
                preguntas_respondidas = preguntas_respondidas + 1
            else:
                print("Respuesta incorrecta")
                preguntas_respondidas = preguntas_respondidas + 1
        
        ##==================
        print(jugador, "has respondido", preguntas_respondidas, "preguntas y has obtenido un puntaje de", score)
        if score == 5:
            print("¡Bien hecho, arrasaste!")
        elif score == 4:
            print("Casi lo tenías, en tu defensa creo que te tocaron las más difíciles.")
        elif score == 3:
            print("Nada mal, pero pudiste hacerlo mejor, solo digo.")
        elif score == 2:
            print("Esfuerzate un poco más la próxima vez.")
        elif score == 1:
            print("Ojalá el otro jugador sea igual de malo")
        elif score == 0:
            print("¡Vuelve al colegio!")
        ##==================

        # Definimos al segundo jugador
        jugador_1 = input('Ingresa tu nombre por favor:\n')
        
        while jugador_1 == "":
            print("No puedes ingresar un nombre vacio")
            jugador_1 = input('Ingresa tu nombre por favor:\n')
        print("Bienvenido", jugador_1)

        while preguntas_respondidas_1 < cant_preguntas:
                
                categoria = elige_categoria(categorias_elegidas_1)
                categorias_elegidas_1.append(categoria)
                preguntas = elegir_pregunta(categoria, respuestas_usadas)  
                respuestas_usadas.append(preguntas[1])     
        
                pregunta = preguntas[0]
                print(pregunta)
                respuestas_1 = listar_respuestas(preguntas[1])
                for i in range(len(respuestas_1)):
                    if i % 2 == 0:
                        print(respuestas_1[i], ":", respuestas_1[i+1])
                respuesta =str(input("Ingresa la letra de tu respuesta:\n"))
                # Validacion para que no se pueda ingresar una respuesta vacia
                
                while respuesta == "":
                    print("No puedes ingresar una respuesta vacía")
                    respuesta = str(input("Ingresa la letra de tu respuesta:\n"))
        
                # Validacion para que no se pueda ingresar una respuesta que no sea a, b, c, d
                while respuesta not in ["a", "b", "c", "d"]:
                    print("No puedes ingresar una respuesta que no sea a, b, c, d")
                    respuesta = str(input("Ingresa la letra de tu respuesta:\n"))

                validate = repuesta_correcta(preguntas[1], respuesta)

                if validate == 1:            
                    print("Respuesta correcta")            
                    score_1 = score_1 + 1
                    preguntas_respondidas_1 = preguntas_respondidas_1 + 1
                else:
                    preguntas_respondidas_1 = preguntas_respondidas_1 + 1
                    print("Respuesta incorrecta")
                    preguntas_respondidas = preguntas_respondidas + 1
        
                
        ##==========================
        print(jugador_1, "has respondido", preguntas_respondidas_1, "preguntas y has obtenido un puntaje de", score_1)
        if score_1 == 5:
            print("¡Bien hecho, arrasaste!")
        elif score_1 == 4:
            print("Casi lo tenías, en tu defensa creo que te tocaron las más difíciles.")
        elif score_1 == 3:
            print("Nada mal, pero pudiste hacerlo mejor, solo digo.")
        elif score_1 == 2:
            print("Esfuerzate un poco más la próxima vez.")
        elif score_1 == 1:
            print("Ojalá el otro jugador haya sido igual de malo")
        elif score_1 == 0:
            print("¡Vuelve al colegio!")
        ##==========================

        # Calculo de los resulados 
        if score > score_1:
            print("¡Felicidades", jugador, "has ganado, yo invito los tragos!")
        elif score < score_1:
            print("¡Felicidades", jugador_1, "has ganado, yo invito los tragos!")
        else:
            print("Resultado: empate.")

        # Inicar el juego de nuevo
        print("¿Quieren volver a jugar? (si/no)")
        volver_a_jugar = str(input("Ingresa tu respuesta, 's' para SI y 'n' para NO:\n"))
        while volver_a_jugar == "":
            print("No puedes ingresar una respuesta vacia")
            volver_a_jugar = str(input("Ingresa tu respuesta:\n"))
        while volver_a_jugar not in ["s", "n"]:
            print("No puedes ingresar una respuesta que no sea 's' o 'n'")
            volver_a_jugar = str(input("Ingresa tu respuesta:\n"))
        if volver_a_jugar == "s":
            print("Vamos a jugar de nuevo")
            continue
        else:
            print("Gracias por jugar")
            break

    return jugador, jugador_1, score, score_1
        
def lista_categorias():

    resultado = []
    # Seleccionar lista de categorias y retornarla
    with open ("Proyecto Preguntados - Lista de preguntas.csv", "r", newline ="") as csvfile:
        reader = csv.reader(csvfile)
        e = 0
        for row in reader:
            if e > 1:
                categoria = row[0].split(';')[2]
                # Eliminar repetidos de la lista de categorias
                if categoria not in resultado:
                    resultado.append(categoria)
            e = e + 1
        return resultado
            
def elige_categoria(cat_elegidas):
    categoria = lista_categorias()
    print("Elige una categoria:")
    for i in range(len(categoria)):
        if cat_elegidas.count(categoria[i]) < 2:
            print(i+1, ":", categoria[i])            

    # Validacion de que la categoria ingresada sea correcta
    while True:
        try:
            categoria_elegida = int(input("Ingresa el numero de la categoria:\n")) 
        except ValueError:
            print("Debes escribir un número válido. Por favor intenta otra vez:")
            continue

        if categoria_elegida > len(categoria):
            print("Esa categoría no existe. Ingresa un número válido por favor:")
            continue
        else:
            break
    
    categoria_elegida = int(categoria_elegida)
    print("Categoria elegida:", categoria[categoria_elegida-1])
    return categoria[categoria_elegida-1]

def elegir_pregunta(categoria, preguntas_elegidas):
    resultado = []
    # Seleccionar lista de preguntas y retornarla con el id de la pregunta
    with open ("Proyecto Preguntados - Lista de preguntas.csv", "r", newline ="") as csvfile:
        reader = csv.reader(csvfile)
        header = next(reader)
        for row in reader:
            # Eliminar repetidos de la lista de preguntas            
            if row[0].split(';')[2] == categoria and row[0].split(';')[0] not in preguntas_elegidas:
                resultado.append(row)

        pregunta = random.choice(resultado) 
        id_pregunta = pregunta[0].split(";")[0]        
        pregunta = pregunta[0].split(";")[3]
        result = [pregunta, id_pregunta]
        return result
        
def listar_respuestas(id_pregunta):
    resultado = []
    respuestas = []
    # Seleccionar lista de preguntas y retornarla con el id de la pregunta
    with open ("Proyecto Preguntados - Lista de preguntas.csv", "r", newline ="") as csvfile:
        reader = csv.reader(csvfile)
        e = 0
        for row in reader:
            if e > 1:
                if row[0].split(';')[0] == id_pregunta:
                    respuestas = row[0].split(';')[4:8]
                    # Iterar sobre las respuestas y agregarlas a la lista con indices de la A a la D
                    options = ["a", "b", "c", "d"]
                    for i in range(len(respuestas)):
                        resultado.append(options[i])
                        resultado.append(respuestas[i])
               
            e = e + 1
        return resultado

def repuesta_correcta(id_pregunta, respuesta):
    resultado = []
    # Seleccionar lista de preguntas y retornarla con el id de la pregunta
    with open ("Proyecto Preguntados - Lista de preguntas.csv", "r", newline ="") as csvfile:
        reader = csv.reader(csvfile)
        e = 0
        for row in reader:
            if e > 1:
                if row[0].split(';')[0] == id_pregunta:
                    resultado = row[0].split(';')[8]
                    if resultado == respuesta:
                        return 1
            e = e + 1
        return 0


 
# Aqui empieza el programa
# -------------------------

if __name__ == '__main__':    
    nombre_jugador()
