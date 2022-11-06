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
    else:
        x1 = x - w / 2
        y1 = y - l / 2
        x2 = x + w / 2
        y2 = y + l / 2

    draw.rectangle(((x1, y1), (x2, y2)), '#000000')

def window(x, y, l, w, r):
    if r == 1:
        x1 = x - l/2
        y1 = y - w/2
        x2 = x + l/2
        y2 = y + w/2
        x3 = x - l/4
        y3 = y - w/2 + 4
        x4 = x + l/4
        y4 = y + w / 2 - 4
    else:
        x1 = x - w / 2
        y1 = y - l / 2
        x2 = x + w / 2
        y2 = y + l / 2
        x3 = x - w / 4
        y3 = y - l / 2 + 4
        x4 = x + w / 4
        y4 = y + l / 2 - 4

    draw.rectangle(((x1, y1), (x2, y2)), '#000000')
    draw.rectangle(((x3, y3), (x4, y4)), '#FFFFFF')

def door(x, y, l, w, r):
    if r == 1:
        x1 = x - l/2
        y1 = y - w/2
        x2 = x + l/2
        y2 = y + w/2

    else:
        x1 = x - w / 2
        y1 = y - l / 2
        x2 = x + w / 2
        y2 = y + l / 2

    draw.rectangle(((x1, y1), (x2, y2)), '#FF0000')

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

# получение данных из JSON
n_data = read('data.json')
n_data = n_data['elements']
print(n_data)

for i,t in enumerate(n_data):
    new_data = t
    g = Element()
    g.name = new_data['Class']
    x = int(new_data['X'])
    y = int(new_data['Y'])
    l = new_data['Length']
    w = new_data['Width']
    r = new_data['Rotation']
    # print(g.name, g.x, g.y, g.l, g.w, g.r)

    if g.name == d[0]:
        door(x,y,l,w,r)
    else:
        if g.name == d[1]:
            wall(x,y,l,w,r)
        else:
            if g.name == d[2]:
                window(x,y,l,w,r)



im.save('res.png')

# получение конкретных данных
# g = Element()
# g.name = new_data['Class']
# print(g.name)
# print(d[2])


