import networkx as nx
import matplotlib.pyplot as plt
#Crear un grafo vacio
G= nx.Graph()
#Agregar nodos al grafo
G.add_node("PADRE")
G.add_node("HIJO 1")
G.add_node("HIJO 2")
#Agregar Conexiones entre nodos
G.add_edge("PADRE","HIJO 1")
G.add_edge("PADRE","HIJO 2")
#Dibujar el Grafo
pos = nx.spring_layout(G)
nx.draw(G,with_labels="true")
plt.show()

