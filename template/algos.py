import math

def find_targets_in_same_area(targets, separating_line_y, obstacles):
  """
  Finds the targets in the same area as the start point, given a separating line
  at a given Y-coordinate and a list of obstacles.

  Args:
    targets: A list of targets, represented as 2D tuples of integers.
    separating_line_y: The Y-coordinate of the separating line.
    obstacles: A list of obstacles, represented as lists of two points, each of
      which is a 2D tuple of integers.

  Returns:
    A list of targets in the same area as the start point, in the order given in
    the input, after filtering out all points that lie between two rays from the
    origin through the two points of the obstacle.
  """

  # Check if the separating line has Y-coordinate zero. If so, raise an error.
  if separating_line_y == 0:
    raise ValueError("The separating line cannot have Y-coordinate zero.")

  # Create a list to store the targets in the same area as the start point.
  targets_in_same_area = []

  # Iterate over the targets and add them to the list if they are in the same area
  # as the start point and do not lie between two rays from the origin through
  # the two points of any obstacle.
  for target in targets:
    if target[1] <= separating_line_y and not is_point_between_rays(target, obstacles):
      targets_in_same_area.append(target)

  # Return the list of targets in the same area as the start point, in the
  # order given in the input.
  return targets_in_same_area


def is_point_between_rays(point, obstacles):
  """
  Returns True if the point lies between two rays from the origin through the
  two points of any obstacle in the given list of obstacles, False otherwise.

  Args:
    point: A 2D tuple of integers, representing the point to check.
    obstacles: A list of obstacles, represented as lists of two points, each of
      which is a 2D tuple of integers.

  Returns:
    True if the point lies between two rays from the origin through the two
    points of any obstacle in the given list of obstacles, False otherwise.
  """

  for obstacle in obstacles:
    point_angle = math.atan2(point[1], point[0])
    ray_angle_1 = math.atan2(obstacle[0][1], obstacle[0][0])
    ray_angle_2 = math.atan2(obstacle[1][1], obstacle[1][0])

    print(point_angle)
    print("is between")
    print(ray_angle_1)
    print(ray_angle_2)

    if ray_angle_1 > 0:
        if ray_angle_1 <= point_angle <= ray_angle_2:
            return True
    else: 
        if ray_angle_2 >= point_angle >= ray_angle_1:
            return True
    

  return False

#print(is_point_between_rays(point=[0,5], obstacles = [[(10, 1), (-10, 1)]]))
obstacles = [[(-3, -5), (4, -6)]]

print(is_point_between_rays(point=[6,-6], obstacles = obstacles))
print(is_point_between_rays(point=[1,1], obstacles = obstacles))
print(is_point_between_rays(point=[-1,-4], obstacles = obstacles))
print(is_point_between_rays(point=[-5,-9], obstacles = obstacles))


