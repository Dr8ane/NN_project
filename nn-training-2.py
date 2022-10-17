import numpy
from keras.models import Sequential
from keras.layers import Dense, Flatten, Activation
from keras.layers import Dropout
from keras.layers.convolutional import Convolution2D, MaxPooling2D
from keras.utils import np_utils

numpy.random.seed(42)



























# # Каталог с данными для обучения
# train_dir = 'images/for_NN/train'
# # Каталог с данными для проверки
# val_dir = 'images/for_NN/val'
# # Каталог с данными для тестирования
# test_dir = 'images/for_NN/test'
# # Размеры изображения
# img_width, img_height = 150, 150
# # Размерность тензора на основе изображения для входных данных в нейронную сеть
# # backend Tensorflow, channels_last
# # Количество эпох
# epochs = 10
# # Размер мини-выборки
# batch_size = 20
# # Количество изображений для обучения
# nb_train_samples = 17500
# # Количество изображений для проверки
# nb_validation_samples = 3750
# # Количество изображений для тестирования
# nb_test_samples = 3750


model = Sequential()
model.add(Convolution2D(32, 3, 3, border_mode='same', input_shape=(3, 32, 32), activation='relu'))

model.add(Convolution2D(32, 3, 3, activation='relu'))

model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))

model.add(Convolution2D(64, 3, 3, border_mode='same', activation='relu'))
model.add(Convolution2D(64, 3, 3, activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))

model.add(Flatten())
model.add(Dense(512, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(3, activation='softmax'))

model.compile(loss='categorical_crossentropy',
              optimizer='SGD',
              metrics=['accuracy'])

model.fit(X_train, Y_train,
          batch_size=32,
          nb_epoch = 25,
          validation_split=0.1,
          shuffle=True)

scores = model.evaluate(X_test, Y_test, verbose=0)
print("Точность работы на тестовых данных: %.2f%%" % (scores[1]*100))








# datagen = ImageDataGenerator(rescale=1. / 255)
# train_generator = datagen.flow_from_directory(
#     train_dir,
#     target_size=(img_width, img_height),
#     batch_size=batch_size,
#     class_mode='categorical')
# val_generator = datagen.flow_from_directory(
#     val_dir,
#     target_size=(img_width, img_height),
#     batch_size=batch_size,
#     class_mode='categorical')
# test_generator = datagen.flow_from_directory(
#     test_dir,
#     target_size=(img_width, img_height),
#     batch_size=batch_size,
#     class_mode='categorical')
# model.fit(
#     train_generator,
#     steps_per_epoch=nb_train_samples // batch_size,
#     epochs=epochs,
#     validation_data=val_generator,
#     validation_steps=nb_validation_samples // batch_size)
#
# model.save('contour_categorical.h5')
#
# scores = model.evaluate(test_generator, nb_test_samples // batch_size)
# print("Аккуратность на тестовых данных: %.2f%%" % (scores[1]*100))