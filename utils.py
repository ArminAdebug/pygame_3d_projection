import math


class Vector3:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __mul__(self, other: "Vector3") -> "Vector3":
        if not isinstance(other, Vector3):
            raise TypeError("non-vector3 is not supported.")

        return Vector3(self.x * other.x,
                       self.y * other.y,
                       self.z * other.z)

    def __sub__(self, other):
        if not isinstance(other, Vector3):
            raise TypeError("non-vector3 is not supported.")

        return Vector3(self.x - other.x,
                       self.y - other.y,
                       self.z - other.z)

    def __add__(self, other):
        if not isinstance(other, Vector3):
            raise TypeError("non-vector3 is not supported.")

        return Vector3(self.x + other.x,
                       self.y + other.y,
                       self.z + other.z)

    def dot(self, other: "Vector3") -> float:
        if not isinstance(other, Vector3):
            raise TypeError("non-vector3 is not supported.")

        return self.x * other.x + self.y * other.y + self.z * other.z

    def __abs__(self):
        return math.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)


class Camera:
    def __init__(self, fov: float, range: float, screen_size: tuple[float, float]):
        self.pos = Vector3(0, 0, 0)
        self.fov = fov
        self.range = range
        self.screen_size = screen_size
