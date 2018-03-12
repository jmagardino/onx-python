def flatten_2d_array(two_d_array):
  newlist = []
  for list in two_d_array:
      for item in list:
          newlist.append(item)
  return newlist

def access_2d_item_in_1d_array(i, j, width, onedarray):
    return onedarray[i*width+j]

def centroid_of_rectangle(first_corner, second_corner):
    return ((first_corner[0] + second_corner[0]) / 2 , (first_corner[1] + second_corner[1]) / 2)

def point_exists_in_rectangle(top_left_corner,length,height,point):
    return top_left_corner[0] <= point[0] and top_left_corner[0] +length >= point[0] and top_left_corner[1] >= point[1] and top_left_corner[1] - height <= point[0]

def point_exists_in_rectangle_enhanced(top_left_corner, bottom_left_corner, top_right_corner, bottom_right_corner, point):
    area_of_rectangle = area_of_triangle(top_left_corner, bottom_left_corner, top_right_corner) + area_of_triangle(bottom_left_corner, bottom_right_corner, top_right_corner)
    tl_bl_point = area_of_triangle(top_left_corner, bottom_left_corner, point)
    bl_br_point = area_of_triangle(bottom_left_corner, bottom_right_corner, point)
    br_tr_point = area_of_triangle(bottom_right_corner, top_right_corner, point)
    tl_tr_point = area_of_triangle(top_left_corner, top_right_corner, point)

    return area_of_rectangle == tl_bl_point + bl_br_point + br_tr_point + tl_tr_point

def area_of_triangle(a,b,c):
    ax = a[0]
    ay = a[1]
    bx = b[0]
    by = b[1]
    cx = c[0]
    cy = c[1]
    return abs((ax*(by-cy) + bx*(cy-ay) + cx*(ay-by))/2)
