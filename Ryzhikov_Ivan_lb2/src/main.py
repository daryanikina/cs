import numpy as np
from PIL import Image, ImageDraw, ImageOps


def pentagram(img: Image.Image, x0, y0, x1, y1, thickness, color):
    color = tuple(color)
    # Calculate
    radius = int(abs(x1 - x0) / 2)
    center_x = int(x1 - abs(x1 - x0) / 2)
    center_y = int(y1 - abs(x1 - x0) / 2)
    points = []
    for i in range(6):
        phi = (np.pi/5)*(4*i+3/2)
        node_i = (int(center_x+radius*np.cos(phi)),
                  int(center_y+radius*np.sin(phi)))
        points.append(node_i)
    # Draw
    draw = ImageDraw.Draw(img, "RGB")
    draw.ellipse((x0, y0, x1, y1), width=thickness, outline=color)
    draw.line(points, width=thickness, fill=color)
    return img


def invert(img: Image.Image, N: int, vertical: bool):
    img_invert = ImageOps.invert(img)
    width, height = img.size
    if vertical:
        for i in range(1, width // N+1, 2):
            start = i*N
            end = (i+1)*N if (i+1)*N <= width else width
            region = img_invert.crop((start, 0, end, height))
            img.paste(region, (start, 0, end, height))
    else:
        for i in range(1, height // N+1, 2):
            start = i*N
            end = (i+1)*N if (i+1)*N <= height else height
            region = img_invert.crop((0, start, width, end))
            img.paste(region, (0, start, width, end))
    return img


def mix(img: Image.Image, rules: dict):
    width, height = img.size
    region_length = width // 3
    new_img = Image.new("RGB", (width, height), "black")
    for n in range(9):
        m = rules[n]
        region = img.crop((m % 3 * region_length, m // 3 * region_length,
                          (m % 3 + 1) * region_length, (m // 3 + 1) * region_length))
        new_img.paste(region, (n % 3 * region_length, n // 3 * region_length,
                      (n % 3 + 1) * region_length, (n // 3 + 1) * region_length))
    return new_img

