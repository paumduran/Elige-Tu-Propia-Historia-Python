#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pilasengine
import os
from System.Modulos import menu_ppal
from System.Modulos import historia
from System.Modulos import acciones
from System.Modulos import menu_decision
from System.Modulos import puntuacion
from System.Modulos import escena
from System.Modulos.Actores import Protagonista

pilas = pilasengine.iniciar(ancho=1000, alto=700)


def vincular_comportamientos():
		pilas.comportamientos.vincular(acciones.correr)
		pilas.comportamientos.vincular(acciones.caminar)
		pilas.comportamientos.vincular(acciones.posicionar)
		pilas.comportamientos.vincular(acciones.salto)
		pilas.comportamientos.vincular(acciones.volverse_loco)
		pilas.comportamientos.vincular(acciones.reir)
		pilas.comportamientos.vincular(acciones.llorar)
		pilas.comportamientos.vincular(acciones.seguir_a)
		pilas.comportamientos.vincular(acciones.sonar)
		pilas.comportamientos.vincular(acciones.hablar_infinitivo)
		pilas.comportamientos.vincular(acciones.hablar_normal)
		pilas.comportamientos.vincular(acciones.escalar_actor)
		pilas.comportamientos.vincular(acciones.empujar)
		pilas.comportamientos.vincular(acciones.rodar_hacia)

# Vinculo de historias
pilas.actores.vincular(Protagonista.ActorJuego)
pilas.escenas.vincular(menu_decision.Menu_decision)
pilas.escenas.vincular(puntuacion.Puntuacion)
vincular_comportamientos()
pilas.escenas.vincular(menu_ppal.Menu_ppal)
pilas.escenas.vincular(historia.Historia)
pilas.escenas.vincular(escena.Escena)

pilas.escenas.Menu_ppal(pilas)

pilas.ejecutar()
