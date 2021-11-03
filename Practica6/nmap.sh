#!/bin/bash
echo "IP pubica: " > resultado.txt
curl ifconfig.co >> resultado.txt
echo -e  >> resultado.txt
echo "IP privada: " >> resultado.txt
hostname -I >> resultado.txt
echo "Escaneando segmento de red 192.168.1.0/24"
nmap -sP 192.168.1.0/24 >> resultado.txt
echo "Escanenado puertos de la ip 192.168.1.69"
nmap 192.168.1.69 >> resultado.txt
ipublica=$(curl ifconfig.co)
echo "Escanenado puertos de la IP publica"
nmap $ipublica >> resultado.txt

