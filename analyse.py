import Image	
im = Image.open('snap2.png')
rgb_im = im.convert('RGB')
rgb_im.save("a","PNG")
print rgb_im.size
def find_line(rgb_im):
	for y  in range(rgb_im.size[1]):
		for x in range(rgb_im.size[0]):
			r, g, b = rgb_im.getpixel((x, y))
			if x>500 and (r,g,b)==rgb_im.getpixel((x-500,y)) and r<50 and g>200 and b>200:
				return (x,y)

def color_of_hack(rgb_im,line_y):
	res=[]
	print line_y
	x_cord=[62,384]
	diffs=[-102,-102]
	for i in range(10):
		if i<2:
			res.append(rgb_im.getpixel((x_cord[i], line_y+diffs[i])))
		else:
			pass
	return res

print color_of_hack(rgb_im,find_line(rgb_im)[1])