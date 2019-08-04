import torch as t
import torch.nn as nn
import torchvision.datasets
import torch.utils.data.dataloader
import torchvision.transforms as transforms
from additional_part import Conv2d


class simple_conv(nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = nn.Sequential(nn.Conv2d(1, 20, 5), nn.LeakyReLU())
        self.conv2 = nn.Sequential(nn.Conv2d(20, 20, 5), nn.LeakyReLU())

            
    def forward(self, INPUT):
        conv1 = self.conv1(INPUT)
        conv2 = self.conv2(conv1)
        return conv2

        