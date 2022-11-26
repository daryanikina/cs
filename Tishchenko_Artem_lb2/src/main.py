from PIL import Image, ImageDraw
import numpy as np


# Задача 1
def triangle(img, x0, y0, x1, y1, x2, y2, thickness, color, fill_color) -> Image:
    drawing = ImageDraw.Draw(img)
    if fill_color is not None:
        fill_color = tuple(fill_color)
    color = tuple(color)
    drawing.polygon(((x0, y0), (x1, y1), (x2, y2)), fill_color, color, thickness)
    return img


# Задача 2
def change_color(img: Image, color) -> Image:
    arr = np.asarray(img).copy()
    colors = {}
    color = tuple(color)
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            px_color = tuple(arr[i][j])
            if px_color in colors:
                colors[px_color] += 1
            else:
                colors[px_color] = 1
    orig_color = max(colors, key=colors.get)
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            px_color = tuple(arr[i][j])
            if px_color == orig_color:
                arr[i][j] = np.array(color)
    return Image.fromarray(arr)


# Задача 3
def collage(img: Image, N, M) -> Image:
    arr = np.asarray(img).copy()
    arr_buf = arr.copy()
    for i in range(M-1):
        arr = np.hstack((arr, arr_buf))
    arr_buf = arr.copy()
    for i in range(N-1):
        arr = np.vstack((arr, arr_buf))
    return Image.fromarray(arr)
