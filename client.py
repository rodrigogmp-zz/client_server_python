#!/usr/bin/env python

import socket
import time
import os


#tcp_ip = '18.204.102.146'
#tcp_ip = '127.0.0.1'
tcp_port = 7502

s = socket.socket(socket.AF_INET,
				socket.SOCK_STREAM)
s.connect((tcp_ip, tcp_port))

def download():
	data = s.recv(1024)
	print (data.decode())
	tamanho_txt = float(data.decode()[64:69])
	inicio = time.time()

	while True:
		#~ data = s.recv(1024)
		#~ f.write(data)
		data = s.recv(1024) #Tamanho do buffer.
		#if data.decode() == msg:
		#print(data.decode())
		if 'Download concluido com sucesso!' in data.decode():
			print(data.decode())
			break

	fim = time.time()
	tempo_total = fim-inicio
	print ("Tempo do download:", tempo_total, "segundos.\n")
	print ("Taxa média de download:", (tamanho_txt/tempo_total), "mb/s\n")
	
	
#end

# menu = input("Escolha uma metrica: ")
while True:
	print("-------------")
	print ("Menu:\n1- RTT\n2- Download\nOutro- Sair")
	print("-------------")
	menu = input("=> Escolha uma metrica: ")
	if menu == '1':
		print ("\nEnviando requisicao para RTT...\n")
		inicio = time.time()
		s.send(str.encode(menu))
		data = s.recv(1024)
		fim = time.time()
		print (data.decode())
		print ("Tempo de RTT:", fim-inicio, "segundos.\n")
	elif menu == '2':
		print ("\nEnviando requisicao para Download...\n")
		s.send(str.encode(menu))
		download()
	else:
		s.send(str.encode(menu))
		break
print("\nServidor fechado.\n")
s.close()


#~ f.close()
#~ f = open('teste.txt', 'rb')
#~ texto = f.read()
#~ print("printando arquivo")
#~ print(texto)
