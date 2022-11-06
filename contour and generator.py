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
# from keras.models import load_model
# from keras.utils import load_img
# from keras.utils import img_to_array
import json

#

def write(data, filename):
    data = json.dumps(data)
    data = json.loads(str(data))
    with open(filename, 'w', encoding = 'utf-8') as file:
        json.dump(data, file, indent = 4)

def read(filename):
    with open(filename, 'r', encoding = 'utf-8') as file:
        return json.load(file)

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
        cv2.drawContours(image1, [approx], -1, (0, 0, 255), 0)
        total += 1
        wall += 1
    if len(approx) == 7:
        cv2.drawContours(image1, [approx], -1, (0, 255, 0), 0)
        total += 1
        door_wall += 1
    if len(approx) == 8:
        cv2.drawContours(image1, [approx], -1, (255, 0, 0), 0)
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

# resize_x_to_min = 150
# resize_y_to_min = 150
#
# directory = 'images/output/'
#
# class Element:
#     def __init__(self):
#         self.Class = _class
#         self.X = _x
#         self.Y = _y
#         self.Length = length
#         self.Width = width
#
# data = {
#     "elements" : []
# }

# pos = None
# # выходные значения(output)
# for c in cnts:
#     p = cv2.arcLength(c, True)
#     approx = cv2.approxPolyDP(c, 0.02 * p, True)
#     if len(approx) == 4:
#         cv2.drawContours(wall_mask, [approx], -1, (0, 0, 0), 4)
#         cv2.imwrite("images/output/elements" + str(number_element) + ".jpg", wall_mask)
#         wall_mask = cv2.imread('images/sours_blank/wall.bmp')
#
#         pos = approx
#         pos1 = pos[0]
#         pos11 = pos1[0]
#         x11 = pos11[0]
#         y11 = pos11[1]
#         x1 = int(x11)
#         y1 = int(y11)
#
#         pos2 = pos[1]
#         pos21 = pos2[0]
#         x21 = pos21[0]
#         y21 = pos21[1]
#         x2 = int(x21)
#         y2 = int(y21)
#
#         pos3 = pos[2]
#         pos31 = pos3[0]
#         x31 = pos31[0]
#         y31 = pos31[1]
#         x3 = int(x31)
#         y3 = int(y31)
#
#         pos4 = pos[3]
#         pos41 = pos4[0]
#         x41 = pos41[0]
#         y41 = pos41[1]
#         x4 = int(x41)
#         y4 = int(y41)
#
#         list_x = [x1, x2, x3, x4]
#         list_y = [y1, y2, y3, y4]
#
#         max_x = max(list_x)
#         min_x = min(list_x)
#
#         max_y = max(list_y)
#         min_y = min(list_y)
#
#         if ((max_y - min_y) > (max_x - min_x)):
#             length = max_y - min_y
#             width = max_x - min_x
#             _x = max_x - width / 2
#             _y = max_y - length / 2
#         else:
#             length = max_x - min_x
#             width = max_y - min_y
#             _x = max_x - length / 2
#             _y = max_y - width / 2
#
#
#         with os.scandir(path=directory) as it:
#             for entry in it:
#                 img_obj = Image.open(directory + entry.name)
#                 width_size = height_size = 0
#                 delta = resize_x_to_min / float(img_obj.size[0])
#                 width_size = int(float(img_obj.size[0]) * delta)
#                 height_size = int(float(img_obj.size[1]) * delta)
#                 delta = resize_y_to_min / float(img_obj.size[1])
#                 width_size = int(float(img_obj.size[0]) * delta)
#                 height_size = int(float(img_obj.size[1]) * delta)
#                 img_obj = img_obj.resize((width_size, height_size), Image.ANTIALIAS)
#                 img_obj.save(directory + entry.name)
#
#         img_path = 'images/output/elements' + str(number_element) + '.jpg'
#         img = load_img(img_path, target_size=(150, 150))
#
#         y = img_to_array(img)
#         y = y / 255
#         y = np.expand_dims(y, axis=0)
#
#         prediction = loaded_model.predict(y)
#
#         for value in range(len(prediction)):
#             prediction = prediction[value]
#
#         prediction = np.argmax(prediction)
#
#         _class = d[prediction]
#
#         data['elements'].append(Element().__dict__)
#
#         number_element += 1
#
#     if len(approx) == 7:
#         cv2.drawContours(door_wall_mask, [approx], -1, (0, 0, 0), 4)
#         cv2.imwrite("images/output/elements" + str(number_element) + ".jpg", door_wall_mask)
#         door_wall_mask = cv2.imread('images/sours_blank/door.bmp')
#         pos = approx
#         pos1 = pos[0]
#         pos11 = pos1[0]
#         x11 = pos11[0]
#         y11 = pos11[1]
#         x1 = int(x11)
#         y1 = int(y11)
#
#         pos2 = pos[1]
#         pos21 = pos2[0]
#         x21 = pos21[0]
#         y21 = pos21[1]
#         x2 = int(x21)
#         y2 = int(y21)
#
#         pos3 = pos[2]
#         pos31 = pos3[0]
#         x31 = pos31[0]
#         y31 = pos31[1]
#         x3 = int(x31)
#         y3 = int(y31)
#
#         pos4 = pos[3]
#         pos41 = pos4[0]
#         x41 = pos41[0]
#         y41 = pos41[1]
#         x4 = int(x41)
#         y4 = int(y41)
#
#         pos5 = pos[4]
#         pos51 = pos5[0]
#         x51 = pos51[0]
#         y51 = pos51[1]
#         x5 = int(x51)
#         y5 = int(y51)
#
#         pos6 = pos[5]
#         pos61 = pos6[0]
#         x61 = pos61[0]
#         y61 = pos61[1]
#         x6 = int(x61)
#         y6 = int(y61)
#
#         pos7 = pos[6]
#         pos71 = pos7[0]
#         x71 = pos71[0]
#         y71 = pos71[1]
#         x7 = int(x71)
#         y7 = int(y71)
#
#         list_x = [x1, x2, x3, x4, x5, x6, x7]
#         list_y = [y1, y2, y3, y4, y5, y6, y7]
#
#         max_x = max(list_x)
#         min_x = min(list_x)
#
#         max_y = max(list_y)
#         min_y = min(list_y)
#
#         if ((max_y - min_y) > (max_x - min_x)):
#             length = max_y - min_y
#             width = max_x - min_x
#             _x = max_x - width/2
#             _y = max_y - length/2
#         else:
#             length = max_x - min_x
#             width = max_y - min_y
#             _x = max_x - length / 2
#             _y = max_y - width / 2
#
#
#         with os.scandir(path=directory) as it:
#             for entry in it:
#                 img_obj = Image.open(directory + entry.name)
#                 width_size = height_size = 0
#                 delta = resize_x_to_min / float(img_obj.size[0])
#                 width_size = int(float(img_obj.size[0]) * delta)
#                 height_size = int(float(img_obj.size[1]) * delta)
#                 delta = resize_y_to_min / float(img_obj.size[1])
#                 width_size = int(float(img_obj.size[0]) * delta)
#                 height_size = int(float(img_obj.size[1]) * delta)
#                 img_obj = img_obj.resize((width_size, height_size), Image.ANTIALIAS)
#                 img_obj.save(directory + entry.name)
#
#         img_path = 'images/output/elements' + str(number_element) + '.jpg'
#         img = load_img(img_path, target_size=(150, 150))
#
#         y = img_to_array(img)
#         y = y / 255
#         y = np.expand_dims(y, axis=0)
#
#         prediction = loaded_model.predict(y)
#
#         for value in range(len(prediction)):
#             prediction = prediction[value]
#
#         prediction = np.argmax(prediction)
#
#         _class = d[prediction]
#
#         data['elements'].append(Element().__dict__)
#
#         number_element += 1
#     if len(approx) == 8:
#         cv2.drawContours(window_wall_mask, [approx], -1, (0, 0, 0), 4)
#         cv2.imwrite("images/output/elements" + str(number_element) + ".jpg", window_wall_mask)
#         window_wall_mask = cv2.imread('images/sours_blank/window.bmp')
#         pos = approx
#         pos1 = pos[0]
#         pos11 = pos1[0]
#         x11 = pos11[0]
#         y11 = pos11[1]
#         x1 = int(x11)
#         y1 = int(y11)
#
#         pos2 = pos[1]
#         pos21 = pos2[0]
#         x21 = pos21[0]
#         y21 = pos21[1]
#         x2 = int(x21)
#         y2 = int(y21)
#
#         pos3 = pos[2]
#         pos31 = pos3[0]
#         x31 = pos31[0]
#         y31 = pos31[1]
#         x3 = int(x31)
#         y3 = int(y31)
#
#         pos4 = pos[3]
#         pos41 = pos4[0]
#         x41 = pos41[0]
#         y41 = pos41[1]
#         x4 = int(x41)
#         y4 = int(y41)
#
#         pos5 = pos[4]
#         pos51 = pos5[0]
#         x51 = pos51[0]
#         y51 = pos51[1]
#         x5 = int(x51)
#         y5 = int(y51)
#
#         pos6 = pos[5]
#         pos61 = pos6[0]
#         x61 = pos61[0]
#         y61 = pos61[1]
#         x6 = int(x61)
#         y6 = int(y61)
#
#         pos7 = pos[6]
#         pos71 = pos7[0]
#         x71 = pos71[0]
#         y71 = pos71[1]
#         x7 = int(x71)
#         y7 = int(y71)
#
#         pos8 = pos[7]
#         pos81 = pos8[0]
#         x81 = pos81[0]
#         y81 = pos81[1]
#         x8 = int(x81)
#         y8 = int(y81)
#
#         list_x = [x1, x2, x3, x4, x5, x6, x7, x8]
#         list_y = [y1, y2, y3, y4, y5, y6, y7, y8]
#
#         max_x = max(list_x)
#         min_x = min(list_x)
#
#         max_y = max(list_y)
#         min_y = min(list_y)
#
#         if ((max_y - min_y) > (max_x - min_x)):
#             length = max_y - min_y
#             width = max_x - min_x
#             _x = max_x - width / 2
#             _y = max_y - length / 2
#         else:
#             length = max_x - min_x
#             width = max_y - min_y
#             _x = max_x - length / 2
#             _y = max_y - width / 2
#
#         with os.scandir(path=directory) as it:
#             for entry in it:
#                 img_obj = Image.open(directory + entry.name)
#                 width_size = height_size = 0
#                 delta = resize_x_to_min / float(img_obj.size[0])
#                 width_size = int(float(img_obj.size[0]) * delta)
#                 height_size = int(float(img_obj.size[1]) * delta)
#                 delta = resize_y_to_min / float(img_obj.size[1])
#                 width_size = int(float(img_obj.size[0]) * delta)
#                 height_size = int(float(img_obj.size[1]) * delta)
#                 img_obj = img_obj.resize((width_size, height_size), Image.ANTIALIAS)
#                 img_obj.save(directory + entry.name)
#
#         img_path = 'images/output/elements' + str(number_element) + '.jpg'
#         img = load_img(img_path, target_size=(150, 150))
#
#         y = img_to_array(img)
#         y = y / 255
#         y = np.expand_dims(y, axis=0)
#
#         prediction = loaded_model.predict(y)
#
#         for value in range(len(prediction)):
#             prediction = prediction[value]
#
#         prediction = np.argmax(prediction)
#
#         _class = d[prediction]
#
#         data['elements'].append(Element().__dict__)
#         number_element += 1
#
# # запись в JSON
# write(data, 'data.json')

# проверка для консоли
print('total = ', total)
print('wall(red) = ', wall)
print('door_wall(green) = ', door_wall)
print('window_wall(blue) = ', window_wall)
# вывод для проверки(test_output)
cv2.imwrite("images/test_output/test_final.jpg", image1)

# # получение данных из JSON
# n_data = read('data.json')
# print(n_data['elements'][0])
#
# # получение конкретных данных
# g = Element()
# g.name = n_data['elements'][0]['Class']
# print(g.name)
