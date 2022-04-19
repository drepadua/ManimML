from manim import *
from ..layers import connective_layers_list

def get_connective_layer(input_layer, output_layer):
    """
        Deduces the relevant connective layer
    """
    connective_layer = None
    for connective_layer_class in connective_layers_list:
        input_class = connective_layer_class.input_class
        output_class = connective_layer_class.output_class
        if isinstance(input_layer, input_class) \
            and isinstance(output_layer, output_class):
            connective_layer = connective_layer_class(input_layer, output_layer)

    if connective_layer is None:
        raise Exception(f"Unrecognized class pair {input_layer.__class__.__name__}" + \
                        " and {output_layer.__class__.__name__}")
                        
    return connective_layer
