
from Ch3_BasicDataStructures.Ch3_07_Queue import Queue

# Simulation Game
# Ten players playing the game
nameList = ["Bill","David","Susan","Jane","Kent","Brad","Mark","Gina","Jenny","Lora"]
potatoPasses = 12

def hotPotato(playerList, passes):
    gameQueue = Queue()

    for name in playerList:
        gameQueue.enqueue(name)

    print(gameQueue.items)

    # Each iteration will
    for i in range(passes):
        gameQueue.enqueue(gameQueue.dequeue())

    return gameQueue.dequeue()

print(hotPotato(nameList,potatoPasses))
