class calculator:
    """Classcalculator for 2 vectors: dot product, addition, subtraction"""

    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        """Dot product of two vectors."""
        result = sum(x * y for x, y in zip(V1, V2))
        print(f"Dot product is: {result}")

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        """Addition of two vectors."""
        result = [float(x + y) for x, y in zip(V1, V2)]
        print(f"Add Vector is : {result}")

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        """Subtraction of two vectors."""
        result = [float(x - y) for x, y in zip(V1, V2)]
        print(f"Sous Vector is: {result}")
