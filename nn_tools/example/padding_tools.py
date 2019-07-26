def padding_same_2d(kernel_size, dilation):
    """
    only for the condition that layer's stride = 1
    :param input_size: input_size
    :param kernel_size: kernel_size
    :param dilation: dilation
    :return: padding param
    """
    return (kernel_size - 1) / 2 + 2 * dilation


