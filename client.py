import struct
from grid import Grid
from twisted.internet.protocol import Protocol, ClientFactory

class PlayerClient(Protocol):
    def dataReceived(self, data):
        fmt = "!" + "c" * 32
        grid_values = struct.unpack(fmt, data)
        print(grid_values)

class PlayerClientFactory(ClientFactory):
    def startedConnecting(self, connector):
        print('Started to connect.')

    def buildProtocol(self, addr):
        print('Connected')
        return PlayerClient()

    def clientConnectionLost(self, connector, reason):
        print('Lost connection. Reason:', reason)

    def clientConnectionFailed(self, connector, reason):
        print('Connection failed. Reason:', reason)

from twisted.internet import reactor

plug = PlayerClientFactory()
reactor.connectTCP("localhost", 1234, plug) 
reactor.run()
