def updatePosition(self, dx, dy):
    self.x += dx
    self.y += dy

    newPoints = []
    for (x,y) in self.points:
       newPoints.append((x+dx, y+dy))

    self.points = newPoints

def rotate_polygon(origin, points, angle) :
    angle = math.radians(angle)
    rotated_polygon = []

    for point in points :
        temp_point = point[0] - origin[0] , point[1] - origin[1]
        temp_point = (temp_point[0] * math.cos(angle) - temp_point[1] * math.sin(angle),
                      temp_point[0] * math.sin(angle) + temp_point[1] * math.cos(angle))
        temp_point = temp_point[0] + origin[0], temp_point[1] + origin[1]
        rotated_polygon.append(temp_point)

    return rotated_polygon

