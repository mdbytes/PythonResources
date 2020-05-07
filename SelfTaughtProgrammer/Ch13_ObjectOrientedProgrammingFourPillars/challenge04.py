class Rider:
    name: str

    def __init__(self, n: str):
        self.name = n


class Horse:
    name: str
    rider: Rider

    def __init__(self, n: str, r: Rider):
        self.name = n
        self.rider = r


def app():
    martin = Rider("Martin")
    trigger = Horse("Trigger", martin)
    print("You have constructed a horse named {} with a rider named {}".format(trigger.name, trigger.rider.name))


if __name__ == "__main__":
    app()
