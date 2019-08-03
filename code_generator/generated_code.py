import torch as t
import torch.nn as nn
import torchvision.datasets
import torch.utils.data.dataloader
import torchvision.transforms as transforms
from additional_part import Conv2d

class My_fc(nn.Module):
    def __init__(self):
        super().__init__()
        self.fc1 = t.nn.Sequential(t.nn.Linear(784, 500), t.nn.LeakyReLU())
        self.fc2 = t.nn.Sequential(t.nn.Linear(500, 200), t.nn.LeakyReLU())
        self.fc3 = t.nn.Sequential(t.nn.Linear(200, 50), t.nn.LeakyReLU())
        self.fc4 = t.nn.Linear(50, 10)

    def forward(self, INPUT):
        fc1 = self.fc1(INPUT)
        fc2 = self.fc2(fc1)
        fc3 = self.fc3(fc2)
        fc4 = self.fc4(fc3)
        return fc4

