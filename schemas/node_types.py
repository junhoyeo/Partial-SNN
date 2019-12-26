class NodeTypes:
  def __init__(self):
    self.INPUT = 0
    self.HIDDEN = 1
    self.OUTPUT = 2

  def get_repr(self, type_id: int):
    return ['INPUT', 'HIDDEN', 'OUTPUT'][type_id]

node_types = NodeTypes()
