import numpy
import PIL
from PIL import Image, ImageDraw
def pentagram(img, x, y, r, thickness, color):
    dr = ImageDraw.Draw(img, "RGB")
    x1 = x - r
    y1 = y - r
    x2 = x + r
    y2 = y + r
    dr.ellipse(((x1, y1), (x2, y2)),fill = None, width = thickness, outline= tuple(color))
    versh = []
    for i in range(5):
        phi = (numpy.pi / 5) * (2 * i + 3 / 2)
        node_i = (int(x + r * numpy.cos(phi)), int(y + r * numpy.sin(phi)))
        versh.append((node_i))
    versh=tuple(versh)
    for i in range(5):
        dr.line((versh[i],versh[(i + 2) % 5]),fill = tuple(color),width = thickness)
    return img
    
def swap(img, x0,y0,x1,y1,width):
    nimg = img.copy()
    part1 = nimg.crop((x0, y0, x0 + width, y0 + width)).rotate(-90)
    part2 = nimg.crop((x1, y1, x1 + width, y1 + width)).rotate(-90)
    nimg.paste(part1, (x1, y1))
    nimg.paste(part2, (x0, y0))
    nimg = nimg.rotate(-90)
    return nimg 
    
def avg_color(img, x0,y0,x1,y1):
    nimg = img.copy()
    sz = img.size
    for x in range(x0, x1 + 1):
        for y in range(y0, y1 + 1):
            sum = [0]*3
            pix_near= [(x-1,y-1), (x,y+1), (x,y-1), (x+1,y), (x+1,y-1), (x+1,y+1), (x-1,y+1), (x-1,y)]
            count = len(pix_near)
            for k in range(count):
                if not filtr_gran(pix_near[count-k-1],sz):
                    pix_near.pop(count-k-1)
            for n in pix_near:
                pixel = img.getpixel(n)
                for m in range(3):
                    sum[m] += pixel[m]        
            count = len(pix_near)        
            ncolor = (int(sum[0] / count), int(sum[1] / count), int(sum[2] / count))
            nimg.putpixel((x, y), ncolor)
    return nimg        
            
            
            
def filtr_gran(coord,sz):
    return (coord[0] >= 0) and (coord[0] < sz[0]) and (coord[1] >= 0) and (coord[1] < sz[1])
