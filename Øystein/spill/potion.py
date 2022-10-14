import item, ioutil

# TODO: Få dette til å funke
class Potion(item.Item):
    def __init__(self, name, info, consume, deconsume) -> None:
        super().__init__(name)
        self.info = info
        self.consumable = True
        self.consume = consume
        self.deconsume = deconsume

    def print_info(self):
        ioutil.slow(self.info)