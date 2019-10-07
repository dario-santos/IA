import networkx as nx
import csv


def readGraph(filepath='autoestradas.txt'):
    G = nx.Graph()

    with open(filepath, newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',')

        for row in spamreader:
            if row[0] not in nx.classes.function.nodes(G):
                G.add_node(row[0])
            if row[1] not in nx.classes.function.nodes(G):
                G.add_node(row[1])
            G.add_edge(row[0], row[1], weight=row[2])
    
    return G

def printGraph(G):
    for i in nx.classes.function.nodes(G):
        for j in G.neighbors(i):
            print(i,j)

def main():
    G = readGraph()
    printGraph(G)
    
main()