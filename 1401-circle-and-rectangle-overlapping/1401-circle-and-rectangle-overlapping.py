class Solution(object):
    def checkOverlap(self, radius, xCenter, yCenter, x1, y1, x2, y2):
        # Find the closest point on the rectangle to the circle center
        closestX = max(x1, min(xCenter, x2))
        closestY = max(y1, min(yCenter, y2))
        
        # Calculate the squared distance between the circle center and this closest point
        distanceX = xCenter - closestX
        distanceY = yCenter - closestY
        squaredDistance = (distanceX * distanceX) + (distanceY * distanceY)
        
        # Check if the distance is within the circle's radius
        return squaredDistance <= (radius * radius)
    
            