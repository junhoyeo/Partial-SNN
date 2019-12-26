from schemas import TrainData
from network import model

train: list = [
  TrainData((0, 1), 1),
  TrainData((1, 0), 1),
  TrainData((0, 0), 0),
  TrainData((1, 1), 0),
]

for node in model.layers[0]:
  node.spike()
