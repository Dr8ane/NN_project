

####################################################################
# Перед началом, убедитесь, что все библиотеки установлены/обновлены
# В окне проекта обязательно должна быть папка images с 5 папками(for_NN, input, output, test_output, sours_blank)
# В окне проекта обязательно должен лежать исходный вайл в пути images/input/input.bmp
# В окне проекта обязательно должны лежать пустышки в пути images/sours_blank/   wall, window, door и т.д.
####################################################################

import cv2
import imutils
import random

# чтение изображения для работы(input)
image = cv2.imread('images/input/input.bmp')
# чтение вспомогательных изображений(sours_blank)
wall_mask = cv2.imread('images/sours_blank/wall.bmp')
door_wall_mask = cv2.imread('images/sours_blank/door.bmp')
window_wall_mask = cv2.imread('images/sours_blank/window.bmp')
# подготовка изображения для работы
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
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

# прогонка для проверки(test_output)
for c in cnts:
    p = cv2.arcLength(c, True)
    approx = cv2.approxPolyDP(c, 0.02 * p, True)
    if len(approx) == 4:
        cv2.drawContours(image, [approx], -1, (0, 0, 255), 4)
        total += 1
        wall += 1
    if len(approx) == 7:
        cv2.drawContours(image, [approx], -1, (0, 255, 0), 4)
        total += 1
        door_wall += 1
    if len(approx) == 8:
        cv2.drawContours(image, [approx], -1, (255, 0, 0), 4)
        total += 1
        window_wall += 1

# генерация для обучения(train)
while n < 875:
    for c in cnts:
        p = cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, 0.02 * p, True)
        if len(approx) == 4:
            cv2.drawContours(wall_mask, [approx], -1, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), 4)
            cv2.imwrite("images/for_NN/train/wall/wall" + str(nwall) + ".jpg", wall_mask)
            wall_mask = cv2.imread('images/sours_blank/wall.bmp')
            nwall += 1
        if len(approx) == 7:
            cv2.drawContours(door_wall_mask, [approx], -1, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), 4)
            cv2.imwrite("images/for_NN/train/door/door" + str(ndoor_wall) + ".jpg", door_wall_mask)
            door_wall_mask = cv2.imread('images/sours_blank/door.bmp')
            ndoor_wall += 1
        if len(approx) == 8:
            cv2.drawContours(window_wall_mask, [approx], -1, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), 4)
            cv2.imwrite("images/for_NN/train/window/window" + str(nwindow_wall) + ".jpg", window_wall_mask)
            window_wall_mask = cv2.imread('images/sours_blank/window.bmp')
            nwindow_wall += 1
    n += 1

# генерация для проверки(val)
while t1 < 188:
    for c in cnts:
        p = cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, 0.02 * p, True)
        if len(approx) == 4:
            cv2.drawContours(wall_mask, [approx], -1, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), 4)
            cv2.imwrite("images/for_NN/val/wall/wall" + str(nwall) + ".jpg", wall_mask)
            wall_mask = cv2.imread('images/sours_blank/wall.bmp')
            nwall += 1
        if len(approx) == 7:
            cv2.drawContours(door_wall_mask, [approx], -1, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), 4)
            cv2.imwrite("images/for_NN/val/door/door" + str(ndoor_wall) + ".jpg", door_wall_mask)
            door_wall_mask = cv2.imread('images/sours_blank/door.bmp')
            ndoor_wall += 1
        if len(approx) == 8:
            cv2.drawContours(window_wall_mask, [approx], -1, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), 4)
            cv2.imwrite("images/for_NN/val/window/window" + str(nwindow_wall) + ".jpg", window_wall_mask)
            window_wall_mask = cv2.imread('images/sours_blank/window.bmp')
            nwindow_wall += 1
    t1 += 1

# генерация для тестов(test)
while t2 < 188:
    for c in cnts:
        p = cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, 0.02 * p, True)
        if len(approx) == 4:
            cv2.drawContours(wall_mask, [approx], -1, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), 4)
            cv2.imwrite("images/for_NN/test/wall/wall" + str(nwall) + ".jpg", wall_mask)
            wall_mask = cv2.imread('images/sours_blank/wall.bmp')
            nwall += 1
        if len(approx) == 7:
            cv2.drawContours(door_wall_mask, [approx], -1, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), 4)
            cv2.imwrite("images/for_NN/test/door/door" + str(ndoor_wall) + ".jpg", door_wall_mask)
            door_wall_mask = cv2.imread('images/sours_blank/door.bmp')
            ndoor_wall += 1
        if len(approx) == 8:
            cv2.drawContours(window_wall_mask, [approx], -1, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), 4)
            cv2.imwrite("images/for_NN/test/window/window" + str(nwindow_wall) + ".jpg", window_wall_mask)
            window_wall_mask = cv2.imread('images/sours_blank/window.bmp')
            nwindow_wall += 1
    t2 += 1

# выходные значения(output)
for c in cnts:
    p = cv2.arcLength(c, True)
    approx = cv2.approxPolyDP(c, 0.02 * p, True)
    if len(approx) == 4:
        cv2.drawContours(wall_mask, [approx], -1, (0, 0, 0), 4)
        cv2.imwrite("images/output/elements" + str(number_element) + ".jpg", wall_mask)
        wall_mask = cv2.imread('images/sours_blank/wall.bmp')
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

# проверка для консоли
print('total = ', total)
print('wall(red) = ', wall)
print('door_wall(green) = ', door_wall)
print('window_wall(blue) = ', window_wall)
# вывод для проверки(test_output)
cv2.imwrite("images/test_output/test_final.jpg", image)
