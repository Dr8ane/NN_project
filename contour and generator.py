###################################################################################################################
# Перед началом, убедитесь, что все библиотеки установлены/обновлены                                              #
# В окне проекта обязательно должна быть папка images с 5 папками(for_NN, input, output, test_output, sours_blank)#
# В окне проекта обязательно должен лежать исходный вайл в пути images/input/input.bmp                            #
# В окне проекта обязательно должны лежать пустышки в пути images/sours_blank/   wall, window, door и т.д.        #
# pip install pillow для PIL(обработка изображений под нужный размер)                                             #
###################################################################################################################

import cv2
import imutils
import random
import os
from PIL import Image
import numpy as np
from keras.models import load_model
from keras.utils import load_img
from keras.utils import img_to_array
import json

# загрузка обученой нейросети
loaded_model = load_model('saved_models/contour_dense.hdf5')

# компиляция нейросети
loaded_model.compile(loss='sparse_categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

d = {0: 'дверь', 1: 'стена', 2: 'окно'}

# чтение изображения для работы(input)
image1 = cv2.imread('images/input/input.bmp')
# чтение вспомогательных изображений(sours_blank)
wall_mask = cv2.imread('images/sours_blank/wall.bmp')
door_wall_mask = cv2.imread('images/sours_blank/door.bmp')
window_wall_mask = cv2.imread('images/sours_blank/window.bmp')
# подготовка изображения для работы
gray = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
gray = cv2.GaussianBlur(gray, (3, 3), 0)

edges = cv2.Canny(gray, 10, 250)
cv2.imwrite("images/test_output/edges.jpg", edges)

kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (7, 7))
closed = cv2.morphologyEx(edges, cv2.MORPH_CLOSE, kernel)
cv2.imwrite("images/test_output/closed.jpg", closed)

cnts = cv2.findContours(closed.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)

# конст для циклов генерации
n = 0
t1 = 0
t2 = 0
# конст для выходных значений
number_element = 0
# конст для консольного вывода
total = 0
wall = 0
door_wall = 0
window_wall = 0
# конст для генерируемых элементов
nwall = 0
ndoor_wall = 0
nwindow_wall = 0
numb = 0

# прогонка для проверки(test_output)
for c in cnts:
    p = cv2.arcLength(c, True)
    approx = cv2.approxPolyDP(c, 0.02 * p, True)
    if len(approx) == 4:
        cv2.drawContours(image1, [approx], -1, (0, 0, 255), 4)
        total += 1
        wall += 1
    if len(approx) == 7:
        cv2.drawContours(image1, [approx], -1, (0, 255, 0), 4)
        total += 1
        door_wall += 1
    if len(approx) == 8:
        cv2.drawContours(image1, [approx], -1, (255, 0, 0), 4)
        total += 1
        window_wall += 1

# # генерация для обучения(train)
# while n < 875:
#     for c in cnts:
#         p = cv2.arcLength(c, True)
#         approx = cv2.approxPolyDP(c, 0.02 * p, True)
#         if len(approx) == 4:
#             cv2.drawContours(wall_mask, [approx], -1,
#                              (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), 4)
#             cv2.imwrite("images/for_NN/train/wall/wall" + str(nwall) + ".jpg", wall_mask)
#             wall_mask = cv2.imread('images/sours_blank/wall.bmp')
#             nwall += 1
#         if len(approx) == 7:
#             cv2.drawContours(door_wall_mask, [approx], -1,
#                              (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), 4)
#             cv2.imwrite("images/for_NN/train/door/door" + str(ndoor_wall) + ".jpg", door_wall_mask)
#             door_wall_mask = cv2.imread('images/sours_blank/door.bmp')
#             ndoor_wall += 1
#         if len(approx) == 8:
#             cv2.drawContours(window_wall_mask, [approx], -1,
#                              (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), 4)
#             cv2.imwrite("images/for_NN/train/window/window" + str(nwindow_wall) + ".jpg", window_wall_mask)
#             window_wall_mask = cv2.imread('images/sours_blank/window.bmp')
#             nwindow_wall += 1
#     n += 1
#
# # генерация для проверки(val)
# while t1 < 188:
#     for c in cnts:
#         p = cv2.arcLength(c, True)
#         approx = cv2.approxPolyDP(c, 0.02 * p, True)
#         if len(approx) == 4:
#             cv2.drawContours(wall_mask, [approx], -1,
#                              (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), 4)
#             cv2.imwrite("images/for_NN/val/wall/wall" + str(nwall) + ".jpg", wall_mask)
#             wall_mask = cv2.imread('images/sours_blank/wall.bmp')
#             nwall += 1
#         if len(approx) == 7:
#             cv2.drawContours(door_wall_mask, [approx], -1,
#                              (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), 4)
#             cv2.imwrite("images/for_NN/val/door/door" + str(ndoor_wall) + ".jpg", door_wall_mask)
#             door_wall_mask = cv2.imread('images/sours_blank/door.bmp')
#             ndoor_wall += 1
#         if len(approx) == 8:
#             cv2.drawContours(window_wall_mask, [approx], -1,
#                              (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), 4)
#             cv2.imwrite("images/for_NN/val/window/window" + str(nwindow_wall) + ".jpg", window_wall_mask)
#             window_wall_mask = cv2.imread('images/sours_blank/window.bmp')
#             nwindow_wall += 1
#     t1 += 1
#
# # генерация для тестов(test)
# while t2 < 188:
#     for c in cnts:
#         p = cv2.arcLength(c, True)
#         approx = cv2.approxPolyDP(c, 0.02 * p, True)
#         if len(approx) == 4:
#             cv2.drawContours(wall_mask, [approx], -1,
#                              (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), 4)
#             cv2.imwrite("images/for_NN/test/wall/wall" + str(nwall) + ".jpg", wall_mask)
#             wall_mask = cv2.imread('images/sours_blank/wall.bmp')
#             nwall += 1
#         if len(approx) == 7:
#             cv2.drawContours(door_wall_mask, [approx], -1,
#                              (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), 4)
#             cv2.imwrite("images/for_NN/test/door/door" + str(ndoor_wall) + ".jpg", door_wall_mask)
#             door_wall_mask = cv2.imread('images/sours_blank/door.bmp')
#             ndoor_wall += 1
#         if len(approx) == 8:
#             cv2.drawContours(window_wall_mask, [approx], -1,
#                              (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), 4)
#             cv2.imwrite("images/for_NN/test/window/window" + str(nwindow_wall) + ".jpg", window_wall_mask)
#             window_wall_mask = cv2.imread('images/sours_blank/window.bmp')
#             nwindow_wall += 1
#     t2 += 1


data = {}
data['element'] = []


resize_x_to_min = 150
resize_y_to_min = 150

directory = 'images/output/'

pos = None
# выходные значения(output)
for c in cnts:
    p = cv2.arcLength(c, True)
    approx = cv2.approxPolyDP(c, 0.02 * p, True)
    if len(approx) == 4:
        cv2.drawContours(wall_mask, [approx], -1, (0, 0, 0), 4)
        cv2.imwrite("images/output/elements" + str(number_element) + ".jpg", wall_mask)
        wall_mask = cv2.imread('images/sours_blank/wall.bmp')

        pos = approx
        pos1 = pos[0]
        pos11 = pos1[0]
        x1 = pos11[0]
        y1 = pos11[1]

        pos2 = pos[1]
        pos21 = pos2[0]
        x2 = pos21[0]
        y2 = pos21[1]

        pos3 = pos[2]
        pos31 = pos3[0]
        x3 = pos31[0]
        y3 = pos31[1]

        pos4 = pos[3]
        pos41 = pos4[0]
        x4 = pos41[0]
        y4 = pos41[1]

        if((y2-y1)>(x3-x2)):
            length = y2-y1
            width = x3-x2
        else:
            length = x3 - x2
            width = y2-y1

        with os.scandir(path=directory) as it:
            for entry in it:
                img_obj = Image.open(directory + entry.name)
                width_size = height_size = 0
                delta = resize_x_to_min / float(img_obj.size[0])
                width_size = int(float(img_obj.size[0]) * delta)
                height_size = int(float(img_obj.size[1]) * delta)
                delta = resize_y_to_min / float(img_obj.size[1])
                width_size = int(float(img_obj.size[0]) * delta)
                height_size = int(float(img_obj.size[1]) * delta)
                img_obj = img_obj.resize((width_size, height_size), Image.ANTIALIAS)
                img_obj.save(directory + entry.name)

        img_path = 'images/output/elements' + str(number_element) + '.jpg'
        img = load_img(img_path, target_size=(150, 150))

        y = img_to_array(img)
        y = y / 255
        y = np.expand_dims(y, axis=0)

        prediction = loaded_model.predict(y)

        for value in range(len(prediction)):
            prediction = prediction[value]

        prediction = np.argmax(prediction)
        print(d[prediction])

        #

        data['element'].append({
            'class': d[prediction],
            'X': x1,
            'Y': y1,
            'length': length,
            'width': width,
        })

        number_element += 1

    if len(approx) == 7:
        cv2.drawContours(door_wall_mask, [approx], -1, (0, 0, 0), 4)
        cv2.imwrite("images/output/elements" + str(number_element) + ".jpg", door_wall_mask)
        door_wall_mask = cv2.imread('images/sours_blank/door.bmp')
        number_element += 1
    if len(approx) == 8:
        cv2.drawContours(window_wall_mask, [approx], -1, (0, 0, 0), 4)
        cv2.imwrite("images/output/elements" + str(number_element) + ".jpg", window_wall_mask)
        window_wall_mask = cv2.imread('images/sours_blank/window.bmp')
        number_element += 1


with open('data.txt', 'w') as outfile:
    json.dump(data, outfile)
print(pos)
print(pos1)
print(pos11)
print(x1)
print(y1)
print(x2)
print(y2)
print(x3)
print(y3)
print(x4)
print(y4)
# проверка для консоли
print('total = ', total)
print('wall(red) = ', wall)
print('door_wall(green) = ', door_wall)
print('window_wall(blue) = ', window_wall)

# вывод для проверки(test_output)
cv2.imwrite("images/test_output/test_final.jpg", image1)
