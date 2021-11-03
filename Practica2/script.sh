#!/bin/bash

Login(){
	a=true
	while [[ $a == true ]]; do
		echo "Introduzca el nombre de usuario"
		read Username
		echo "Introduzca su email"
		read Email
		echo "Confirme sus credenciales"
		echo "Nombre de usuario: " $Username
		echo "Correo electronico: " $Email
		echo "Sus contrasenas son correctas? (s/n)"
		read c
		if [ $c == "s" ]; then
			a=false
		else
			a=true
		fi
	done
}
CreaRepoLocal(){
	echo "Introduzca el nombre del repositorio local"
	read repo
	git init $repo
	if [ -d "$repo" ]; then
		echo "El directorio ${repo} se creo exitosamente"
	else
		echo "El directorio ${repo} no se pudo crear, 
				finalice y vuelva a ejecutar"
	fi
	cd $repo
	nano README.txt
	nano script.sh
	ls
}
AñadirArchivos(){
	echo "Agregaremos archivos, por favor indique el nombre de los archivos. Si ya no tiene archivos por agregar escriba exit"
	a=true
	while [[ $a==true ]]; do
		echo "Introduca el nombre del archivo a agregar"
		read archivo
		if [ -f "$archivo" ]; then
			git add $archivo
			echo "El archivo ${archivo} se agrego correctamente"
		elif [[ $archivo == "exit" ]]; then
			echo "Saliendo..."
			sleep 2
			break
		else
			echo "El archivo ${archivo} no se encontro, intentecon otro"
			ls
		fi
	done
	echo "Se procedera a hacer el commit"
	echo "Describa los cambios realizados en el commit"
	read m
	git commit -m $m
	echo "Introduzca el link para subir sus archivos"
	read link
	git remote add origin $link
	git branch -M main
	git push -u origin main
}
while [[ True ]]; do
	echo "Bienvenido Alan, disfruta tus tareas"
	echo "****************Menu****************"
	echo "Login------------------------------1"
	echo "Crear repositorio------------------2"
	echo "Añadir archivos--------------------3"
	echo "exit-------------------------------4"
	read a
	if [[ $a == 1 ]]; then
		Login
	elif [[ $a == 2 ]]; then
		CreaRepoLocal
	elif [[ $a == 3 ]]; then
		AñadirArchivos
	elif [[ $a == "exit" ]]; then
		break
	fi
done
