import random

class DrawError(Exception):
    pass

class drawPair():
    greetings = ['Oh shit', 'Congrats,', 'Tight, well done', 'Look at that, what a great draw', ]

    def __init__(self, secretSanta, recipient):
        self.is_price = False
        self.is_xavier = False
        self.secretSanta = secretSanta
        self.recipient = recipient
        if self.recipient == "Price":
            self.is_price = True
        if self.secretSanta == "Xavier":
            self.is_xavier = True


    def greeting(self):
        index = random.randint(0, (len(self.greetings)-1))
        return self.greetings[index]

    def writeCsv(self):
        filename = "{}_secret_santa_draw.txt".format(self.secretSanta)
        with open(filename, "w") as file:
            file.write(" ~~~ SECRET SANTA DRAWING 2017 ~~~\n")
            file.write(self.__str__())

    def __str__(self):
        string_suffix = ""
        if self.is_price:
            string_suffix += "\n(Great pick you got price, everyone will be very jealous this is very coveted!)"
        if self.is_xavier:
            string_suffix += "\n(My records indicate you are xavier and that price is 47 times " \
                            "doper than you could ever be)"
        return "{} {}! You are getting a gift for {}{}".format(self.greeting(), self.secretSanta,
                                                               self.recipient, string_suffix)


def draw(names):
    drawn_names = []
    shuffled_names = names
    for x in range(5):
        random.shuffle(shuffled_names)

    for name in shuffled_names:
        key = (shuffled_names.index(name) + 2)%len(shuffled_names)

        if shuffled_names[key] == name:
            raise DrawError("Someone got themselves for secret santa!")

        if shuffled_names[key] in drawn_names:
            raise DrawError("{} has already been drawn and already has a secret santa!".format(shuffled_names[key]))

        drawn_names.append(shuffled_names[key])


        d = drawPair(name, names[key])
        d.writeCsv()
    return drawn_names

def checklist(names, drawn_names):
    for name in names:
        if name not in drawn_names:
            raise DrawError("Oh no! {} never got drawn!".format(name))
    if len(drawn_names) < len(names):
        raise DrawError("Somehow less names got drawn then were given, run it again")
    elif len(drawn_names) > len(names):
        raise DrawError("Somehow more names got drawn then were given, don't know how that's possible")



def draw_names(names):
    drawn_names = draw(names)
    checklist(names, drawn_names)


if __name__ == "__main__":
    names = ["Price", "Adam", "Tommy", "Aaron", "Xavier", "Danna", "Christene", "Drisana", "Courtney", "Alex", "Codi"]
    draw_names(names)