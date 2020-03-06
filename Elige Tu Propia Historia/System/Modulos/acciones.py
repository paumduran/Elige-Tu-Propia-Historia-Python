#!/usr/bin/env python
# -*- coding: utf-8 -*-

#import necesario para asignar direcciones de archivos dentro de carpetas.
import os
from Actores.Protagonista import ActorJuego
#import necesario para las funciones matematicas
import math
import pilasengine
# import necesario para heredar de la clase Comportamiento.
from pilasengine.comportamientos import Comportamiento

class caminar(Comportamiento):
	"El actor se mueve a paso lento hasta la posición x, y."
	
	def tiempo (self):
		"Determina que tiempo va a tardar en moverse de la posicion actual a la siguiente."
		camino = math.sqrt( ((self.finX - self.receptor.x)**2) + ((self.finY - self.receptor.y)**2))
		saltos = int(camino//20)
		self.velocidad = 0.7 * saltos
	
	def iniciar(self, receptor, pilas, tup):
		"Inicializa los valores de la instancia. Parametros: tup - formato:(x,y)."
		self.receptor = receptor
		self.finY = int(tup[1])
		self.finX = int(tup[0])
		self.tiempo()
		
	def actualizar(self): 
		"Realiza el procedimiento de caminar desde la posicion actual, hasta la indicada con la velocidad calculada."
		self.receptor.x = [self.finX],self.velocidad
		self.receptor.y = [self.finY],self.velocidad
		return True 

class correr(Comportamiento):
	"El actor se mueve a paso rápido hasta la posición x, y."
	
	def tiempo (self):
		"Determina que tiempo va a tardar en moverse de la posicion actual a la siguiente."
		camino = math.sqrt( ((self.finX - self.receptor.x)**2) + ((self.finY - self.receptor.y)**2))
		saltos = int(camino//20)
		self.velocidad = 0.2 * saltos
		
	def iniciar(self, receptor, pilas,tup):
		"Inicializa los valores de la instancia. Parametros: tup - formato:(x,y)."
		self.receptor = receptor
		self.finY = int(tup[1])
		self.finX = int(tup[0])
		self.tiempo()
		
	def actualizar(self):
		"Realiza el procedimiento de correr desde la posicion actual, hasta la indicada con la velocidad calculada."
		self.receptor.x = [self.finX],self.velocidad
		self.receptor.y = [self.finY],self.velocidad
		return True 

class posicionar(Comportamiento):
	"El actor aparece (se posiciona, sin animación) en la posición x, y."
	
	def iniciar(self, receptor, pilas, tup):
		"Inicializa los valores de la instancia. Parametros: tup - formato:(x,y)."
		self.receptor = receptor
		self.avY = int(tup[1])
		self.avX = int(tup[0])
		
	def actualizar(self): 
		"Realiza el procedimiento de correr desde la posicion actual, hasta la indicada con la velocidad calculada."
		self.receptor.x = self.avX
		self.receptor.y = self.avY
		return True 

class Salto(Comportamiento):
	"Realiza un salto, cambiando los atributos 'y'."
	
	def iniciar(self, receptor, x, y, velocidad_inicial=2.5, cuando_termina=None):
		"Inicializa los valores de la instancia. Parametros: x, y, velocidad_inicial = 2.5, cuando_termina = None ."
		#se define velocidad inicial 2.5 para que el salto dure poco y no sea demasiado alto. De esa manera
		#va en conjunto con las proporciones de 1 segundo para repetir tarea.
		self.receptor = receptor
		self.velocidad_inicial = velocidad_inicial
		self.cuando_termina = cuando_termina
		#self.sonido_saltar = self.pilas.sonidos.cargar("audio/saltar.wav")
		self.suelo = int(self.receptor.y)
		self.velocidad = self.velocidad_inicial
		#self.sonido_saltar.reproducir()
		self.velocidad_aux = self.velocidad_inicial
		self.detY = y
		self.detX = x
	
	def actualizar(self):
		"Salta incrementando y decrementando los valores de y, al llegar al suelo (valor inicial de y) se mueve hasta la posicion indicada."
		self.receptor.y += self.velocidad
		self.velocidad -= 0.3
		
		if self.receptor.y <= self.suelo:
			self.velocidad_aux /= 2.0
			self.velocidad = self.velocidad_aux
			
			if self.velocidad_aux <= 1:
				# Si toca el suelo
				self.receptor.y = [self.suelo + self.detY]
				self.receptor.x = [self.receptor.x + self.detX]
				if self.cuando_termina:
					self.cuando_termina()
				return True

class salto(Comportamiento):
	"El actor se mueve saltando hasta la posición x, y."
	
	def avances(self):
		"Define el tamanio del avance en x e y por cada salto y la cantidad de saltos."
		camino = math.sqrt( ((self.finX - self.receptor.x)**2) + ((self.finY - self.receptor.y)**2))
		saltos = int(camino//20)
		self.avX = (self.finX-self.receptor.x)//saltos
		self.avY = (self.finY-self.receptor.y)//saltos
	
	
	def iniciar(self, receptor, pilas, tup):
		"Inicializa los valores de la instancia. Parametros: tup - formato: (x,y)."
		self.receptor = receptor
		self.pilas = pilas
		self.finX = int(tup[0])
		self.finY = int(tup[1])
		self.avances()
	
	def saltare(self):
		"Realiza un salto y se mueve el avance calculado previamente."
		if (self.receptor.x == self.finX):
			avX = 0
		elif (abs(self.finX - self.receptor.x) <= abs(self.avX)):
			avX = self.finX -self.receptor.x
		else:
			avX = self.avX
		
		if (self.receptor.y == self.finY):
			avY = 0
		elif (abs(self.finY - self.receptor.y) <= abs(self.avY)):
			avY = self.finY - self.receptor.y
		else:
			avY = self.avY
		self.receptor.hacer(Salto,avX,avY)
		if (self.receptor.y == self.finY) and (self.receptor.x == self.finX):
			return False
		else:
			return True
	
	def actualizar(self):
		"Realiza el comportamiento determinado, cada 1 segundo hasta llegar a la posicion final."
		self.pilas.escena_actual().tareas.agregar(1,self.saltare)
		return True
	
class volverse_loco(Comportamiento):
	"El actor gira sobre su eje 3 veces."
	
	def iniciar(self, receptor, pilas):
		"Inicializa los valores de la instancia. Parametros: sin parametros."
		self.pilas = pilas
		self.receptor = receptor
		self.rotacion = 1080
		self.duracion = 3
		
	def actualizar(self):
		"Realiza el comportamiento"
		self.pilas.utils.interpolar(self.receptor, "rotacion", [self.rotacion], duracion=self.duracion)
		return True

class reir(Comportamiento):
	"El actor emite el sonido de risa y sobre su imagen aparece un emoticón de risa."
	
	def iniciar(self, receptor, pilas):
		"Inicializa los valores de la instancia. Parametros: sin parametros."
		self.pilas = pilas
		self.receptor = receptor
		diractual = os.getcwd()
		os.chdir("System"+os.sep+"Sonidos")
		self.risa = self.pilas.sonidos.cargar("risa.ogg")
		os.chdir(diractual)
		os.chdir("System"+os.sep+"Imagenes")
		imagen = self.pilas.imagenes.cargar("risa.png")
		self.emoji = self.pilas.actores.Actor()
		self.emoji.imagen = imagen
		self.emoji.escala = 0.15
		os.chdir(diractual)

	def actualizar(self): 
		"Realiza el comportamiento."
		self.risa.reproducir(repetir=False)
		self.emoji.x = self.receptor.x
		self.emoji.y = self.receptor.y
		self.pilas.escena_actual().tareas.una_vez(2, self.emoji.eliminar)
		return True

class llorar(Comportamiento):
	"El actor emite el sonido de un llanto y sobre su imagen aparece un emoticón de tristeza/llanto."
	
	def iniciar(self, receptor, pilas):
		"Inicializa los valores de la instancia. Parametros: sin parametros."
		self.pilas = pilas
		self.receptor = receptor
		diractual = os.getcwd()
		os.chdir("System"+os.sep+"Sonidos")
		self.llanto = self.pilas.sonidos.cargar("llanto.ogg")
		os.chdir(diractual)
		os.chdir("System"+os.sep+"Imagenes")
		imagen = self.pilas.imagenes.cargar("llanto.png")
		self.emoji = self.pilas.actores.Actor()
		self.emoji.imagen = imagen
		self.emoji.escala = 0.15
		os.chdir(diractual)

	def actualizar(self):
		"Realiza el comportamiento."
		self.llanto.reproducir(repetir=False)
		self.emoji.x = self.receptor.x
		self.emoji.y = self.receptor.y
		self.pilas.escena_actual().tareas.una_vez(4, self.emoji.eliminar)
		return True

class seguir_a(Comportamiento):
	"El actor se mueve hasta la posición del actor2."

	def tiempo (self):
		"Determina que tiempo va a tardar en moverse de la posicion actual hasta el otro actor."
		camino = math.sqrt( ((self.finX - self.receptor.x)**2) + ((self.finY - self.receptor.y)**2))
		saltos = int(camino//20)
		self.velocidad = 0.5 * saltos
		
	def iniciar(self, receptor, pilas,actor):
		"Inicializa los valores de la instancia. Parametros: tup - formato: (actor2)."
		self.receptor = receptor
		self.quien = actor
		# determina el final del recorrido sin ubicarse debajo del actor2
		if (self.quien.x > 0):
			self.finX = (self.quien.x - (self.quien.ancho) * (self.quien.escala) / 1.25)
		else:
			self.finX = (self.quien.x + (self.quien.ancho) * (self.quien.escala) / 1.25)
		if (self.quien.y > 0):
			self.finY = (self.quien.y - (self.quien.alto)*(self.quien.escala) / 1.25)
		else:
			self.finY = (self.quien.y + (self.quien.alto)*(self.quien.escala) / 1.25)
		self.tiempo()
		
	def actualizar(self):
		"Realiza el comportamiento."
		self.receptor.x = [self.finX],self.velocidad
		self.receptor.y = [self.finY],self.velocidad
		return True 

class sonar(Comportamiento):
	"Reproduce el sonido o música indicado por el nombre de archivo."
	
	def iniciar(self, receptor, pilas,tup):
		"Inicializa los valores de la instancia. Parametros: tup - formato: (dir_del_sonido)."
		self.pilas = pilas
		self.receptor = receptor
		diractual = os.getcwd()
		direccion = tup[0].split(os.sep)
		if (len(direccion) >1):
			dire2 = direccion[:-1]
			dire=""
			for parte in dire2:
				dire += parte +os.sep
			dire = dire[:-1]
			os.chdir(dire)
			self.sonido = self.pilas.sonidos.cargar(direccion[-1])
			os.chdir(diractual)
		else:
			self.sonido = self.pilas.sonidos.cargar(tup[0])
		
	def actualizar(self): 
		"Realiza el comportamiento."
		self.sonido.reproducir(repetir=False)
		return True

# POSIBLES ERRORES:
class hablar_infinitivo(Comportamiento):
	"Determina que las siguientes lineas del actor van a ser con los verbos en infinitivo."
	
	def iniciar(self, receptor, pilas):
		"Inicializa los valores de la instancia. Parametros: Sin Parametros."
		self.receptor = receptor
		
	def actualizar(self): 
		"Actualiza el valor de hablar_norm del actor en False para que hable en infinitivo."
		self.receptor.hablar_norm = False
		return True 

class hablar_normal(Comportamiento):
	"Determina que las siguientes lineas del actor van a ser normales."
	
	def iniciar(self, receptor, pilas):
		"Inicializa los valores de la instancia. Parametros: Sin Parametros."
		self.receptor = receptor
		
	def actualizar(self): 
		"Actualiza el valor de hablar_norm del actor en True para que deje de hablar en infinitivo."
		self.receptor.hablar_norm = True
		return True 


# DEFINIDA POR EL PROGRAMADOR
class escalar_actor(Comportamiento):
	"La imagen del actor se escala al valor definido por el parametro."
	# UTILIDAD: si la imagen definida por el usuario es demasiado grande o demasiado pequeña, permite redefinirla a un tamaño que se considere valido.
	
	def iniciar(self, receptor, pilas, tup):
		"Inicializa los valores de la instancia. Parametros: tup - formato: (escala)."
		self.receptor = receptor
		self.escala = float(tup[0])
		
	def actualizar(self):
		"Realiza el comportamiento." 
		self.receptor.escala = self.escala
		return True 

#posible error en empujar al empujar una segunda vez. ver al usar en historia
class empujar(Comportamiento):
	"El actor va rapidamente hasta la posicion del actor2 y lo empuja."

	def tiempo (self):
		"Determina el tiempo en que se va a mover hacia el actor2, y cual va a ser el punto final al que debe moverse el actor2."
		camino = math.sqrt( ((self.finX - self.receptor.x)**2) + ((self.finY - self.receptor.y)**2))
		saltos = int(camino//10)
		self.velocidad = 0.05 * saltos
		#saco plus de figuras en caso de que se superpongan
		vy = (self.finY - self.receptor.y)
		vx =(self.finX - self.receptor.x)
		xa2 = (self.actor2.ancho /2 + vx ) * self.actor2.escala *0.3
		ya2 = (self.actor2.alto /2 +vy)* self.actor2.escala * 0.3
		xr = (self.receptor.ancho/2 +vx) * self.receptor.escala *0.3
		yr = (self.receptor.alto/2 +vy) * self.receptor.escala  *0.3
		# asigno el punto final de actor2s
		self.finX2 = self.finX + vx * 0.3 +xa2 + xr
		self.finY2 = self.finY + vy * 0.3 +ya2 + yr
		
	def iniciar(self, receptor, pilas,actor):
		"Inicializa los valores de la instancia. Parametros: tup - formato: (actor2)."
		self.pilas = pilas
		self.receptor = receptor
		self.actor2 = actor
		# determina a que lugar debe moverse el receptor.
		self.finX = self.actor2.x
		self.finY = self.actor2.y 
		self.tiempo()
	
	def choque(self):
		"Mueve al actor2 a la posicion que corresponde."
		self.actor2.y = [self.finY2],self.velocidad
		self.actor2.x = [self.finX2],self.velocidad

	def actualizar(self): 
		"Realiza el comportamiento."
		self.receptor.x = [self.finX],self.velocidad
		self.receptor.y = [self.finY],self.velocidad
		self.pilas.colisiones.agregar(self.receptor,self.actor2, self.choque)
		self.pilas.colisiones.limpiar()
		return True

class rodar_hacia(Comportamiento):
	"El actor se mueve rodando hasta la posicion x,y." 
	
	def tiempo (self):
		"Determina el tiempo en que se va a mover hacia el nuevo punto, y cuantos giros realizara para llegar hasta ahi."
		camino = math.sqrt( ((self.finX - self.receptor.x)**2) + ((self.finY - self.receptor.y)**2))
		saltos = int(camino//20)
		self.velocidad = 0.2 * saltos
		self.rotacion *= (saltos/3)
	
	def rodar(self):
		"Rueda desde donde esta hasta el nuevo punto, en un tiempo determinado por la distancia que tiene que recorrer, al igual que la cantidad de giros. "
		self.receptor.rotacion = [self.rotacion],self.velocidad
		self.receptor.x = [self.finX],self.velocidad
		self.receptor.y = [self.finY],self.velocidad
			
	def iniciar(self, receptor, pilas,tup):
		"Inicializa los valores de la instancia. Parametros: tup - formato: (x,y)."
		self.pilas = pilas
		self.receptor = receptor
		self.rotacion = 360
		self.finX = int(tup[0])
		self.finY = int(tup[1])
		self.tiempo()
		
	def actualizar(self):
		"Realiza el comportamiento."
		self.rodar()
		return True
