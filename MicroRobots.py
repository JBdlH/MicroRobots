## Hauríeu de poder obrir-lo amb el vostre python. Si es queixa de les llibreries les haureu d'instal·lar, busqueu com fer-ho per internet. De moment podeu comentar els imports amb un # davant de la línia

#import numpy as np
#import networkx as nx
#import matplotlib.pyplot as plt

class Peca(object):
  def __init__(self,llista):
    """Crea una peça del taulell orientada directament al nord,
       la casella del mig a dalt (en el moment de la creació)
       marca la orientació"""
    self.caselles = llista
    # Pot estar en N, S, E, O
    self.orientacio = 'N'
    
  def dalt(self):
    if self.orientacio == 'N':
      return self.caselles[0:3]
    elif self.orientacio == 'E':
      return [self.caselles[6],self.caselles[3],self.caselles[0]]
    elif self.orientacio == 'O':
      return [self.caselles[2],self.caselles[5],self.caselles[8]]
    else:
      return [self.caselles[8],self.caselles[7],self.caselles[6]]
  
  def migh(self):
    if self.orientacio == 'N':
      return self.caselles[3:6]
    elif self.orientacio == 'E':
      return [self.caselles[7],self.caselles[4],self.caselles[1]]
    elif self.orientacio == 'O':
      return [self.caselles[1],self.caselles[4],self.caselles[7]]
    else:
      return [self.caselles[5],self.caselles[4],self.caselles[3]]
  
  def baix(self):
    if self.orientacio == 'N':
      return self.caselles[6:9]
    elif self.orientacio == 'E':
      return [self.caselles[8],self.caselles[5],self.caselles[2]]
    elif self.orientacio == 'O':
      return [self.caselles[0],self.caselles[3],self.caselles[6]]
    else:
      return [self.caselles[2],self.caselles[1],self.caselles[0]]
  
  def esquerra(self):
    if self.orientacio == 'N':
      return [self.caselles[0],self.caselles[3],self.caselles[6]]
    elif self.orientacio == 'E':
      return self.caselles[6:9]
    elif self.orientacio == 'O':
      return [self.caselles[2],self.caselles[1],self.caselles[0]]
    else:
      return [self.caselles[8],self.caselles[5],self.caselles[2]]
  
  def migv(self):
    if self.orientacio == 'N':
      return [self.caselles[1],self.caselles[4],self.caselles[7]]
    elif self.orientacio == 'E':
      return self.caselles[3:6]
    elif self.orientacio == 'O':
      return [self.caselles[5],self.caselles[4],self.caselles[3]]
    else:
      return [self.caselles[7],self.caselles[4],self.caselles[1]]
  
  def dreta(self):
    if self.orientacio == 'N':
      return [self.caselles[2],self.caselles[5],self.caselles[8]]
    elif self.orientacio == 'E':
      return self.caselles[0:3]
    elif self.orientacio == 'O':
      return [self.caselles[8],self.caselles[7],self.caselles[6]]
    else:
      return [self.caselles[6],self.caselles[3],self.caselles[0]]
    
#negres
p1 = Peca(['5P','2P','3P','6R','4R','3Y','4B','5G','3G'])
p2 = Peca(['1Y','5R','1G','6Y','5B','1R','1P','5Y','6P'])
p3 = Peca(['5W','4G','3B','3W','4Y','3R','2B','6B','6W'])
p4 = Peca(['4P','2W','2Y','6G','2G','1W','4W','2R','1W'])

class Taulel (object):
  def __init__ (self,llista_peces,llista_or):
    self.peces = llista_peces[:]
    for i in range(len(llista_peces)):
      self.peces[i].orientacio = llista_or[i]
  def __repr__(self):
    fila1 = cadena(self.peces[0].dalt() + self.peces[1].dalt())
    fila2 = cadena(self.peces[0].migh() + self.peces[1].migh())
    fila3 = cadena(self.peces[0].baix() + self.peces[1].baix())
    fila4 = cadena(self.peces[2].dalt() + self.peces[3].dalt())
    fila5 = cadena(self.peces[2].migh() + self.peces[3].migh())
    fila6 = cadena(self.peces[2].baix() + self.peces[3].baix())

    return fila1 + fila2+ fila3+ fila4+ fila5+ fila6


def cadena (llista):
  string=''
  for element in llista:
    string+=(element + ' ')
  string+='\n'
  return string

