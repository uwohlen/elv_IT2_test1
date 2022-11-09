class World:
    def __init__(self) -> None:
        self.objects = []

    def add(self, object):
        self.objects.append(object)

    def step(self, dt):
        for object in self.objects:
            object.step(dt)