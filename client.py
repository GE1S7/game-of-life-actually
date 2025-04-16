import struct
from grid import Grid
from twisted.internet.protocol import Protocol, ClientFactory

class PlayerClient(Protocol):

    def __init__(self, factory):
        self.factory = factory

    def dataReceived(self, data):
        fmt = "!" + "i" * 32 * 32
        grid_values = struct.unpack(fmt, data)
        #print(grid_values)
        conv_grid = {}

        DEAD = "░"
        ALIVE = "█"

        i = 0
        for x in range(0, 32):

            for y in range(0,32):

                if grid_values[i] == 0:
                    self.factory.grid.grid_list[(x,y)] = DEAD

                elif grid_values[i] == 1:
                    self.factory.grid.grid_list[(x,y)] = ALIVE
                    #print(conv_grid[(x,y)])

                i += 1
        #print(conv_grid.values())
        #print(len(conv_grid.values()))
        #print(self.factory.grid.grid_list)
        #print(self.factory.grid.grid_list)
        #print("inprotocol gridlist id:", id(self.factory.grid.grid_list))

class PlayerClientFactory(ClientFactory):

    def __init__(self):
        self.grid = Grid(32,32)
        self.grid.init_grid()
        #print("infactory gridlist_id", id(self.grid.grid_list))

    def startedConnecting(self, connector):
        print('Started to connect.')

    def buildProtocol(self, addr):
        print('Connected')
        return PlayerClient(self)

    def clientConnectionLost(self, connector, reason):
        print('Lost connection. Reason:', reason)

    def clientConnectionFailed(self, connector, reason):
        print('Connection failed. Reason:', reason)

    def passGrid(self):
        return self.grid
        


