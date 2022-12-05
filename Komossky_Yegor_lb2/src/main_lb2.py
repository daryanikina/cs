import numpy as np
from PIL import Image, ImageDraw
# Задача 1
def triangle(img, x0, y0, x1, y1, x2, y2, thickness, color, fill_color):
    draw = ImageDraw.Draw(img)
    if fill_color is None:
        draw.polygon([(x0,y0), (x1, y1), (x2,y2)], fill = None, outline = tuple(color), width=thickness)
    else: draw.polygon([(x0,y0), (x1, y1), (x2,y2)], fill = tuple(fill_color), outline = tuple(color), width=thickness)
    return img

# Задача 2
def change_color(img, color):
    count= {}
    for i in img.getdata():
        if i not in count:
            count[i] = 0
        count[i] += 1
    max_color = max(count, key=count.get)
    arr = np.array(img)
    arr[arr == max_color] = color
    img = Image.fromarray(arr)
    return img

# Задача 3
def collage(img, N, M):
    img1 = Image.new("RGB", (img.size[0]*M, img.size[1]*N), 'white')
    width, height = img1.size
    for x in range(0, width, img.size[0]):
        for y in range(0, height, img.size[1]):
            img1.paste(img, (x, y))
    return img1
