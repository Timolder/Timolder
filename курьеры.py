import math
a=0
class Point():
    def __init__(self, X,Y):
        self.X=X
        self.Y=Y
    def __str__(self):
        return f"X point: {self.X}  Y point: {self.Y}"
    def get_distance(self, other_point):
        X1=self.X
        X2=other_point.X
        Y1=self.Y
        Y2=other_point.Y
        return math.dist((self.X, self.Y), (other_point.X, other_point.Y))
class Courier():
    def __init__(self, name, X, Y):
        self.name=name
        self.X=X
        self.Y=Y
    def __str__(self):
        return f"Имя: {self.name} X point: {self.X}  Y point: {self.Y} "
Courier1 = Courier("Дмитрий", 4, 4)
Courier2 =Courier("Семен", 1, 7)
O=Point(0, 0)
p1=Point(3, 4)
p2=Point(4, 8)
CourierN =[Courier1, Courier2]
p = [p1, p2]
for i in p:
    a=a+1
    dist = i.get_distance(CourierN[0])
    dist2= i.get_distance(CourierN[1])
    if (dist>=dist2):
        print("заказ", a, "получает", Courier1)
    else:
        print("заказ", a, "получает", Courier2)
