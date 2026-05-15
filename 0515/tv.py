class Television:
    def __init__(self, channel, volume, on=False):
        self.channel = channel
        self.volume = volume
        self.on = on
    def show(self):
        print(self.channel, self.volume, self.on)
    def setChannel(self, channel):
        self.channel = channel
    def getChannel(self):
        return self.channel
    
tv1 = Television(9, 10, True)
tv2 = Television(6, 15)
tv1.show()
tv1.setChannel(3)
tv1.show()
tv2.show()
print(tv1.getChannel())