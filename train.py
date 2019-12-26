from schemas import TrainData
from network import model, nodes

from itertools import count
from time import sleep
from pprint import pprint
import matplotlib.pyplot as plt

train_list: list = [
  TrainData((0, 1), 1),
  TrainData((1, 0), 1),
  TrainData((0, 0), 0),
  TrainData((1, 1), 0),
]

train = train_list[0]

model.layers[0][0].theta = train.x[0] * 0.15
model.layers[0][1].theta = train.x[1] * 0.15

for node in model.layers[0]:
  node.spike()

max_time = 6000
for time in count(1):
  print('Frame: ', time)

  if time == max_time:
    print(False)
    break

  ended = False
  for node in nodes:
    if node.next >= time:
      ended = node.spike(time)
      if ended:
        print(True)
        break

  if ended:
    break

pprint(nodes)

plt.scatter(
  [node.x for node in nodes],
  [node.y for node in nodes],
)
plt.show()
