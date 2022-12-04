from PIL import Image, ImageDraw, ImageOps


# Задача 1
def user_func(image, x0, y0, x1, y1, fill, width):
	draw = ImageDraw.Draw(image)
	draw.line(((x0,y0),(x1,y1)), fill, width)
	return image

# Задача 2
def check_coords(image, x0, y0, x1, y1):
	if all(map(lambda p: isinstance(p, int), (x0, y0, x1, y1))):
		if 0 <= x0 < x1 <= image.size[0]:
			if 0 <= y0 < y1 <= image.size[1]:
				return True
	return False

def set_black_white(image, x0, y0, x1, y1):
	if check_coords(image, x0, y0, x1, y1):
		place = image.crop((x0, y0, x1, y1))
		place = place.convert('1')
		image.paste(place, (x0, y0))
	return image

# Задача 3
def max_rectangle_under_histogram(data):
	stack = []
	max_rectangle = [0, 0, 0, 0] # площадь, ширина, высота, x
	i = 0
	while (i < len(data) or stack):
		if (i < len(data)) and (not stack or data[stack[-1]] <= data[i]):
			stack.append(i)
			i += 1
		else:
			width = i
			height = data[stack.pop()]
			if stack:
				width = (i-stack[-1]-1)
			area = width * height
			if area > max_rectangle[0]:
				max_rectangle = [area, width, height, i-1]
	return max_rectangle

def max_rectangle_in_matrix(matrix):
	max_rectangle = max_rectangle_under_histogram(matrix[0]) + [0] # добавляем y
	for y in range(1, len(matrix)):
		for x in range(len(matrix[0])):
			if matrix[y][x]:
				matrix[y][x] += matrix[y-1][x]
		new_rectangle = max_rectangle_under_histogram(matrix[y]) + [y]
		if max_rectangle[0] < new_rectangle[0]:
			max_rectangle = new_rectangle
	return max_rectangle

def find_rect_and_recolor(image, old_color, new_color):
	pix = image.load()
	matrix = []
	for y in range(image.height):
		matrix.append([])
		for x in range(image.width):
			flag = (pix[x, y] == old_color)
			matrix[y].append(int(flag))
	area, w, h, x2, y2 = max_rectangle_in_matrix(matrix)
	x1, y1 = x2 - w + 1, y2 - h + 1
	draw = ImageDraw.Draw(image)
	draw.rectangle((x1, y1, x2, y2), fill=new_color)
	return image


#test = Image.open("test1.png")
#find_rect_and_recolor(test, (0,0,0), (0,0,255)).resize((600, 600)).show()
#test = Image.open("test2.png")
#find_rect_and_recolor(test, (0,0,0), (0,0,255)).resize((600, 600)).show()
#test = Image.open("test3.png")
#find_rect_and_recolor(test, (255,0,0), (0,0,255)).resize((400, 300)).show()
