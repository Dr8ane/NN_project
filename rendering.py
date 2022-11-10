from PIL import Image, ImageDraw
import json

im = Image.new("RGB", (1000, 800), '#FFFFFF')
draw = ImageDraw.Draw(im)

d = {0: 'дверь', 1: 'стена', 2: 'окно'}

def wall(x, y, l, w, r):
    if r == 1:
        x1 = x - l/2
        y1 = y - w/2
        x2 = x + l/2
        y2 = y + w/2
        xt1 = x1
        yt1 = y2
        xt2 = x2
        yt2 = y1
        xti = xt1 + w
        yti = yt1 -w
        draw.rectangle(((x1, y1), (x2, y2)), '#FFFFFF', outline=(0, 0, 0))
        draw.line((xt1, yt1 - w/2, xti - w/2, yti), fill='black')
        while xti < xt2:
            draw.line((xt1, yt1, xti, yti), fill='black')
            xt1 += w/2
            xti += w / 2
        draw.line((xt1, yt1, xti - w / 2, yti + w / 2), fill='black')
    else:
        x1 = x - w / 2
        y1 = y - l / 2
        x2 = x + w / 2
        y2 = y + l / 2
        xt1 = x - w / 2
        yt1 = y + l / 2
        xt2 = x + w / 2
        yt2 = y - l / 2
        xti = xt1 + w
        yti = yt1 - w
        draw.rectangle(((x1, y1), (x2, y2)), '#FFFFFF', outline=(0, 0, 0))
        draw.line((xt1 + w / 2, yt1, xti, yti + w / 2), fill='black')
        while yti > yt2:
            draw.line((xt1, yt1, xti, yti), fill='black')
            yt1 -= w / 2
            yti -= w / 2
        draw.line((xt1, yt1, xti - w / 2, yti + w / 2), fill='black')

def window(x, y, l, w, r):
    if r == 1:
        x1 = x - l / 2
        y1 = y - w / 2
        x2 = x + l / 2
        y2 = y + w / 2
        x3 = x - l / 4
        y3 = y - w / 2
        x4 = x + l / 4
        y4 = y + w / 2
        xt1 = x1
        yt1 = y2
        xt2 = x2
        yt2 = y1
        xti = xt1 + w
        yti = yt1 - w

        draw.rectangle(((x1, y1), (x2, y2)), '#FFFFFF', outline=(0, 0, 0))
        draw.line((xt1, yt1 - w / 2, xti - w / 2, yti), fill='black')
        while xti < xt2:
            draw.line((xt1, yt1, xti, yti), fill='black')
            xt1 += w / 2
            xti += w / 2
        draw.line((xt1, yt1, xti - w / 2, yti + w / 2), fill='black')
        draw.rectangle(((x3, y3), (x4, y4)), '#FFFFFF', outline=(0, 0, 0))
        draw.line((x3, y, x4, y), fill='black')
    else:
        x1 = x - w / 2
        y1 = y - l / 2
        x2 = x + w / 2
        y2 = y + l / 2
        x3 = x - w / 2
        y3 = y - l / 4
        x4 = x + w / 2
        y4 = y + l / 4
        xt1 = x - w / 2
        yt1 = y + l / 2
        xt2 = x + w / 2
        yt2 = y - l / 2
        xti = xt1 + w
        yti = yt1 - w
        draw.rectangle(((x1, y1), (x2, y2)), '#FFFFFF', outline=(0, 0, 0))
        draw.line((xt1 + w / 2, yt1, xti, yti + w / 2), fill='black')
        while yti > yt2:
            draw.line((xt1, yt1, xti, yti), fill='black')
            yt1 -= w / 2
            yti -= w / 2
        draw.line((xt1, yt1, xti - w / 2, yti + w / 2), fill='black')
        draw.rectangle(((x3, y3), (x4, y4)), '#FFFFFF', outline=(0, 0, 0))
        draw.line((x, y3, x, y4), fill='black')

def door(x, y, l, w, r):
    if r == 1:
        x1 = x - l/2
        y1 = y - w/2
        x2 = x + l/2
        y2 = y + w/2
        x3 = x - l/8
        y3 = y1 - w
        x4 = x + l/8 + l/4
        y4 = y2
        x5 = x + l/8
        y5 = y3
        x6 = x + l/8
        y6 = y1
        xt1 = x1
        yt1 = y2
        xt2 = x2
        yt2 = y1
        xti = xt1 + w
        yti = yt1 - w

        draw.rectangle(((x1, y1), (x2, y2)), '#FFFFFF', outline=(0, 0, 0))
        draw.line((xt1, yt1 - w / 2, xti - w / 2, yti), fill='black')
        while xti < xt2:
            draw.line((xt1, yt1, xti, yti), fill='black')
            xt1 += w / 2
            xti += w / 2
        draw.line((xt1, yt1, xti - w / 2, yti + w / 2), fill='black')
        draw.arc(xy=(x3, y3, x4, y4), start=180, end=270, fill=(0, 0, 0))
        draw.line((x5, y5, x6, y6), fill='black')
        draw.rectangle(((x3, y1), (x6, y2)), '#FFFFFF', outline=(0, 0, 0))
        draw.line((x3, y1+w/2, x6, y1+w/2), fill='black')
        draw.line((x3+1, y2, x6-1, y2), fill='white')


    else:
        x1 = x - w / 2
        y1 = y - l / 2
        x2 = x + w / 2
        y2 = y + l / 2
        x3 = x1 - w
        y3 = y - l/2 + l/8
        x4 = x + w/2
        y4 = y + l/8
        x5 = x3
        y5 = y- l/8
        x6 = x - w/2
        y6 = y - l/8
        xt1 = x - w / 2
        yt1 = y + l / 2
        xt2 = x + w / 2
        yt2 = y - l / 2
        xti = xt1 + w
        yti = yt1 - w

        draw.rectangle(((x1, y1), (x2, y2)), '#FFFFFF', outline=(0, 0, 0))
        draw.line((xt1 + w / 2, yt1, xti, yti + w / 2), fill='black')
        while yti > yt2:
            draw.line((xt1, yt1, xti, yti), fill='black')
            yt1 -= w / 2
            yti -= w / 2
        draw.line((xt1, yt1, xti - w / 2, yti + w / 2), fill='black')
        draw.arc(xy=(x3, y3, x4, y4), start=90, end=180, fill=(0, 0, 0))
        draw.line((x5, y5, x6, y6), fill='black')
        draw.rectangle(((x6, y6), (x2, y4)), '#FFFFFF', outline=(0, 0, 0))
        draw.line((x, y4, x, y5), fill='black')
        draw.line((x2, y4 - 1, x2, y5 + 1), fill='white')


def write(data, filename):
    data = json.dumps(data)
    data = json.loads(str(data))
    with open(filename, 'w', encoding = 'utf-8') as file:
        json.dump(data, file, indent = 4)

def read(filename):
    with open(filename, 'r', encoding = 'utf-8') as file:
        return json.load(file)

class Element:
    def __init__(self):
        self.Class = _class
        self.X = _x
        self.Y = _y
        self.Length = length
        self.Width = width
        self.Rotation = _r

data = {
    "elements" : []
}

_class = None
_x = None
_y = None
length = None
width = None
_r = None
x_for_r0 = []
y_for_r0 = []
x_for_r1 = []
y_for_r1 = []

# получение данных из JSON
n_data = read('data.json')
n_data = n_data['elements']

for i,t in enumerate(n_data):
    new_data = t
    g = Element()
    g.name = new_data['Class']
    if g.name == d[1]:
        l = new_data['Length']
        w = new_data['Width']

for i,t in enumerate(n_data):
    new_data = t
    g = Element()
    x = int(new_data['X'])
    y = int(new_data['Y'])
    r = new_data['Rotation']
    if r == 0:
        x_for_r0.append(x)
        y_for_r0.append(y)
    else:
        x_for_r1.append(x)
        y_for_r1.append(y)

x_r0_t = x_for_r0[0]
y_r1_t = y_for_r1[0]
for i in range(len(y_for_r1)):
    if abs(y_r1_t - y_for_r1[i]) < w:
        y_for_r1[i] = y_r1_t
        i +=1
    else:
        y_r1_t = y_for_r1[i]
        i +=1

for i in range(len(x_for_r0)):
    for j in range(len(x_for_r0)):
        if abs(x_for_r0[i] - x_for_r0[j]) < l/2:
            x_for_r0[j] = x_for_r0[i]
        j+=1
    i+=1

j = 0
k = 0

for i,t in enumerate(n_data):
    new_data = t
    g = Element()
    g.name = new_data['Class']
    # x = int(new_data['X'])
    # y = int(new_data['Y'])
    r = new_data['Rotation']
    if g.name == d[0]:
        if r == 0:
            x = x_for_r0[j]
            y = y_for_r0[j]
            j += 1
        else:
            x = x_for_r1[k]
            y = y_for_r1[k]
            k += 1
        door(x,y,l,w,r)
    else:
        if g.name == d[1]:
            if r == 0:
                x = x_for_r0[j]
                y = y_for_r0[j]
                j += 1
            else:
                x = x_for_r1[k]
                y = y_for_r1[k]
                k += 1
            wall(x,y,l,w,r)
        else:
            if g.name == d[2]:
                if r == 0:
                    x = x_for_r0[j]
                    y = y_for_r0[j]
                    j += 1
                else:
                    x = x_for_r1[k]
                    y = y_for_r1[k]
                    k += 1
                window(x,y,l,w,r)

im.save('res.png')
