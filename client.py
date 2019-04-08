#!/usr/bin/env python

import socket
import time
import os


tcp_ip = '177.105.60.80'
#tcp_ip = '127.0.0.1'
tcp_port = 7502

s = socket.socket(socket.AF_INET,
				socket.SOCK_STREAM)
s.connect((tcp_ip, tcp_port))

def Rtt(menu):
	inicio = time.time()
	s.send(str.encode(menu)) #Requisição de RTT
	data = s.recv(1024) #Resposta da requisição
	fim = time.time()
	print (data.decode())
	print ("Tempo de RTT:", format((fim-inicio)*1000, '.2f'), "ms.\n")

def Download(menu):
	s.send(str.encode(menu)) #Requisição de Download
	data = s.recv(1024)  #Resposta da requisição
	print (data.decode()) 
	tamanho_txt = float(data.decode()[64:69]) #Fatiamento da string para receber o tamanho
	inicio = time.time()

	while True:
		data = s.recv(1024) #Recebendo dados em buffers de 1024

		if 'Download concluido com sucesso!' in data.decode(): 
			break

	fim = time.time()
	tempo_total = fim-inicio
	print ("Tempo do download:", tempo_total, "segundos.\n")
	print ("Taxa média de download:", (tamanho_txt/tempo_total), "mb/s\n")

def Upload(menu):
	print ('Metrica: Upload\n')
	s.send(str.encode(menu))
	tamanho_txt = os.path.getsize('texto.txt') #Calculando tamanho do arquivo de download em bytes
	tamanho_txt = (tamanho_txt/1024)/1024 #Convertendo tamanho para mb
	file = open('texto.txt','rb')
	inicio = time.time()
	l = file.read(1024)
	while (l): #cliente enviando o arquivo para o server
		s.send(l)
		print(l.decode())
		l = file.read(1024)
	fim = time.time()
	message = "Upload concluido com sucesso!\n"
	s.send(str.encode(message))
	tempo_total = fim-inicio
	print (message, "\nTempo de upload:", tempo_total, "segundos\n")
	print ("Taxa média de upload:", (tamanho_txt/tempo_total), "mb/s\n")
	file.close()


while True:
	print("-------------")
	print ("Menu:\n1- RTT\n2- Download\n3- Upload\nOutro- Sair")
	print("-------------")
	menu = input("=> Escolha uma metrica: ")
	if menu == '1': #RTT
		print ("\nEnviando requisicao para RTT...\n")
		Rtt(menu)
	elif menu == '2': #Download
		print ("\nEnviando requisicao para Download...\n")
		Download(menu)
	elif menu == '3':
		print ("\nIniciando upload...\n")
		Upload(menu)
	else:
		s.send(str.encode(menu))
		break
print("\nServidor fechado.\n")
s.close()
