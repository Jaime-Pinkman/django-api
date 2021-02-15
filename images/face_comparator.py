from scipy.spatial import distance


class FaceComparator:
    """Сравнивает facial landmarks между собой через евклидово расстояние"""

    def __init__(self, portrait, faces, threshold=0.6):
        self.threshold = threshold
        self.portrait = portrait
        self.faces = faces

    @staticmethod
    def find_distance(old_face, new_face):
        return distance.euclidean(list(map(float, old_face)), new_face)

    def find_similar_face(self):
        return min([FaceComparator.find_distance(face.portrait.split(','), self.portrait) for face in self.faces])

    def check_if_the_same_person(self):
        return self.find_similar_face() < self.threshold
