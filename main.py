"""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Unimelb Network

Created by Harrison Langdon on 17/10/2021

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
import networkx
import networkx as nx
import matplotlib.pyplot as plt
from pyvis import network as net
from IPython.core.display import display, HTML

title = "Stop 2 Social Circle"
TEST = False
COLOUR = '#222222'
COLOUR = '#FFFFFF'

members = [
    "Ashley",
    "Bangyan",
    "Bowen",
    "Harrison",
    "Kasie",
    "Holly",
    "Jasir",
    "Louis",
    "Jenny",
    "Sai",
    "Alex",
    "Amanda",
    "Anna",
    "Ava",
    "Anne",
    "Emily",
    "Cassidy",
    "Danny",
    "Francesco",
    "Gavin",
    "Helena",
    "Irena",
    "Isaac",
    "Jake",
    "Jerry",
    "Leon",
    "Margaret",
    "Maria",
    "Nash",
    "Nijiko",
    "Pat",
    "Aidan",
    "Peter",
    "Sahil",
    "Sam H",
    "Sam S",
    "Thi",
    "Silvy",
    "Teak",
    "Tsui",
    "Tunan",
    "Zach",
    "Grace",
    "Cindy"
]

formatted_data = sorted(members)

data_old = {
    "Ashley": ["Bangyan", "Kasie", "Holly", "Jasir", "Ava", "Danny", "Gavin", "Margaret", "Maria", "Nash", "Pat",
               "Sam H"],
    "Tsui": ["Sam H", "Sam S", "Thi", "Tunan", "Peter", "Aidan", "Holly", "Helena", "Sai", "Emily", "Bangyan", "Jenny"],
    "Kasie": ["Thi", "Ashley", "Harrison", "Alex", "Amanda"],
    "Irena": ["Thi"],
    "Jenny": ["Tsui", "Ashley", "Sai", "Bangyan", "Holly"],
    "Holly": ["Ashley", "Margaret", "Aidan", "Danny"],
    "Thi": ["Kasie", "Amanda", "Alex", "Tsui", "Irena", "Cindy", "Cassidy", "Francesco", "Anne", "Anna", "Leon",
            "Helena", "Bangyan"],
    "Harrison": ["Ashley", "Kasie", "Margaret", "Teak", "Jake", "Grace", "Bowen"],
    "Teak": ["Jake", "Sam S", "Harrison"],
    "Sai": ["Isaac", "Sahil", "Tsui", "Zach"],
    "Bangyan": ["Thi", "Tsui", "Aidan", "Jenny"],
    "Bowen": ["Grace", "Harrison", "Holly"],
    "Sam H": ["Isaac", "Sam S", "Jerry", "Tsui", "Jerry"],
    "Grace": ["Bowen", "Holly", "Harrison", "Silvy", "Tunan", "Louis"],
    "Leon": ["Nijiko"],
    "Isaac": ["Sahil", "Zach"],
}

# Checks that name is valid for the list
def checker(name, data):
        try:
            # Attempts to get the name
            if type(data[name]) == list:
                return True
            else:
                return False
        except:
            return False


def write_data():
    data = open("data.txt", "a")

    for name in members[0:4]:
        try:
            print(f"Enter data for {name}")
            data.write(input())
        except:
            x = 2

    data.close()


def graph_pyvis():
    g = net.Network(height="800px", width="100%", bgcolor=COLOUR, heading=title)

    for name in members:
        g.add_node(name, value=100)

    for name in members:
        if checker(name, data_old):
            for connection in data_old[name]:
                g.add_edge(name, connection)

    g.repulsion(node_distance=260, spring_length=200)
    # g.show_buttons(filter_=True)
    g.show("main.html")
    display(HTML("main.html"))
    return g


# Used for graphing in networkx
# Operates almost identical tograph_pyvis
def graph_networkx():
    G = nx.Graph()

    for name in members:
        G.add_node(name)

    for name in members:
        if checker(name, data_old):
            # print(data_old[name])
            for connection in data_old[name]:
                G.add_edge(name, connection)
    nx.draw(G, with_labels=False, font_weight='bold')
    plt.show()
    return 0


if __name__ == "__main__":
    graph_pyvis()
    # graph_networkx()
