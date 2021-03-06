from schemas import Model, Node, node_types

from itertools import chain
from pprint import pprint

layers = [
  [
    Node(node_types.INPUT, 0, 0),
    Node(node_types.INPUT, 1, 0),
  ],
  [
    Node(node_types.HIDDEN, 0, 1),
    Node(node_types.HIDDEN, 1, 1),
    Node(node_types.HIDDEN, 2, 1),
  ],
  [
    Node(node_types.HIDDEN, 0, 2),
    Node(node_types.HIDDEN, 1, 2),
  ],
  [
    Node(node_types.OUTPUT, 0, 3)
  ],
]

model = Model(layers)

nodes = list(chain.from_iterable(model.layers))
for node in nodes:
  node.update_ref(nodes)

print('[+] 💡 Created Model!')
pprint(model.layers)
