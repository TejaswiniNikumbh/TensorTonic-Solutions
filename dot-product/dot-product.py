import numpy as np

def dot_product(x: list, y: list) -> float:
    """
    Returns the dot product as a float.
    """
    dot_product = 0.0
    for i in range(len(x)):
        p = x[i]*y[i]
        dot_product += p
    return float(dot_product)