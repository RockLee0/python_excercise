class Graph:
    def __init__(self,edges):
        self.edges=edges
        self.graph_dict={}
        for start,end in edges:
            if  start in  self.graph_dict:
                self.graph_dict[start].append(end)
            else:
                self.graph_dict[start]=[end]
        print('Graph dictionary look like after taking input as touple ',self.graph_dict)


if __name__=='__main__':
    routes=[
        ('mumbai','paris'),
        ('mumbai','dubai'),
        ('paris','new york'),
        ('dubai','new york'),
        ('new york', 'totento')
    ]

    routes_graph=Graph(routes)

