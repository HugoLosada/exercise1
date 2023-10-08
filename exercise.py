#Este pograma va a permitir convertir de pies a metros, de metros por segundo a millas por hora y de julios a calorias 
#Vamos a crear una opción para preguntarle al usuario cual de las tres opciones desea convertir para esto tenemos que utilizar el input
#Creamos la función iniciar programa donde utilizamos while true para que el programa siga iniciándose hasta que el usuario seleccione salir 
def iniciar_programa():
    while True:
#Creamos la variable opción para que el usuario elija una opción
        opcion = int(input("Bienvenido al programa de conversiones ;) \n 1-De pies a metros \n 2-De metros por segundo a millas por hora \n 3-De julios a calorias \n 4-Salir del programa \n Escoge una de las cuatro opciones: ")) # Utilizamos el \n para hcer saltos de linea
        
        if opcion == 4:
            print("Pues nada, tu te lo pierdes...!")
            break  # si la opción es 4 salimos del programa

        # Creamos el diccionario donde asignamos a cada función un número para que el usuario pueda seleccionar una de las opciones.
        diccionario = {1: pies_a_metros, 2: metros_segundo_a_millas_hora, 3: julios_a_calorias}

        # Utilizamos el try para llamar a la opción que el usuario seleccionó. El except lo utilizamos por si el usuario elige una opción que no está dentro del diccionario.
        try:
            diccionario[opcion]()
        except:
            print("No es muy difícil..., pon una opción de esas cuatro")

        otra_conversion()



#Creamos la función otra conversión para que el usuario no tenga que volver a iniciar el programa en el caso de qe quiera hacer otra conversión. 
def otra_conversion():
#Le damos al usuario dos opciones, hacer otra conversión o salir del programa
    opcion = input("¿Quieres realizar otra conversión? (Si/No): ")
    if opcion.lower() == 'no': #Ponemos opción.lower() para que aunque el usuario lo ponga en minúsculas sirva igual
        print("Muchas gracias por utilizar el programa, Hasta la próxima!")
        exit()  # Salir del programa si la respuesta es 'no'.


#Creamos la función para convertir de pies a metros
def pies_a_metros():
    print("-----------------------------")
#Solicitamos que el usuario ingrese la cantidad que desea convertir
    pies = int(input("Ingresa la cantidad de pies que deseas convertir: "))
#Ponemos la fórmula para hacer la conversión
    metros = pies * 0.3048
#Utilizamos print para mostrar la solución
    print(pies,"pies equivalen a",metros,"metros")

#Hacemos los mismos pasos con las dos funciones siguientes

def metros_segundo_a_millas_hora ():
    print("----------------")
    metros = int(input("Ingresa la cantidad de metros que deseas conertir: "))
    millas = metros * 0.44704
    print(metros,"metros por segundo equivalen a",millas,"millas por hora")

def julios_a_calorias():
    print("------------------")
    julios = int(input("Ingresa la cantidad de julios que quieres convertir: "))
    calorias = julios * 4.184
    print(julios,"julios equivalen a",calorias,"calorias")

#ponemos la función iniciar programa para poder iniciarlo 
iniciar_programa()








