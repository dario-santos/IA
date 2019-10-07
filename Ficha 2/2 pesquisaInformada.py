import networkx as nx
from networkx import algorithms
import matplotlib.pyplot as plt
import csv

def readGraph(filepath='autoestradas.txt'):
    G = nx.Graph()

    with open(filepath, newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',')
        for row in spamreader:
            G.add_edge(row[0], row[1], weight=int(row[2]))
    
    return G

def readNode(G):
    while True:
        node = input("Insira o nome da cidade: ")
        if G.has_node(node):
            return node

def weightSum(G, L):
    sum = 0
    for i in range(0, len(L) - 1):
        start = L[i]
        end = L[i + 1]
        sum += int(G[start][end]['weight'])
    return sum

def main():
    G = readGraph()

    start_node = readNode(G)
    end_node = readNode(G)

    caminho = nx.astar_path(G, start_node, end_node, weight='weight')
    
    print(caminho, weightSum(G, caminho))
    
    plt.show()

main()