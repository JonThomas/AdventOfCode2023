def isPointInRect(x, y, rect_x, rect_y, rect_w, rect_h):
    if (x >= rect_x and x <= rect_x + rect_w and
        y >= rect_y and y <= rect_y + rect_h):
        return True
    else:
        return False