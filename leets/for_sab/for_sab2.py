# import pandas as pd
# diamonds = pd.read_csv(
#     'http://vincentarelbundock.github.io/Rdatasets/csv/ggplot2/diamonds.csv')
# # diamonds[['price', 'carat']].hist()

# diamonds[['price']].hist()

test = {1: [2, 3, 4], 2: [1, 5, 6], 3: [1, 7, 8], 4: [1, 9], 5: [2], 6: [2], 7: [3], 8: [3], 9: [4]}

def shortest_path(start_node, end_node, graph):
    if start_node == end_node:
        return [start_node]
    else:
        options = graph[start_node]
        for item in options:
            return [start_node] + shortest_path(item, end_node, graph)

shortest_path(1, 7, test)