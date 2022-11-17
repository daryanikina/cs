from PIL import Image, ImageDraw
import numpy as np


# Задача 1
def user_func(image, x0, y0, x1, y1, fill, width):
    drawing = ImageDraw.Draw(image)
    drawing.line(((x0, y0), (x1, y1)), fill=fill, width=width)
    return image


# Задача 2
def check_coords(image, x0, y0, x1, y1):
    height, width = image.height, image.width

    if not (0 <= x0 < width and 0 <= y0 < height):
        return False
    if not (0 < x1 < width and 0 < y1 < height):
        return False

    if not (x0 < x1 and y0 < y1):
        return False

    return True


def set_black_white(image, x0, y0, x1, y1):
    if not check_coords(image, x0, y0, x1, y1):
        return image

    cropped_image = image.crop((x0, y0, x1, y1))
    cropped_image = cropped_image.convert("1")
    image.paste(cropped_image, (x0, y0))

    return image


# Задача 3
def find_biggest_rect(image, color):
    # to bin matrix
    arr = np.array(image).tolist()
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            arr[i][j] = 1 if arr[i][j] == list(color) else 0
    arr = np.array(arr)

    # count max height
    for i in range(1, len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] == 0:
                arr[i][j] = 0
            else:
                arr[i][j] += arr[i - 1][j]

    # find max area
    max_area = 0
    coordinates = (0, 0, 0, 0)
    for i in range(len(arr)):
        area = 0
        for k in set(arr[i]):
            for j in range(len(arr[i])):
                if k <= arr[i][j]:
                    area += k

                if j == len(arr[i]) - 1 or arr[i][j + 1] < k:
                    if max_area < area:
                        max_area = area
                        # x0, y0, x1, y1
                        coordinates = (j - area // k + 1, i - k + 1, j, i)
                    area = 0

    return coordinates


def find_rect_and_recolor(image, old_color, new_color):
    coords = find_biggest_rect(image, old_color)

    if coords == (0, 0, 0, 0):
        return image

    arr = np.array(image)
    arr[coords[1]:coords[3] + 1, coords[0]:coords[2] + 1, :3] = list(new_color)
    image = Image.fromarray(arr)

    return image
