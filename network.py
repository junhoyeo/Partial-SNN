from schemas import Node, node_types
from pprint import pprint

model = [
  [Node(node_types.INPUT)] * 2,
  [Node(node_types.HIDDEN)] * 3,
  [Node(node_types.HIDDEN)] * 2,
  [Node(node_types.OUTPUT)] * 1,
]

pprint(model)
