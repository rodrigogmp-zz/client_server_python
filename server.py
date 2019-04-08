#!/usr/bin/env python
import os
import socket

tcp_ip = '127.0.0.1'
tcp_port = 7502

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', tcp_port))
s.listen(5)

conn, addr = s.accept()

while True:
	print("Escutando...\n") 
	data = conn.recv(1024)
	if (data == str.encode('1')): #RTT
		print ('Metrica: RTT')
		message = "Requisicao aceita.\n"
		conn.send(str.encode(message)) #Enviando resposta
		print ('\nMetrica executada com sucesso!\n')
	elif (data == str.encode('2')): #Download
		print ('Metrica: Download')
		tamanho_txt = os.path.getsize('texto.txt') #Calculando tamanho do arquivo de download em bytes
		tamanho_txt = (tamanho_txt/1024)/1024 #Convertendo tamanho para mb
		message = "Requisicao aceita. Download em andamento...\nTamanho do arquivo: "+ str(tamanho_txt)[0:5] + " mb.\n"
		conn.send(str.encode(message)) #Enviando mensagem de requisição aceita e o tamanho do arquivo ao client.
		file = open('texto.txt','rb')
		l = file.read(1024)
		while (l): #servidor enviando o arquivo para o cliente
			print(l)
			conn.send(l)
			l = file.read(1024)
		message = "Download concluido com sucesso!\n"
		conn.send(str.encode(message)) #Mensagem para o client encerrar o loop de recepção de dados.
		print ('\nMetrica executada com sucesso!\n')
		file.close()
	elif (data == str.encode('3')):
		while True:
			data = conn.recv(1024) #Recebendo dados em buffers de 1024
			if 'Upload concluido com sucesso!' in data.decode(): 
				break

		print("Métrica executada com sucesso!\n")
	else:
		break
print("Servidor fechado.\n")
conn.close()
