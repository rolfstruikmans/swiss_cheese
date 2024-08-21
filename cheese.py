import numpy as np
import random
import math

class Hole:
    def __init__(self, radius, center):
        self.radius = radius
        self.center = np.array(center) # whatever center is, turn it into a numpy.ndarray
        self.ndim = self.center.size
        self.nball_constant = self._nball_constant(self.ndim)
        self.volume = 0

    def _nball_constant(self, n):
        if n == 0:
            return 1
        if n == 1:
            return 2
        return (2*math.pi/n)*self._nball_constant(n-2)

    @property
    def volume(self):
        self.volume = self.nball_constant*math.pow(self.radius, self.ndim)
        return self._volume

    @volume.setter
    def volume(self, value):
        self._volume = value

    def contains(self, object):
        if type(object) == list:
            object = np.array(object)
        if type(object) == np.ndarray:
            point = object
            dist = point - self.center
            if np.linalg.norm(dist) < self.radius:
                return True
            return False
        if type(object) == Hole:
            other_hole = object
            center_to_center = other_hole.center - self.center
            dist = np.linalg.norm(center_to_center)
            if (dist + other_hole.radius) < self.radius:
                return True
            return False
    def intersects(self, hole):
        center_to_center = hole.center - self.center
        dist = np.linalg.norm(center_to_center)
        disjunct = dist > (self.radius + hole.radius)
        if disjunct or self.contains(hole) or hole.contains(self):
            return False
        return True

    def __str__(self):
        return f"Hole(radius={self.radius}, center={self.center})"

class SwissCheese:
    def __init__(self, num_points=10000, dimensions=(1, 1, 1), max_hole_perc=0.3, hole_radius_min=0.05, hole_radius_max=0.1):
        self.num_points = num_points
        self.dimensions = dimensions
        self.ndim = len(self.dimensions)
        self.volume = abs(math.prod(self.dimensions))
        self.total_hole_volume = 0
        self.holes = []
        self.num_holes = 0
        self.max_hole_perc = max_hole_perc
        self.hole_radius_min = hole_radius_min
        self.hole_radius_max = hole_radius_max

        self.holes = self._make_holes()
        self.data = self._make_swiss_cheese()

    @property
    def num_holes(self):
        self.num_holes = len(self.holes)
        return self._num_holes

    @num_holes.setter
    def num_holes(self, value):
        self._num_holes = value


    def _random_point(self):
        point = []
        for x in self.dimensions:
            point.append(random.uniform(0,x))
        return point

    def _point_in_any_hole(self, point):
        # check if point falls within any of the holes
        for hole in self.holes:
            if hole.contains(point):
                return True
        return False

    def _make_holes(self):
        hole_volume_threshold = self.volume*self.max_hole_perc
        holes = []
        include = True
        while self.total_hole_volume < hole_volume_threshold:
            center = self._random_point()
            radius = random.uniform(self.hole_radius_min, self.hole_radius_max)
            hole = Hole(radius, center)
            #check whether the hole to be added is contained in or contains any of the already existing holes.
            for existing_hole in holes:
                if existing_hole.contains(hole) or hole.contains(existing_hole):
                    include = False
                    break
            if include:
                self.total_hole_volume += hole.volume
                holes.append(hole)
            include = True
        return holes

    def _make_swiss_cheese(self):
        swiss_cheese = np.empty((self.num_points, self.ndim)) # generate a random array with 'num_points' number of 'ndim' points
        for i in range(self.num_points):
            point = self._random_point()
            while self._point_in_any_hole(point):
                point = self._random_point()    # generate new random point and check if we can add it
            swiss_cheese[i] = point
        return swiss_cheese

    def __str__(self):
        return f"SwissCheese(size={self.size}, dimensions={self.dimensions}, max_hole_perc={self.max_hole_perc}, hole_radius_min={self.hole_radius_min}, hole_radius_max={self.hole_radius_max})"
