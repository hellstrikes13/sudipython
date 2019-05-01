import logging
#logging.basicConfig(level=logging.DEBUG)
logging.basicConfig(
        filename="pizza.log",
        level=logging.DEBUG,
        format="%(asctime)s:%(levelname)s:%(message)s"
        )
class Pizza():
    def __init__(self,name,price):
        self.name = name
        self.price = price
        logging.debug("Pizza created: {} Rate : ${}".format(self.name,self.price))

    def make(self,q= 1):
        logging.debug("Made : {} pizza(s)".format(q,self.name))

    def eat(self,q=1):
        logging.debug("ate : {} pizza(s)".format(q,self.name))
p1 = Pizza("BBQ chiken",4)
p1.make()
p1.eat()
p2 = Pizza("Thousand islands",5)
p2.make()
p2.eat()

