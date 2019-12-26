from .node_types import node_types

class Node:
  def __init__(self, node_type: int, x: int, y: int, z: int = 0):
    self.axon: float = 1.0
    self.threshold: float = -52.0
    self.voltage: float = -65.0
    self.x: int = x
    self.y: int = y
    self.z: int = z
    self.type: int = node_type

  def __repr__(self):
    return f'<Node {node_types.get_repr(self.type)} ({self.x}, {self.y}, {self.z})>'
