class TrainData:
  def __init__(self, x, y):
    self.x: tuple(int, int) = x
    self.y: int = y

  def __repr__(self):
    return f'<TrainData x: {self.x}, y: {self.y}>'

train: list = [
  TrainData((0, 1), 1),
  TrainData((1, 0), 1),
  TrainData((0, 0), 0),
  TrainData((1, 1), 0),
]
