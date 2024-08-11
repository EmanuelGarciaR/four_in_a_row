import numpy as np
class Dimension:
    def __init__(self, dimension: int):
        if dimension not in [4, 5, 6]:  # Verificar dimensión en el rango permitido
            raise ValueError("Dimensión no permitida. Debe ser 4, 5 o 6.")
        self.dimension = dimension