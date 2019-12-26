from schemas import TrainData
from network import model, nodes

from itertools import count
from time import sleep

train: list = [
  TrainData((0, 1), 1),
  TrainData((1, 0), 1),
  TrainData((0, 0), 0),
  TrainData((1, 1), 0),
]

for node in model.layers[0]:
  node.spike()

max_time = 500000
for time in count(1):
  if time == max_time:
    print(False)
    exit(0)

  for node in nodes:
    if node.next >= time:
      if node.spike(time):
        print(True)
        exit(0)
