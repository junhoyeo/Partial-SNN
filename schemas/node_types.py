class NodeTypes:
  def __init__(self):
    self.INPUT = 0
    self.DEFAULT = 1
    self.OUTPUT = 2

  def get_repr(self, type_id: int):
    return ['INPUT', 'DEFAULT', 'OUTPUT'][type_id]

node_types = NodeTypes()
