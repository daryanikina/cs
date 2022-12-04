import numpy as np
from PIL import Image, ImageDraw, ImageOps

def pentagram(img, x0, y0, x1, y1, thickness, color):
    color = tuple(color)
    # # радиус и центр окружности
    r = int(abs(x1 - x0) // 2)
    center_x = int(x1 - (abs(x1 - x0) // 2))
    center_y = int(y1 - (abs(y1 - y0) // 2))
    drawing = ImageDraw.Draw(img)
    drawing.ellipse((x0, y0, x1, y1), fill = None , width= thickness,  outline= color )
    coordinates = []
    for i in range(0, 6):
        phi = (np.pi / 5) * (4 * i + 3 / 2)
        node_i = (int(center_x + r * np.cos(phi)), int(center_y + r * np.sin(phi)))
        coordinates.append(node_i)
    drawing.line(coordinates, color, thickness)
    return img

def invert(img, N,vertical):
    img_invert = ImageOps.invert(img)
    width, height = img.size
    if vertical:
        for i in range(1, width // N+1, 2):
            x0 = i*N
            if (i+1)*N <= width:
                x1 = (i+1)*N
            else:
                x1 = width
            part = img_invert.crop((x0, 0, x1, height))
            img.paste(part, (x0, 0, x1, height))
    else:
        for i in range(1, height // N+1, 2):
            x0 = i*N
            if (i+1)*N <= height:
                x1 = (i+1)*N
            else:
                x1 = height
            part = img_invert.crop((0, x0, width, x1))
            img.paste(part, (0, x0, width, x1))
    return img

def mix(img, rules):
    width, height = img.size
    part_side = width // 3
    res = Image.new("RGB", (width, height), (0, 0, 0))
    for n in range(9):
        m = rules[n]
        x = m % 3
        y = m // 3
        part = img.crop((x * part_side, y * part_side, (x + 1) * part_side, (y + 1) * part_side))
        x = n % 3
        y = n // 3
        res.paste(part, (x * part_side, y * part_side, (x + 1) * part_side, (y + 1) * part_side))
    return res