from .model import Model
from .node_types import node_types

class Node:
  def __init__(self, node_type: int, x: int, y: int, z: int = 0):
    self.axon: float = 1.0
    self.threshold: float = -52.0
    self.voltage: float = -65.0
    self.theta: float = 0.05
    self.delay: float = 1
    self.x: int = x
    self.y: int = y
    self.z: int = z
    self.type: int = node_type
    self.others: list = []

  def __repr__(self):
    coord = f'({self.x}, {self.y}, {self.z})'
    return f'<Node {node_types.get_repr(self.type)}, v: {self.voltage}, c: {coord}>'

  def update_ref(self, nodes: list):
    self.others = [
      node
      for node in nodes
      if (
        node.x != self.x and
        node.y != self.y and
        node.type != node_types.INPUT
      )
    ]

  def spike(self):
    print(self.others)
    for node in self.others:
      node.voltage += self.theta
      if node.voltage > node.threshold:
        node.spike()
    print(self.others)
