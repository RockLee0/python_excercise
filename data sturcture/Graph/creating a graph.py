class Graph:
    def __init__(self,edges):
        self.edges=edges
        self.graph_dict={}
        for start,end in edges:
            if  start in  self.graph_dict:  # checks if start value from the touple matches with any existing key of the current dictionary
                self.graph_dict[start].append(end)
            else:
                self.graph_dict[start]=[end]
        print('Graph dictionary look like after taking input as touple ',self.graph_dict)

    def get_paths(self,start,end,path=[]):
        path=path+[start]

        if start==end:
            return [path]
        if start not in self.graph_dict:
            return []

        paths=[]

        for node in self.graph_dict[start]:
            if node not in path:
                new_paths=self.get_paths(node,end,paths)
                for p in new_paths:
                    paths.append(p)
        return paths


    def get_shortest_path(self,start,end,path=[]):
        path=path+[start]

        if start==end:
            return [path]

        if start not in self.graph_dict:
            return []

        shortest_path=None
        for node in self.graph_dict[start]:
            sp=self.get_shortest_path(node,end,path)
            if shortest_path is None or len(sp)<len(shortest_path):
                shortest_path=sp
        return shortest_path






if __name__=='__main__':
    routes=[
        ('mumbai','paris'),
        ('mumbai','dubai'),
        ('paris','new york'),
        ('dubai','new york'),
        ('new york', 'totento')
    ]

    routes_graph=Graph(routes)
    start='mumbai'
    end='new york'

    print(f'shortest path: between {start} and {end} is ', routes_graph.get_shortest_path(start,end))
