                  import json



def mostrarjson():
    with open ("Movistar.json","r") as file:
        return json.load(file)

def crearjson():
    with open ("Movistar.json","w") as file:
        return json.dump(file) 



def crear_usuario():
    mifile = mostrarjson()
    for usuario in mifile:
        for mifile in usuario:
            nombre_usuario = input("imgresa un nombre de usuariso: ")
            password = input("ingresa tu contraseña: ")    
            tip = input("ingresa el tipo de documentos: ")
            iD = int(input("ingresa tu numero de identificacion: "))
            nom = input("ingres tu nobre completo: ")
            ape = input("ingresa tu apelldio completo: ")
            dire = input("ingresa tu direccion: ")
            tel = int(input("ingresa tu telefono de contacto: "))
    
    Nusuario ["usuarios"]={
                            "npmbre_usuario":nombre_usuario,
                            "pasword":password,
                            "tipo":tip,
                            "iD":iD,
                            "nombre":nom,
                            "apellido":ape,
                            "direccion":dire,
                            "telefono":tel
                            }
    
    Nusuario = crearjson()


def menu_registro():
    print("""                                    
 ---------------------------------------
|                                       |
|            ¡Registrate!               | 
|                                       |
 --------------------------------------- 
        ( ͡° ͜ʖ ͡°) (.1)- 👨 -regist-.
        ( ͡° ͜ʖ ͡°) (.2)- 🙋 -Salir al menu usuario-.         
""")


x = True
while True:
    print("""                                    
    ---------------------------------------
    |                                       |
    |             ¡BIEBENIDO!               | 
    |                                       |
    ---------------------------------------          
    """)
    print(""" 
    ( ͡° ͜ʖ ͡°) (.1)- 👨 -registrar-.
    ( ͡° ͜ʖ ͡°) (.2)- 👨 -iniciar-.      
    ( ͡° ͜ʖ ͡°) (.3)- 🙋 -Salir-.   
    """)
    op = input("")

    if op == "1":
        menu_registro()
        o=input("")
        if o == "1":
            crear_usuario()
        elif o == "2":
            x=True



    elif op == "2":
        x = input()
        if x == 1:
            input("ingresa tu ")

    elif op == "3":
        x == False        
