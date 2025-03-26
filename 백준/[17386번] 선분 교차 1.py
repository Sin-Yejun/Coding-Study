def is_divide_pt(x11,y11, x12,y12, x21,y21, x22,y22):

    #  // line1 extension이 line2의 두 점을 양분하는지 검사..
    # 직선의 양분 판단
    f1= (x12-x11)*(y21-y11) - (y12-y11)*(x21-x11)
    f2= (x12-x11)*(y22-y11) - (y12-y11)*(x22-x11)
    if f1*f2 < 0 :
      return True
    else:
      return False

def is_cross_pt(x11,y11, x12,y12, x21,y21, x22,y22):
    b1 = is_divide_pt(x11,y11, x12,y12, x21,y21, x22,y22)
    b2 = is_divide_pt(x21,y21, x22,y22, x11,y11, x12,y12)
    if b1 and b2:
        return True
    return False

x11, y11, x12, y12 = map(int, input().split())
x21, y21, x22, y22 = map(int, input().split())

if is_cross_pt(x11, y11, x12, y12, x21, y21, x22, y22):
    print(1)
else:
    print(0)
