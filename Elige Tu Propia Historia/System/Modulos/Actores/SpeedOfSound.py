#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pilasengine
import os
import json

class Soniditos(pilasengine.actores.Actor):
	
	def inicializar (self, pilas):
		self.pilas = pilas
		self.x = 420
		self.y = 300
		self.ruta_normal = 'iconos/sonido_on.png'
		self.ruta_press = 'iconos/sonido_off.png'
		self.imagen = self.ruta_normal
		self.radio_de_colision = 15
		self.cuando_hace_click = self.cuando_pulsa
		self.activado = True
	
	def cambiar(self):
		if self.activado:
			self.pilas.deshabilitar_musica()
			self.pilas.deshabilitar_sonido()
			self.imagen = self.ruta_press
			self.activado = False
		else:
			self.pilas.deshabilitar_musica(estado=False)
			self.pilas.deshabilitar_sonido(estado=False)
			self.imagen = self.ruta_normal
			self.activado = True
	
	def cuando_pulsa(self):
		self.cambiar()
		diractual = os.getcwd()
		os.chdir("System"+os.sep+"Configuraciones")
		archivo4 = open ("configuracion.txt", "r+")
		opc = json.load(archivo4)
		archivo4.close()
		os.chdir(diractual)
		opc[0] = self.activado
		os.chdir("System"+os.sep+"Configuraciones")
		archivo5 = open ("configuracion.txt", "w+")
		json.dump(opc,archivo5)
		archivo5.close()
		os.chdir(diractual)

