import numpy
import dlib
import cv2
import os
from api.settings import BASE_DIR


class FaceRecognizer:
    """Основная задача поиск лиц на изображении"""

    def __init__(self, file):
        self.frame = cv2.imdecode(numpy.fromstring(file.read(), numpy.uint8), cv2.IMREAD_UNCHANGED)
        self.preloadLibs()
        self.portrait = None
        self.compute_landmarks()

    def preloadLibs(self):
        self.sp = dlib.shape_predictor(os.path.join(BASE_DIR, 'data/shape_predictor_68_face_landmarks.dat'))
        self.facerec = dlib.face_recognition_model_v1(
            os.path.join(BASE_DIR, 'data/dlib_face_recognition_resnet_model_v1.dat'))
        self.detector = dlib.get_frontal_face_detector()

    def take_biggest_face(self):
        """Поиск нужного лица (наибольшего)"""
        faces = self.detector(self.frame, 0)
        if len(faces) > 0:
            return max(faces, key=lambda x: x.area())
        else:
            self.biggest = None
            raise Exception("Отсутствует список лиц.")

    def compute_landmarks(self):
        shape = self.sp(self.frame, self.take_biggest_face())
        self.portrait = self.facerec.compute_face_descriptor(self.frame, shape)
