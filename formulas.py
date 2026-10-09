import math
from utils import Vector3

def get_angle_between_vectors(vector1 : Vector3, vector2 : Vector3) -> float:
    angle = math.degrees(
                math.acos((vector1.dot(vector2)) / (0.000000001 if (abs(vector1) * abs(vector2)) == 0 else (abs(vector1) * abs(vector2)))

                )
            )

    return angle

def distanse(point1: Vector3, point2: Vector3):
    point3 = (point1 - point2)
    return math.sqrt(point3.x ** 2 +
                     point3.y ** 2 +
                     point3.z ** 2)


def aspect_to_pos(aspect : tuple[float, float], screen_size : tuple[float, float]) -> tuple[float, float]:
    return (aspect[0] * screen_size[0] + screen_size[0] / 2,
            aspect[1] * screen_size[1] + screen_size[1] / 2)

# test
if __name__ == "__main__":
    a = Vector3(10, 0, 0)
    b = Vector3(-10, 0, 0)
    c = Vector3(0, 10, 0)

    d = Vector3(0.8660254, 0.5, 0)
    #print(get_angle_between_vectors(a, b)) # -> 180
    #print("-----")
    #print(get_angle_between_vectors(a, c)) # -> 90

    print(get_angle_between_vectors(a, d))

    #print(distanse(a, b))
    #print(distanse(a, c))
