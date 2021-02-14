import numpy
import dlib
import cv2
import os
from api.settings import BASE_DIR


class FaceRecognizer:
    """Поиск лиц на изображении"""

    def __init__(self, file):
        self.frame = cv2.imdecode(numpy.fromstring(file.read(), numpy.uint8), cv2.IMREAD_UNCHANGED)
        self.sp = dlib.shape_predictor(os.path.join(BASE_DIR, 'data/shape_predictor_68_face_landmarks.dat'))
        self.face_rec = dlib.face_recognition_model_v1(
            os.path.join(BASE_DIR, 'data/dlib_face_recognition_resnet_model_v1.dat'))
        self.detector = dlib.get_frontal_face_detector()
        self.portrait = None
        self.compute_landmarks()

    def take_biggest_face(self):
        faces = self.detector(self.frame, 0)
        if len(faces) > 0:
            return max(faces, key=lambda x: x.area())
        else:
            raise Exception("Отсутствует список лиц.")

    def compute_landmarks(self):
        shape = self.sp(self.frame, self.take_biggest_face())
        self.portrait = self.face_rec.compute_face_descriptor(self.frame, shape)
