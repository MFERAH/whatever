import torch as t
import torch.nn as nn
import torch.functional as F
import collections


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


class User_Defined(nn.Module):
    def __init__(self):
        super().__init__()
        self.custom_network = collections.OrderedDict()
        self.usr_define()

    def print_self(self):
        for sm in self.children():
            print(sm)

    @staticmethod
    def print_dict(dic):
        for item in dic.items():
            print(item)

    def usr_define(self):
        while 1:
            print("Please define your layer.")
            layer_type = input("layer type:")
            layer_name = input("layer name:")
            if layer_type == "conv":
                in_channels = int(input("in_channels:"))
                out_channels = int(input("out_channels:"))
                kernel_size = int(input("kernel_size:"))
                stride = 1
                padding = "valid"
                dilation = 1
                while 1:
                    instruction = input("stride={}, padding={}, dilation={}\nType in what you want to change"
                                        "(otherwise,type in 'ok'):".format(stride, padding, dilation))
                    if instruction == "ok":
                        break
                    elif instruction == "stride":
                        stride = int(input("stride:"))
                    elif instruction == "padding":
                        padding = input("padding:")
                    elif instruction == "dilation":
                        dilation = int(input("dilation:"))
                self.custom_network.update({layer_name: Conv2d(in_channels, out_channels, kernel_size, stride,
                                                               padding, dilation)})
            self.print_dict(self.custom_network)
            conti = input("Do you want to create next one?")
            if conti == "no":
                break
a = User_Defined()