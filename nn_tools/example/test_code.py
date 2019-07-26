import torch as t
import torch.nn as nn
from torch.autograd import Variable
from layers import Conv2d

x = t.randn(1, 3, 50, 50)

y = Conv2d(3, 4, 5, padding="fuck")(x)
print(y.size())
