import torch as t
import torch.nn as nn
import torchvision.datasets
import torch.utils.data.dataloader
import torchvision.transforms as transforms
from additional_part import Conv2d


class My_fc(nn.Module):
    def __init__(self):
        super().__init__()
        self.fc1 = nn.Sequential(Linear((784, 500)), LeakyReLU())
        self.fc2 = nn.Sequential(Linear((500, 200)), LeakyReLU())
        self.fc3 = nn.Sequential(Linear((200, 50)), LeakyReLU())
        self.fc4 = nn.Sequential(Linear((50, 10)))

            
    def forward(self, INPUT):
        fc1 = self.fc1(INPUT)
        fc2 = self.fc2(fc1)
        fc3 = self.fc3(fc2)
        fc4 = self.fc4(fc3)
        return fc4

        