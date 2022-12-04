import numpy
import PIL
from PIL import Image, ImageDraw
def user_func(image, x0, y0, x1, y1, fill, width):
    drawing = ImageDraw.Draw(image)
    drawing.line((x0, y0, x1, y1), fill, width)
    return image
def check_coords(image, x0, y0, x1, y1):
    height, width=image.size
    if ((height>=x1) and (x1>x0) and (x0>=0) and (width>=y1) and (y1>y0) and (y0>=0)):
        return True
    else:
        return False
def set_black_white(image, x0, y0, x1, y1):
    if not check_coords(image, x0, y0, x1, y1):
        return image
    cropped_image = image.crop((x0, y0, x1, y1))
    cropped_image = cropped_image.convert("1")
    image.paste(cropped_image, (x0, y0))
    return image
def find_rect_and_recolor(image, old_color, new_color):
    if not isinstance(old_color, tuple):
        old_color = PIL.ImageColor.getrgb(old_color)
    width, height = image.size
    max_area = 0
    best_xy = None
    part = numpy.zeros(image.size, dtype=numpy.uint32)
    for i in range(width):
        for j in range(height):
            part[i, j] = int(image.getpixel((i, j)) == old_color)
    hist = numpy.zeros(height, dtype=numpy.uint32)
    for i in range(width):
        hist = numpy.multiply((hist + 1), part[i])
        area, yy = max_area_histogram(hist)
        if yy is not None:
            width = area // (yy[1] - yy[0])
            assert width == min(hist[yy[0] : yy[1]])
        if area > max_area:
            max_area = area
            best_xy = (i + 1 - width, yy[0]), (i, yy[1] - 1)
    if best_xy is not None:
        draw = ImageDraw.Draw(image)
        draw.rectangle(best_xy, fill=new_color, outline=new_color)
    return image
def max_area_histogram(hist):
    stack = []
    max_area = 0
    best_yy = None
    index = 0
    while index < len(hist):
        if (not stack) or (hist[stack[-1]] <= hist[index]):
            stack.append(index)
            index += 1
        else:
            top = stack.pop()
            yy = (stack[-1] + 1, index) if stack else (0, index)
            area = hist[top] * (yy[1] - yy[0])
            if area > max_area:
                max_area = area
                best_yy = yy
    while stack:
        top = stack.pop()
        yy = (stack[-1] + 1, index) if stack else (0, index)
        area = hist[top] * (yy[1] - yy[0])
        if area > max_area:
            max_area = area
            best_yy = yy
    return max_area, best_yy
