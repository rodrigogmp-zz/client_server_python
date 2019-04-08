#!/usr/bin/env python

import socket
import time
import os


#tcp_ip = '18.204.102.146'
tcp_ip = '127.0.0.1'
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
			print(data.decode())
			break

	fim = time.time()
	tempo_total = fim-inicio
	print ("Tempo do download:", tempo_total, "segundos.\n")
	print ("Taxa média de download:", (tamanho_txt/tempo_total), "mb/s\n")


while True:
	print("-------------")
	print ("Menu:\n1- RTT\n2- Download\nOutro- Sair")
	print("-------------")
	menu = input("=> Escolha uma metrica: ")
	if menu == '1': #RTT
		print ("\nEnviando requisicao para RTT...\n")
		Rtt(menu)
	elif menu == '2': #Download
		print ("\nEnviando requisicao para Download...\n")
		Download(menu)
	else:
		s.send(str.encode(menu))
		break
print("\nServidor fechado.\n")
s.close()