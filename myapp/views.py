from django.shortcuts import render
import networkx as nx

# Create your views here.

def graph(request):
    G = nx.Graph()
    G.add_nodes_from([1,2,3,4])
    G.add_edges_from([(1,2), (1,3), (2,3), (3,4)])

    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True)
    img_data = nx.nx_pydot.to_pydot(G).create_png()

    context = {'graph_image': img_data}
    return render(request, 'myapp/graph.html', context)
