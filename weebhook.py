import time
import datetime
import requests
import os
print("Bienvendio a WEBHOOKS ATACKER")
hora = datetime.datetime.now()
print(hora)  
print("github: NEXXITO")
KEY = "MEXIR"
CLAVE = input("iNTRODUCE LA KEY [MEXIR] PARA VERIFICAR QUE NO ERES UN ROBOT : ")

if KEY == CLAVE:
    
    print("VERIFICACION COMPLETADA")
    time.sleep(2)
    os.system("cls")

    


else:
    print("La clave es incorrecta")
    time.sleep(2)
    os.system("cls")
    exit()


print("Ataca a una webhook(DC)")
try:
   WEEBHOOK = input("Introduce URL  de la webhook:  ")
   link = input("Introduce el link que quieres spamear:  ")


   requests.post(WEEBHOOK , json={"content": link})
except:
    print("Algo no ha ido bien")
    exit()





