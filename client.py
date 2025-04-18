import struct
from grid import Grid
from twisted.internet.protocol import Protocol, ClientFactory
from sys import getsizeof
class PlayerClient(Protocol):

    def __init__(self, factory):
        self.factory = factory
        self.buffer = b''
        factory.client.append(self)

    def dataReceived(self, data):
        self.buffer += data 
        while len(self.buffer) >= self.factory.buffer_size:
            chunk = self.buffer[:self.factory.buffer_size]
            buffer = self.buffer[self.factory.buffer_size:]
            fmt = "!" + "i" * self.factory.grid.width * self.factory.grid.height
            grid_values = struct.unpack(fmt, chunk)
            self.buffer = b''
            #print(grid_values)
            conv_grid = {}

            DEAD = "░"
            ALIVE = "█"

            i = 0
            for x in range(0, self.factory.grid.width):

                for y in range(0,self.factory.grid.height):

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

    def sendCoord(self, x, y):
        coord = struct.pack("!ii", x, y)
        self.transport.write(coord)


class PlayerClientFactory(ClientFactory):

    def __init__(self):
        self.grid = Grid(64,64)
        self.buffer_size = self.grid.width * self.grid.height * 4
        self.grid.init_grid()
        self.client = []
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




