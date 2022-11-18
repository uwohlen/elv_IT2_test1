class World:
    def __init__(self) -> None:
        self.objects = []

    def add(self, object):
        self.objects.append(object)

    def step(self, dt):
        for object in self.objects:
            object.step(dt)

    def broad_phase(self):
        for i in range(len(self.objects)):
            for j in range(i+1, len(self.objects)):
                a = self.objects[i].aabb()
                b = self.objects[j].aabb()

                d1x = b[0].x - a[1].x
                d1y = b[0].y - a[1].y
                d2x = a[0].x - b[1].x
                d2y = a[0].y - b[1].y

                if d1x > 0 or d1y > 0:
                    continue
                if d2x > 0 or d2y > 0:
                    continue