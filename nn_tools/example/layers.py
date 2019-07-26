import torch
import torch.nn as nn
import torch.nn.functional as F


def padding_same_2d(kernel_size, dilation):
    return int((kernel_size - 1) / 2 + dilation - 1)


def Conv2d(in_channels, out_channels, kernel_size, stride=1,
           padding="valid", dilation=1):
    assert padding == "same" or padding == "valid"
    if padding == "same":
        p = padding_same_2d(kernel_size, dilation)
    elif padding == "valid":
        p = 0
    return nn.Conv2d(in_channels, out_channels, kernel_size, stride, p, dilation)


class UserDefined(nn.Module):
    def __init__(self):
        super().__init__()
        # add your layers here

    def forward(self, x):
        pass
        # create your net here
