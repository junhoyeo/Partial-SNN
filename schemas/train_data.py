class TrainData:
  def __init__(self, x: int, y: int):
    self.x: tuple(int, int) = x
    self.y: int = y

  def __repr__(self):
    return f'<TrainData x: {self.x}, y: {self.y}>'
