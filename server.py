#!/usr/bin/env python
import os
import socket

tcp_ip = '18.204.102.146'
tcp_port = '7386'

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((tcp_ip, tcp_port))
s.listen(5)

print("Escutando...") 
conn, addr = s.accept()

#~ #print 'Endereco de conexao: ', addr

#~ while True:


data = conn.recv(1024)
if (data == '1'):
	print 'Metrica: RTT'
	conn.send('Requisicao aceita.\n')
else:
	print 'Metrica: Download'
	conn.send('Requisicao aceita. Download em andamento:\n')
	f = open('texto.txt','rb')
	l = f.read(1024)
	#servidor enviando o arquivo para o cliente
	while (l):
		conn.send(l)
		l = f.read(1024)
	f.close()

conn.close()
