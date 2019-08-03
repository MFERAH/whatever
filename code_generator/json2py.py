import json
from copy_snippet import copy

with open("fc_mnist.json") as f:
    text = f.read()
    dic = json.loads(text)
    print(dic)
    with open('generated_code.py', 'w') as code:
        c = copy(code)
        c.copy_code("import")
        c.copy_code("User_Defined_1", dic["module_name"])
        for layer in dic["layers"]:
            if layer["module"]["type"] == "Linear":
                if "activation" in layer.keys():
                    c.copy_code("layers/layer_init_1",
                                layer["identifier"],
                                c.read_code("layers/fc_init",
                                            layer["module"]["parameter"][0],
                                            layer["module"]["parameter"][1]),
                                c.read_code("layers/activation_init",
                                            layer["activation"]["type"]))
                else:
                    c.copy_code("layers/layer_init_2",
                                layer["identifier"],
                                c.read_code("layers/fc_init",
                                            layer["module"]["parameter"][0],
                                            layer["module"]["parameter"][1]))
        c.copy_code("User_Defined_2", dic["layers"][0]["in"])
        for layer in dic["layers"]:
            c.copy_code("layers/using", layer["identifier"], layer["identifier"], layer["in"])
        c.copy_code("User_Defined_3", dic["layers"][-1]["identifier"])
