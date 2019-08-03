import json
import sys
import os
from snippets.import_statements import import_statements


def generate_init_snippet(layers, tabs = 8, tab_character = " "):
    init_snippet = ""
    for single_layer in layers:

        module = single_layer["module"]
        activation = single_layer["activation"] if "activation" in single_layer.keys() else None

        init_snippet += "{tabs}self.{identifier} = nn.Sequential({type}{activation})\n".format(
            tabs = tabs * tab_character,
            identifier = single_layer["identifier"],
            type = module["type"] + ("({})".format(module["parameter"]).replace("[","(").replace("]",")") if "parameter" in module.keys() else "()"),
            activation = (", " + activation["type"] + ("({})".format(activation["parameter"].replace("[","(").replace("]",")") if "parameter" in activation.keys() else ""))) if activation != None else ""
        )
    return init_snippet



def generate_forward_snippet(output_identifier, layers, tabs = 8, tab_character = " "):
    forward_snippet = ""
    for single_layer in layers:
        forward_snippet += "{tabs}{identifier} = self.{identifier}({input})\n".format(
            tabs = tabs * tab_character,
            identifier = single_layer["identifier"],
            input = single_layer["in"]
            )
    forward_snippet += "{tabs}return {output_identifier}".format(output_identifier=output_identifier,tabs=tabs * tab_character)
    return forward_snippet
    


if __name__ == '__main__':

    with open(sys.argv[1]) as file:
        
        json_data=json.loads(file.read())

        generated_text = r"""{import_statements}

class {module_name}(nn.Module):
    def __init__(self):
        super().__init__()
{init_snippet}
            
    def forward(self, INPUT):
{forward_snippet}

        """.format(
            import_statements = import_statements,
            module_name = json_data["module_name"],
            init_snippet = generate_init_snippet(json_data["layers"]),
            forward_snippet = generate_forward_snippet(json_data["output_identifier"], json_data["layers"])
            )
        
        with open(os.path.splitext(sys.argv[1])[0] + ".py", "w") as generated_code:
            generated_code.write(generated_text)


# from copy_snippet import copy

# with open("fc_mnist.json") as f:
#     text = f.read()
#     dic = json.loads(text)
#     print(dic)
#     with open('generated_code.py', 'w') as code:
#         c = copy(code)
#         c.copy_code("import")
#         c.copy_code("User_Defined_1", dic["module_name"])
#         for layer in dic["layers"]:
#             if layer["module"]["type"] == "Linear":
#                 if "activation" in layer.keys():
#                     c.copy_code("layers/layer_init_1",
#                                 layer["identifier"],
#                                 c.read_code("layers/fc_init",
#                                             layer["module"]["parameter"][0],
#                                             layer["module"]["parameter"][1]),
#                                 c.read_code("layers/activation_init",
#                                             layer["activation"]["type"]))
#                 else:
#                     c.copy_code("layers/layer_init_2",
#                                 layer["identifier"],
#                                 c.read_code("layers/fc_init",
#                                             layer["module"]["parameter"][0],
#                                             layer["module"]["parameter"][1]))
#         c.copy_code("User_Defined_2", dic["layers"][0]["in"])
#         for layer in dic["layers"]:
#             c.copy_code("layers/using", layer["identifier"], layer["identifier"], layer["in"])
#         c.copy_code("User_Defined_3", dic["layers"][-1]["identifier"])
