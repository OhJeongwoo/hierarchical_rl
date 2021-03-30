import math

def clipping(x, threshold):
    threshold = abs(threshold)
    if abs(x) < threshold:
        return x
    return threshold * x / abs(x)