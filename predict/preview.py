from keras.models import load_model
import numpy as np
import csv
import cv2


class VideoCamera():
    def __init__(self):
        self.video = cv2.VideoCapture(1)

    def __del__(self):
        self.video.release()

    def get_image(self):
        _, image = self.video.read()
        return image

    def get_frame(self):
        image = self.get_image()
        image = cv2.flip(image, 1)
        image = cv2.rectangle(image, (192, 112), (448, 368), (0, 255, 0), 3)
        ret, jpeg = cv2.imencode('.jpg', image)
        return jpeg.tobytes()


class Model():
    def __init__(self):
        self.categories = self.loadCategories()
        self.model = load_model('predict/static/Gesture25.h5')
        self.model.compile(
            optimizer='adam', loss="sparse_categorical_crossentropy", metrics=["accuracy"])

    def loadCategories(self):
        with open("predict/static/Categories.csv", newline='') as f:
            reader = csv.reader(f)
            ctg = list(reader)

        return ctg[0]

    def predict(self, image):
        frame = image

        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        frame = frame[112:368, 192:448]
        frame = cv2.resize(frame, (64, 64))
        frame = np.reshape(frame, (1, 64, 64, 1))
        frame = frame.astype("float32")
        frame = frame / 255.0

        max_value = np.argmax(self.model.predict(frame))

        return self.categories[max_value]

        # from datasetToArray import loadCategories
        # from keras.models import load_model
        # import tensorflow as tf

        # import numpy as np
        # import cv2

        # def predict(image):

        #     print(categories[np.argmax(model.predict(image))])

        # def run():

        #     while True:

        #         _, frame = cam.read()

        #         frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        #         frame = cv2.flip(frame, 1)
        #         frame_crop = frame[112:368, 192:448]
        #         cv2.imshow("Frame Crop", cv2.resize(frame_crop, (768, 768)))

        #         frame_crop = cv2.resize(frame_crop, (64, 64))
        #         frame_crop = np.reshape(frame_crop, (1, 64, 64, 1))
        #         frame_crop = np.astype("float32")
        #         frame_crop = frame_crop / 255.0

        #         predict(frame_crop)

        #         q = ord("q")

        #         if cv2.waitKey(1) == q:
        #             break

        #     cam.release()
        #     cv2.destroyAllWindows()

        # if name == "main":

        #     cam = cv2.VideoCapture(1)

        #     model = load_model('Gesture5.h5')
        #     model.compile(optimizer='adam',
        #                   loss="sparse_categorical_crossentropy",
        #                   metrics=["accuracy"])

        #     categories = loadCategories()

        #     run()
