import numpy
import cv2

from size import getSize

size = getSize()


def renderImage(solution):
    mazeSolution = solution * 70
    maze = numpy.reshape(mazeSolution, (size, size))
    im_g = cv2.imwrite("GeneratedMaze.jpg", maze)
