import struct
from grid import Grid
from twisted.internet.protocol import Factory 
from twisted.internet.endpoints import TCP4ServerEndpoint
from twisted.internet import reactor
from twisted.internet.protocol import Protocol
from twisted.internet.task import LoopingCall
from twisted.internet import protocol, reactor, endpoints
import time

class GridMod(Protocol):
    def __init__(self,factory, grid):
        self.grid = grid
        self.factory = factory
        self.can_act = True

    """update grid state based on client's input and send it back with additional info"""
    def connectionMade(self):
        print("Player joined")
        self.factory.clients.append(self)
        print(self.factory.clients)
        self.player_id = len(self.factory.clients)
        self.sendGrid()
        # send initial state of the board 

    def connectionLost(self, reason):
        print(f"Lost connection to Player {self.player_id}, reason: {reason}")
        self.factory.clients.remove(self)

    def dataReceived(self, data):
        if self.can_act == True:
            x, y = struct.unpack("!ii", data) # receive cell coordinates
            self.grid.edit(x,y)

    def sendGrid(self):
        grid_now = list(self.grid.grid_list.values())
        
        fmt = "!" + "i" * self.grid.width * self.grid.height
        data = struct.pack(fmt, *grid_now)
        self.transport.write(data)


class GridModFactory(protocol.Factory):
    def __init__(self):
        self.grid = Grid(256,256)
        self.grid.init_grid()
        self.grid.randomize()
        self.clients = []
    #create the grid here
    #pass it to the protocol
    def buildProtocol(self, addr):
        return GridMod(self, self.grid)


def server_loop(factory):
    factory.grid.c_eval()
    for client in factory.clients:
        client.sendGrid()
    # print(factory.grid.grid_list.values())
    time.sleep(0.1)

        


def main():
    factory = GridModFactory()
    factory.protocol = GridMod
    fmt = "!" + "c" * factory.grid.width * factory.grid.height
    looping_call = LoopingCall(server_loop, (factory))
    loopDeferred = looping_call.start(0.05)
    endpoints.serverFromString(reactor, "tcp:1234").listen(factory)
    reactor.run()


        



    # send info about width
    



if __name__ == "__main__":
    main()



