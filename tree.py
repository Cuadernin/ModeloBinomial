import networkx as nx
import matplotlib.pyplot as plt
from graphviz import Source

def arbol(n,lista):
    """
    Diagrama para visualizar los precios

    Args:
        n: total de periodos
        lista: precios
    """
    G=nx.Graph()
    for i in range(n+1):
        for k in range(1,i+2):
            if i<n:
                G.add_edge((i,k),(i+1,k))
                G.add_edge((i,k),(i+1,k+1))
    posG,dic={},{}
    for i,node in enumerate(G.nodes()):
        posG[node]=[node[0],n+2+node[0]-2*node[1]] 
        dic[node]=lista[i]
    if n<=10:
        plt.figure(1,figsize=(20,20))
        nx.draw(G,pos=posG,node_size=150,alpha=0.6)
        nx.draw_networkx_labels(G,posG,labels=dic,font_size=15)
        xmax=n
        ymax=n*2
        plt.suptitle(f"Gráfico de {n} periodos")
        plt.xlim(-1,xmax+1)
        plt.ylim(-1,ymax+1)
        plt.show()
    elif n>10 and n<15:
        plt.figure(1,figsize=(20,20))
        nx.draw(G,pos=posG,node_size=70)
        nx.draw_networkx_labels(G,posG,labels=dic,font_size=15)
        xmax=n
        ymax=n*2
        plt.suptitle(f"Gráfico de {n} periodos")
        plt.xlim(-1,xmax+1)
        plt.ylim(-1,ymax+1)
        plt.show()
    elif n>=15 and n<29:
        plt.figure(1,figsize=(20,20))
        nx.draw(G,pos=posG,node_size=70,node_color='pink')
        nx.draw_networkx_labels(G,posG,labels=dic,font_size=10,font_weight='bold')
        xmax=n
        ymax=n*2
        plt.suptitle(f"Gráfico de {n} periodos")
        plt.xlim(-1,xmax+1)
        plt.ylim(-1,ymax+1)
        plt.show()
    elif n>=29 and n<48:
        plt.figure(1,figsize=(21,21))
        nx.draw(G,pos=posG,node_size=30,node_color='yellow')
        nx.draw_networkx_labels(G,posG,labels=dic,font_size=7,font_weight='bold')
        xmax=n
        ymax=n*2
        plt.xlim(-1,xmax+1)
        plt.ylim(-1,ymax+1)
        plt.suptitle(f"Gráfico de {n} periodos")
        plt.savefig("nodos.svg",dpi=1000)
    elif n>=48 and n<65:
        plt.figure(1,figsize=(21,21))
        nx.draw(G,pos=posG,node_size=40,node_color='orange',alpha=0.6)
        nx.draw_networkx_labels(G,posG,labels=dic,font_size=5,font_weight='bold')
        xmax=n
        ymax=n*2
        plt.xlim(-1,xmax+1)
        plt.ylim(-1,ymax+1)
        plt.suptitle(f"Gráfico de {n} periodos")
        plt.savefig("nodos.svg",dpi=1000)
    elif n>=65 and n<76:
        plt.figure(1,figsize=(21,21))
        nx.draw(G,pos=posG,node_size=30,node_color='orange',alpha=0.8)
        nx.draw_networkx_labels(G,posG,labels=dic,font_size=5,font_weight='bold')
        xmax=n
        ymax=n*2
        plt.xlim(-1,xmax+1)
        plt.ylim(-1,ymax+1)
        plt.suptitle(f"Gráfico de {n} periodos")
        #plt.savefig("nodos.pdf",bbox_inches="tight")
        plt.savefig("nodos.svg",dpi=1000)
    elif n>=76 and n<86:
        plt.figure(1,figsize=(21,21))
        nx.draw(G,pos=posG,node_size=20,node_color='orange',alpha=0.8)
        nx.draw_networkx_labels(G,posG,labels=dic,font_size=4,font_weight='bold')
        xmax=n
        ymax=n*2
        plt.xlim(-1,xmax+1)
        plt.ylim(-1,ymax+1)
        plt.suptitle(f"Gráfico de {n} periodos")
        #plt.savefig("nodos.pdf",bbox_inches="tight")
        plt.savefig("nodos.svg",dpi=1000)
    elif n>=86 and n<100:
        plt.figure(1,figsize=(21,21))
        nx.draw(G,pos=posG,node_size=10,node_color='orange',alpha=0.7)
        nx.draw_networkx_labels(G,posG,labels=dic,font_size=3,font_weight='bold')
        xmax=n
        ymax=n*2
        plt.xlim(-1,xmax+1)
        plt.ylim(-1,ymax+1)
        #plt.savefig("nodos.pdf",bbox_inches="tight")
        plt.savefig("nodos.svg",dpi=1000)
    elif n>=100:
        plt.figure(1,figsize=(21,21))
        nx.draw(G,pos=posG,node_size=3.1,node_color='orange',alpha=0.6)
        nx.draw_networkx_labels(G,posG,labels=dic,font_size=3.1,font_weight='bold')
        xmax=n
        ymax=n*2
        plt.xlim(-1,xmax+1)
        plt.ylim(-1,ymax+1)
        plt.suptitle(f"Gráfico de {n} periodos")
        #plt.savefig("nodos.pdf",bbox_inches="tight")
        plt.savefig("nodos.svg",dpi=1000)
