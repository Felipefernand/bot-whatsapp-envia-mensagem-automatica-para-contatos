import pywhatkit #bibliotecas
import keyboard
import time
from datetime import datetime

contatos = ['+55']  #numeros, para adicionar mais coloque 'numero','numero'

while len(contatos) >= 1:  #intervalo envio

    #mensagens enviadas
    pywhatkit.sendwhatmsg(contatos[0], 'Digite aqui a mensagem',datetime.now().hour, datetime.now().minute + 2)
    del contatos[0]
    time.sleep(60)
    keyboard.press_and_release('ctr + w')
    #não use o pc depois de compilar
