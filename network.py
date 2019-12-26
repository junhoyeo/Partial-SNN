from schemas import Node, node_types
from pprint import pprint

model = [
  [Node(node_types.INPUT)] * 2,
  [Node(node_types.DEFAULT)] * 3,
  [Node(node_types.DEFAULT)] * 2,
  [Node(node_types.OUTPUT)] * 1,
]

pprint(model)
