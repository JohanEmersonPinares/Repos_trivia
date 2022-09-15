import random
import time
#Damos la bienvenida a nuestra trivia relatado en base a una obra llamada metamorfosis
BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
RESET = '\033[39m'
print(RED+"Sea bien recibido ante la trivia de obras literarias"+RESET)
time.sleep(1)
print(RED+
    "\nEvaluaremos tu nivel de conocimiento de obras y que tan preparado estas en estos libros bien conocidos"+RESET
)

time.sleep(2)
#Tenemos que dar las instrucciones de juego para poder jugar
#APLICAMOS UPPER PARA QUE EL NOMBRE ESTE EN TODO MAYUSCULA
puntaje = 0
iniciar_trivia = True  # Iniciamos la variable en True
intentos = 0  # variable que almacenará el número de veces que el usuario intenta nuestra trivia.

# Lo primero es mostrar en pantalla el texto de bienvenida para quien juegue tu trivia


while iniciar_trivia == True: #  Mientras iniciar_trivia sea True, repite:
  intentos += 1
  puntaje = 0

 
  nombre = input(MAGENTA+"\n Ingrese su nombre:"+RESET).upper()
  time.sleep(1)
  edad = input(GREEN+"\n Ingrese su edad:"+RESET).upper()
  suerte=random.randint(0,13)
  suertenota=random.randint(0,4)

  print(CYAN+"\n Bienvenido estimado"+RESET, nombre)
  time.sleep(1)
  print(CYAN+"\n Su numero de la suerte es:"+RESET, suerte)
  time.sleep(1)
  for numero_carga in range(3,0,-1):
    print(numero_carga)
    time.sleep(1)

  print(
    GREEN+"\n Marque la respuesta correcta", nombre,
    "con la letra asignada de cada respuesta y luego presione 'ENTER' para saber si es correcto o no"+RESET
)
  time.sleep(1)
  print("SI REPUESTA INCORRECTA SE DESCONTARA UN VALOR ALEATORIO DE PUNTOS")
  puntaje=0
  print("\n","USTED INICIA CON",suertenota,"PUNTOS  GRACIAS A SU NUMERO DE SUERTE")
  for numero_carga in range(3,0,-1):
    print(numero_carga)
    time.sleep(1)
#PREGUNTA1
  a = RED+"Mario Vargas Llosa"+RESET
  b = RED+"Franz Kaftka"+RESET
  c = RED+"Jose Maria Arguedas"+RESET
  d = RED+"Truman Capote"+RESET

  print(BLUE+"\n PREGUNTA 1"+RESET)
  print("¿Quien escribio la obra LA CIUDAD Y LOS PERROS?")
  print("a)", a)
  print("b)", b)
  print("c)", c)
  print("d)", d)

  respuesta1 = input("\n Inserte su respuesta:")
#VALIDACION DE RESPUESTAS EN RANGO DE A B C D
  while respuesta1 not in ("a", "b", "c", "d"):
      respuesta1 = input(
        "Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")
#CONDICIONAL DE LA RESPUESTA CORRECTA  
  if respuesta1 == "a":
      puntaje =puntaje+suertenota+7
      print("\n",nombre, "su respuesta es correcta")
  
  else:
      puntaje =suertenota+puntaje-2
      print("\n",nombre, "su respuesta es incorrecta")

  time.sleep(2)
  
#PREGUNTA2
  a = CYAN+"Miguel Cervantes"+RESET
  b = CYAN+"Isabel Allende"+RESET
  c = CYAN+"German Melwille"+RESET
  d = CYAN+"Leonardo Da Vinci"+RESET

  print(BLUE+"\n PREGUNTA 2"+RESET)
  print("¿Quien escribio la obra LA ULTIMA CENA?")
  print("a)", a)
  print("b)", b)
  print("c)", c)
  print("d)", d)

  respuesta2 = input("\n Inserte su respuesta:")

#VALIDACION DE RESPUESTAS EN RANGO DE AB C D
  while respuesta2 not in ("a", "b", "c", "d","x"):
      respuesta2 = input(
        "Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")
  if respuesta2 == "a":
      puntaje -= 2
      print("\n",nombre,"es incorrecto" ,"el escribio DON QUIJOTE DE LA MANCHA")
  elif respuesta2=="b":
    puntaje -= 2
    print("\n",nombre,"es incorrecto" , "ella escribio LA CASA DE LOS ESPIRITUS")
  elif respuesta2=="c":
    puntaje -= 2
    print("\n",nombre,"es incorrecto" , "el escribio MOVI DICK")
  elif respuesta2=="x":
    puntaje += 2
    print("\n",nombre,"es una respuesta secreta" , "has ganado 2 puntos a tu calificacion final")
  else:
    puntaje += 6.6
    print("\n","¡MUY BIEN!",nombre, "su respuesta es correcta")

  time.sleep(2)
#PREGUNTA3
  a = YELLOW+"2022"+RESET
  b = YELLOW+"2000"+RESET
  c = YELLOW+"1498"+RESET
  d = YELLOW+"1999"+RESET
  print(BLUE+"\n PREGUNTA 3"+RESET)
  print("¿Cuando se escribio LA ULTIMA CENA?")
  print("a)", a)
  print("b)", b)
  print("c)", c)
  print("d)", d)
  respuesta3 = input("\n Inserte su respuesta:")
#VALIDACION DE RESPUESTAS N RANGO A B C D
  while respuesta3 not in ("a", "b", "c", "d","x"):
      respuesta3 = input(
        "Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")
  if respuesta3 == "a":
    puntaje -= 2
    print("\n",nombre,"es incorrecto" ,"es un año muy cercano")
  elif respuesta3=="b":
    puntaje -= 2
    print("\n",nombre,"es incorrecto" , "son muchos años de diferencia")
  elif respuesta3=="d":
    puntaje -= 2
    print("\n",nombre,"es incorrecto" , "hay un rango de mas años ")
  elif respuesta3=="x":
    puntaje += 2
    print("\n",nombre,"es una respuesta secreta" , "has ganado 2 puntos a tu calificacion final")
  else:
    puntaje += 6.6
    print("\n","¡MUY BIEN!",nombre, "su respuesta es correcta")
  time.sleep(2)
#PREGUNTA BONUS
  a = GREEN+"2018"+RESET
  b = GREEN+"2017"+RESET
  c = GREEN+"2014"+RESET
  d = GREEN+"2016"+RESET
  print(YELLOW+"\n PREGUNTA 4"+RESET)
  print("ACIERTA LA RESPUESTA GANA O PIERDES TODO")
  print("¿CUANDO PERU PARTICIPO EN SU ULTIMO MUNDIAL")
  print("a)", a)
  print("b)", b)
  print("c)", c)
  print("d)", d)
  respuesta4 = input("\n Inserte su respuesta:")
#VALIDACION DE RESPUESTAS N RANGO A B C D
  while respuesta3 not in ("a", "b", "c", "d"):
     respuesta2 = input(
        "Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")
  if respuesta4 == "b":
     puntaje = puntaje/2
     print("\n",nombre,"es incorrecto" ,"es un año muy cercano")
  elif respuesta4=="c":
    puntaje = puntaje/3
    print("\n",nombre,"es incorrecto" , "son muchos años de diferencia")
  elif respuesta4=="d":
    puntaje = puntaje-5
    print("\n",nombre,"es incorrecto" , "hay un rango de mas años ")
  elif respuesta4=="x":
    puntaje += 3
    print("\n",nombre,"es una respuesta secreta" , "has ganado 3 puntos a tu calificacion final")
  else:
    puntaje += 6.6
    print(MAGENTA+"\n","¡MUY BIEN!",nombre, "AHORA SUME SUS PUNTOS"+RESET)
 
  print(MAGENTA+"\n Hasta otra oportunidad"+RESET, nombre)
  print(GREEN+"Usted tiene ",puntaje,"de nota final"+RESET)
 

  print("\n¿Deseas intentar la trivia nuevamente?")
  repetir_trivia = input("Ingresa 'si' para repetir, o cualquier tecla para finalizar: ").lower()

  if repetir_trivia != "si":  # != significa "distinto"
   print("\nEspero {nombre} que lo hayas pasado bien, hasta pronto!")
   iniciar_trivia = False  # Cambiamos el valor de iniciar_trivia a False para evitar que se repita.