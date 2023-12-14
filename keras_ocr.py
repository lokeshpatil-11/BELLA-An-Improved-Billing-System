import matplotlib.pyplot as plt
import keras_ocr
pipeline = keras_ocr.pipeline.Pipeline()
images = [
    keras_ocr.tools.read(images) for images in[
        '/test1.jpg'
    ]

]
prediction = pipeline.recognize(images)
print(prediction)