# -*- coding: utf-8 -*-
"""
Created on Thu Oct  7 16:15:16 2021

@author: iker pintado garcía
"""
import bisect

#Input: grafo no dirigido representado con una matriz de adyacencia
#Output: lista de listas con los nodos que cumplen la clique más grande
def clique(graph):
    
    # Inicializamos el problema a los nodos individuales, cliques de 1
    #También creamos una lista para recorrerla más tarde
    cliques = []
    sizes = []
    for i in range(len(graph)):
        aux = [i]
        #lista de los posibles tamaños del máximo clique
        sizes.append(i+1)
        cliques.append(aux)
        
    #buscamos cliques de distintos rangos y actualizamos
    for size in sizes:
        newcliques=[]
        
        #procesaremos la nueva lista de todos los cliques de rango superior a partir de los de rango anterior
        for node in range(len(graph)):
            introducir(node, newcliques, cliques.copy(), graph)
            
        #Si no se han encontrado nuevos cliques, el rango mayor de cliques es el anterior
        #y esas cliques están en el vector cliques
        if not newcliques:
            #Devuelvo la tupla del clique y su tamaño el momento que no haya más cliques
            return cliques,size
        
        #Si han habido nuevos cliques, pasamos al siguente tamaño
        cliques=newcliques
        
    #En caso de que el grafo en sí mismo sea un clique gigante, lo devolvemos
    return cliques,size

#siempre introduciremos ordenadamente para facilitar la comparación, para ello usamos el paquete bisect
def introducir(node, new ,old, graph):
    for clique in old:
        #Si el nodo a introducir no está en el clique y puede unirse, se une
        if (node not in clique) and (belongsToClique(clique, node, graph)):
            #lo introducimos ordenado a clique (hacemos copia por seguridad)
            temp=clique.copy()
            bisect.insort(temp, node)
            insertarclique(temp, new)
    
#Inserta, si no está repetido, un nuevo clique a la lista
def insertarclique(clique, new):
    #si la lista de nuevos cliques está vacía, metemos primer valor
    if not len(new):
        new.append(clique)
    else:
        add=True
        for lista in new:
            #las cliques serán las mismas si sus listas son idénticas ya que sus elementos están ordenados
            if(exactCopy(lista,clique)):
                add=False
                break
        if add:
            new.append(clique)
        
#Solo devuelve true si uno y dos son copias exactas
def  exactCopy(uno, dos):
    if len(uno)!=len(dos):
        return False
    else:
        for i in range(len(uno)):
            if uno[i]!=dos[i]:
                return False
        return True
        
        
#Comprueba si un nodo pertenece a un clique  
def belongsToClique(clique, node, graph):
    for i in clique:
        #Si el nodo a introducir no aumenta el clique que ya hay
        if(not graph[i][node]):
            return False
    #Si no encuentra un elemento que eche al nodo del clique, es que el clique es expansible
    return True








def test():
    
    g1=[[1,1,1,1,0,1],
        [1,1,1,0,0,0],
        [1,1,1,1,1,1],
        [1,0,1,1,0,1],
        [0,0,1,0,1,1],
        [1,0,1,1,1,1]]
    
    g2=[[1,0,1,0,1,1,1,1,0],
        [0,1,0,0,0,0,1,0,1],
        [1,0,1,0,1,1,0,1,0],
        [0,0,0,1,0,0,1,0,1],
        [1,0,1,0,1,0,0,0,0],
        [1,0,1,0,0,1,1,1,0],
        [1,1,0,1,0,1,1,0,1],
        [1,0,1,0,0,1,0,1,0],
        [0,1,0,1,0,0,1,0,1]]
    
    g3=[[1,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [0,1,0,0,0,0,0,0,0,0,0,0,1,0],
        [0,0,1,0,1,0,1,1,1,1,0,0,0,0],        
        [0,0,0,1,0,0,0,0,0,0,1,0,0,0],
        [0,0,1,0,1,0,1,1,1,0,0,0,0,0],
        [0,0,0,0,0,1,0,0,0,1,0,1,0,0],
        [0,0,1,0,1,0,1,0,0,0,0,0,0,0],
        [0,0,1,0,1,0,0,1,1,0,0,0,0,0],
        [0,0,1,0,1,0,0,1,1,1,0,0,0,0],
        [0,0,1,0,0,1,0,0,1,1,1,1,1,1],
        [0,0,0,1,0,0,0,0,0,1,1,1,1,1],
        [0,0,0,0,0,1,0,0,0,1,1,1,1,1],
        [0,1,0,0,0,0,0,0,0,1,1,1,1,1],
        [1,0,0,0,0,0,0,0,0,1,1,1,1,1]]



    print(clique(g1),"\n")
    print(clique(g2),"\n")
    print(clique(g3),"\n")






