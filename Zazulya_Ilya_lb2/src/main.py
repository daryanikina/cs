from PIL import Image, ImageDraw
from math import pi, cos, sin

def pentagram(img, x0, y0, x1, y1, thickness, color):
    color = tuple(color)
    drawing = ImageDraw.Draw(img, "RGB")
    drawing.ellipse((x0,y0,x1,y1), outline=color, width=thickness)
    r = int(abs(x0-x1)/2)
    center_x = int(x1 - abs(x0-x1)/2)
    center_y = int(y1 - abs(y0-y1)/2)
    coords_pen = []
    for i in range(0, 6):
        phi = (pi / 5) * (4 * i + 3 / 2)
        node_i = (int(center_x + r * cos(phi)), int(center_y + r * sin(phi)))
        coords_pen.append(node_i)
    drawing.line(coords_pen, fill=color, width=thickness)
    return img

def invert(img, N,vertical):
    w,h = img.size
    if vertical:
        curr_width = 0
        count_l = w//N if w%N==0 else int(w/N)+1
        for i in range(count_l):
            if w%N!=0 and i==count_l-1:
                if i%2==1:
                    for j in range(curr_width, w):
                        for k in range(h):
                            pix = img.getpixel((j, k))
                            pix = tuple((255 - pix[i]) for i in range(3))
                            img.putpixel((j, k), pix)
                else:
                    continue
            elif i%2==1:
                for j in range(curr_width, curr_width+N):
                    for k in range(h):
                        pix = img.getpixel((j,k))
                        pix = tuple((255 - pix[i]) for i in range(3))
                        img.putpixel((j,k), pix)
            if curr_width + N <= w: curr_width += N
            else: break
    else:
        curr_height = 0
        count_l = h//N if h%N==0 else int(h/N)+1
        for i in range(count_l):
            if h%N!=0 and i==count_l-1:
                if i%2==1:
                    for j in range(curr_height, h):
                        for k in range(w):
                            pix = img.getpixel((k, j))
                            pix = tuple((255 - pix[i]) for i in range(3))
                            img.putpixel((k, j), pix)
                else:
                    continue
            elif i%2==1:
                for j in range(curr_height, curr_height+N):
                    for k in range(w):
                        pix = img.getpixel((k,j))
                        pix = tuple((255 - pix[i]) for i in range(3))
                        img.putpixel((k,j), pix)
            if curr_height + N <= h: curr_height += N
            else: break
    return img

def mix(img, rules):
    w,h = img.size
    side = int(h/3)
    images = []
    coords = []
    coords1 = [((0, int((side)*i)), (int(side)*1, int((side)*(i+1)))) for i in range(3)]
    coords2 = [((int(side), int((side)*i)), (int((side)*2), int((side)*(i+1)))) for i in range(3)]
    coords3 = [((int((side)*2), int((side)*i)), (int((side)*3), int((side)*(i+1)))) for i in range(3)]
    coords = [coords1] + [coords2] + [coords3]
    sort_coords = [coords[i][k] for k in range(3) for i in range(3)]
    good_coords = []
    for i in range(9):
        good_coords.append([g for k in sort_coords[i] for g in k])
    for l in range(9):
        images.append(img.crop((good_coords[l])))
    for t in range(9):
        img.paste(images[rules[t]], (good_coords[t][0], good_coords[t][1]))
    return img