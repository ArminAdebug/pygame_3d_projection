import math

from utils import Vector3, Camera
from formulas import get_angle_between_vectors, distanse


def project_point_to_screen(point: Vector3, camera: Camera) -> tuple[float, float] | None:
    """returns 3d point position in 2d screen from left to right and up to down

    Args:
        point (Vector3): target 3d point
        camera (Camera): camera

    Returns:
        tuple[float, float] | None: returns point position aspect in screen or None
    """

    camera_forward = Vector3(0, 0, camera.range)
    horizenal_angle = camera.fov
    aspect = camera.screen_size[0] / camera.screen_size[1]

    vertical_angele = math.degrees(
        2 * math.atan(
            math.tan(math.radians(camera.fov / 2)) / aspect
        )
    )

    camera_to_point = point - camera.pos
    if get_angle_between_vectors(camera_forward, camera_to_point) > camera.fov / 2:
        print("not in FOV range")
        return None

    if abs(camera_to_point) > camera.range:
        print("not in camera range")
        return None



    horizenal_angle = get_angle_between_vectors(
        camera_forward,
        Vector3(camera_to_point.x, 0, camera_to_point.z)
    )

    vertical_angle = get_angle_between_vectors(
        camera_forward,
        Vector3(0, camera_to_point.y, camera_to_point.z)
    )

    horizenal_point_arc = math.radians(horizenal_angle) * abs(camera_to_point)
    vertical_point_arc = math.radians(vertical_angle) * abs(camera_to_point)

    horizenal_full_arc = math.radians(camera.fov) * abs(camera_to_point)
    vertical_full_arc = math.radians(camera.fov) * abs(camera_to_point)

    horizenal_aspect = 0 if not horizenal_full_arc else horizenal_point_arc / horizenal_full_arc
    vertical_aspect = 0 if not vertical_full_arc else vertical_point_arc / vertical_full_arc

    print(f"{horizenal_full_arc=} ; {horizenal_point_arc=}")
    print(f"{vertical_full_arc=} ; {vertical_point_arc=}")

    return (horizenal_aspect, vertical_aspect)
