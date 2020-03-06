#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pilasengine
import textwrap
from Hablar import globito
import random 
import os
from pattern.es import parse,split
from pattern.es import INFINITIVE
from pattern.es import conjugate

class ActorJuego(pilasengine.actores.Actor):
	
	def inicializar(self, pilas, nombre, direc):
		self.pilas = pilas
		diractual = os.getcwd()
		os.chdir("Historias"+os.sep+direc+os.sep+"images")
		self.imagen = self.pilas.imagenes.cargar(nombre+".png")
		os.chdir(diractual)
		self.nombre = nombre
		self.escala = 0.3
		self.x = random.sample(xrange(-300,300),1)
		self.y = random.sample(xrange(-300,300),1)
		self.hablar_norm = True
	
	def get_nombre(self):
		return self.nombre
	
	def set_nombre(self,nombre):
		self.nombre = nombre
		
	def transformar_dialogo(self,dialogo):
		"Transforma un diálogo a uno nuevo con los verbos en infinitivo"
		palabras = parse(dialogo).split()
		nueva_linea = ''
		print (palabras)
		for elem in palabras:
			for elem2 in elem:
				if 'VB' in elem2[1]: 
					pal = elem2[0]
					pal = str (pal)
					conj = conjugate(pal,INFINITIVE)
					nueva_linea = nueva_linea + conj + ' '
				else:
					pal = str (elem2[0])
					nueva_linea = nueva_linea + pal + ' '
		return nueva_linea
		
	def hablar(self,mensaje, modo):
		if not (self.hablar_norm):
			mensaje = self.transformar_dialogo(mensaje)
		largo = len(mensaje)
		if (modo == 1 ):
			tiempo = largo /2
			if (tiempo <= 10):
				tiempo += 10
		elif (modo == 2):
			tiempo = largo / 5
			if (tiempo <= 10):
				tiempo += 5
		else:
			tiempo = largo / 10
			if (tiempo <= 10):
				tiempo += 3
		dice = globito(self.pilas, textwrap.fill(mensaje, 30), self.x, self.y, objetivo = self,tiempo = tiempo)
		return False

