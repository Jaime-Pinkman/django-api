import numpy
import dlib
import cv2


class Frame():
    """
    Основная задача поиск лиц на изображении.
    """

    def __init__(self, frame=None, path=None, cuda=False):
        super().__init__()
        self.newFrame(frame, path)
        self.preloadLibs()

    def newFrame(self, frame=None, path=None):
        if frame is not None:
            self.frame = frame
        else:
            if path is not None:
                stream = open(u'' + path, "rb")
                _bytes = bytearray(stream.read())
                numpyarray = numpy.asarray(_bytes, dtype=numpy.uint8)
                self.frame = cv2.imdecode(numpyarray, cv2.IMREAD_UNCHANGED)
            else:
                self.frame = None

        self.faces = None
        self.chosen = None

    def preloadLibs(self):
        self.sp = dlib.shape_predictor('../data/shape_predictor_68_face_landmarks.dat')
        self.facerec = dlib.face_recognition_model_v1('../data/dlib_face_recognition_resnet_model_v1.dat')
        self.detector = dlib.get_frontal_face_detector()

    def takeFaceRect(self):
        """
        Получаем координаты зоны лица

        rect -> num, name, left, top, width, height

        Получаем список лиц на изображении типа: вектор (пустой), квадрат в котором опредлено лицо

        Если на выходе None: На кадре не были обнаружены лица

        """
        self.chosen = None
        self.faces = None

        rezult = []  # {"face_descriptor": None, "rect": None}

        try:
            self.dets = self.detector(self.frame, 0)

            if len(self.dets) != 0:
                width = self.frame.shape[1]
                height = self.frame.shape[0]
                for k, d in enumerate(self.dets):
                    rect = [k, str(k), (d.left() + d.width() / 2) / width, (d.top() + d.height() / 2) / height,
                            d.width() / width, d.height() / height]
                    rezult.append({"face_descriptor": "", "rect": rect})
                self.faces = rezult
            else:
                self.faces = None
        except Exception as error:
            cv2.imwrite('errors_img/.png', self.frame)
            raise Exception(str(error))

    def rect_sqwr(self, rect):
        return rect[4] * rect[5]


    def takeBiggestFace(self):
        """
        Поиск нужного лица (наибольшего)
        """
        faces = self.faces
        if faces is not None:
            _max = 0
            for i in range(len(faces)):
                if self.rect_sqwr(faces[_max]['rect']) < self.rect_sqwr(faces[i]['rect']):
                    _max = i
            self.chosen = self.faces[_max]
        else:
            self.chosen = None
            raise Exception("Отсутствуют список лиц.")

    def takeVector(self):
        """
        Получаем вектор лица и добавляем в список в нужные места

        (numpy.ndarray (img), dlib.face_recognition_model_v1,
        dlib.shape_predictor, dlib.get_frontal_face_detector) -> [{dlib.vector, rect}]


        """
        self.takeFaceRect()

        if self.faces is not None:
            try:
                for k, d in enumerate(self.dets):
                    shape = self.sp(self.frame, d)
                    face_descriptor = self.facerec.compute_face_descriptor(self.frame, shape)
                    self.faces[k]["face_descriptor"] = face_descriptor
            except:
                raise Exception("Ошибка в определении вектора лица " + str(self.dets) + "/" + str(k))

