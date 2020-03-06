#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pilasengine.actores.actor import Actor

class globito(Actor):
    """Representa un cuadro de dialogo estilo historietas.

    El actor se tiene que inicializar con una cadena de texto:

        >>> globo = pilas.actores.Globo("Hola mundo")

    .. image:: ../../pilas/data/manual/imagenes/actores/globo.png
    """

    def __init__(self, pilas, texto="", x=0, y=0, dialogo=None,
                 avance_con_clicks=True,ancho_globo=0,
                 alto_globo=0, objetivo=None, tiempo = 3, autoeliminar=True):
        self.dialogo = dialogo
        Actor.__init__(self, pilas, x=x, y=y)
        self.imagen = 'invisible.png'
        self.z = -1
        self.objetivo = objetivo

        ancho, alto = pilas.utils.obtener_area_de_texto(texto)

        # Podemos pasar el ancho del globo ya que si contiene opciones
        # cuyo texto es más largo que la cabecera del globo, no queda bien.
        if ancho_globo == 0:
            ancho = int((ancho + 12) - (ancho % 12))
        else:
            if ancho_globo > ancho:
                ancho = ancho_globo
            else:
                ancho = int((ancho + 12) - (ancho % 12))

        # Lo mismo para el alto
        if alto_globo == 0:
            alto = int((alto + 12) - alto % 12)
        else:
            alto = alto + alto_globo

        self.imagen = pilas.imagenes.cargar_superficie(ancho + 36,
                                                       alto + 24 + 35)

        self._pintar_globo(ancho, alto)
        self.imagen.texto(texto, 17, 20)
        self.centro = ("derecha", "abajo")
        self.escala = 0.1
        self.escala = [1], 0.2

        self.ancho_globo = ancho
        self.alto_globo = alto

        if avance_con_clicks:
            self.pilas.escena_actual().click_de_mouse.conectar(self.cuando_quieren_avanzar)

        if autoeliminar:
            pilas.escena_actual().tareas.una_vez(tiempo, self.eliminar)

        self.x = x
        self.y = y

    def colocar_origen_del_globo(self, x, y):
        """ Cambia la posicion del globo para que el punto de donde se emite el
        globo sea (x, y).
        :param x: Posición horizontal del globo.
        :type x: int
        :param y: Posición vertical del globo.
        :type y: int
        """
        self.x = x
        self.y = y

    def cuando_quieren_avanzar(self, *k):
        """Función que se ejecuta al hacer click para avanzar o
        eliminar el globo.
        """
        if self.dialogo:
            self.dialogo.avanzar_al_siguiente_dialogo()
        else:
            self.eliminar()

    def _pintar_globo(self, ancho, alto):
        imagen = self.pilas.imagenes.cargar("globo.png")

        # esquina sup-izq
        self.imagen.pintar_parte_de_imagen(imagen, 0, 0, 12, 12, 0, 0)

        # borde superior
        for x in range(0, int(ancho) + 12, 12):
            self.imagen.pintar_parte_de_imagen(imagen, 12, 0, 12, 12, 12 + x, 0)

         # esquina sup-der
        self.imagen.pintar_parte_de_imagen(imagen, 100, 0, 12, 12,
                                           12 + int(ancho) + 12, 0)

        # centro del dialogo
        for y in range(0, int(alto) + 12, 12):
            # borde izquierdo
            self.imagen.pintar_parte_de_imagen(imagen, 0, 12, 12, 12, 0, 12 + y)
            # linea horizontal blanca, para el centro del dialogo.
            for x in range(0, int(ancho) + 12, 12):
                self.imagen.pintar_parte_de_imagen(imagen, 12, 12, 12, 12,
                                                   12 + x, 12 + y)

            # borde derecho
            self.imagen.pintar_parte_de_imagen(imagen, 100, 12, 12, 12,
                                               12 + int(ancho) + 12, 12 + y)

        # parte inferior
        self.imagen.pintar_parte_de_imagen(imagen, 0, 35, 12, 12, 0,
                                           0 + int(alto) + 12 + 12)

        # linea horizontal de la parte inferior
        for x in range(0, int(ancho) + 12, 12):
            self.imagen.pintar_parte_de_imagen(imagen, 12, 35, 12, 12, 12 + x,
                                               0 + int(alto) + 12 + 12)

        self.imagen.pintar_parte_de_imagen(imagen, 100, 35, 12, 12,
                                           12 + int(ancho) + 12,
                                           0 + int(alto) + 12 + 12)
        # Pico de la parte de abajo
        self.imagen.pintar_parte_de_imagen(imagen, 67, 35, 33, 25,
                                           int(ancho) - 12,
                                           0 + int(alto) + 12 + 12)


    def actualizar(self):
        if self.objetivo:
            self.x = self.objetivo.x
            self.y = self.objetivo.y

