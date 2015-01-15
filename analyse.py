ops_button_corner = (151, 636)


def find_line(rgb_im):
    if rgb_im[ops_button_corner][0] > 200 and rgb_im[ops_button_corner][1] > 200 and rgb_im[ops_button_corner][2] > 200:
        for y in range(700, 1000):
            x = 650
            b, g, r = rgb_im[y, x]
            # print r,g,b
            # print (rgb_im[y,x-500]==rgb_im[y,x]).all()
            # print b
            minus = 500
            if (rgb_im[y, x][0] - 20 <= rgb_im[y, x - minus][0] <= rgb_im[y, x][0] + 20)\
                    and (rgb_im[y, x][1] - 20 <= rgb_im[y, x - minus][1] <= rgb_im[y, x][1] + 20)\
                    and b > 140 and g > 130 and g < 200 and r < 70:
                return (x, y)


def color_of_hack(rgb_im, line_y):
    res = []
    x_cord = [62, 0]
    diffs = [65, 65]
    for i in range(10):
        if i < 1:
            b, g, r = rgb_im[line_y[1] + diffs[i], x_cord[i]]
            if r > 210 and g < 55 and b < 220 and b > 180:
                #print "L6!"
                res.append("L6")
            if r > 200 and g < 65 and b > 120 and b < 160:
                #print "L5!"
                res.append("L5")
            elif b < 70 and g < 140 and g > 80 and r > 200:
                #print "L3!"
                res.append("L3")
        elif i < 2:
            for x in range(300, 440):
                b, g, r = rgb_im[line_y[1] + diffs[i], x_cord[i] + x]
                # print line_y[1] + diffs[i], x_cord[i]
                if r > 210 and g < 55 and b < 220 and b > 180:
                    #print "L6!"
                    res.append("L6")
                    break
                if r > 200 and g < 65 and b > 120 and b < 160:
                    #print "L5!"
                    res.append("L5")
                    break
                elif b < 70 and g < 140 and g > 80 and r > 200:
                    #print "L3!"
                    res.append("L3")
                    break
        else:
            pass
    return res
