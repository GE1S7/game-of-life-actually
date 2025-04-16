from twisted.internet import reactor
import client
from curses import wrapper
from twisted.internet.task import LoopingCall
from interface import interface 

def loadInterface(factory, interface):
    wrapper(interface, factory)


def run_client():
    factory = client.PlayerClientFactory()
    #LoopingCall(lambda: print(factory.grid.grid_list.values())).start(1.0)
    LoopingCall(wrapper, interface, factory).start(0)
    #reactor.callLater(0, wrapper, interface, factory)
    reactor.connectTCP("localhost", 1234, factory) 
    reactor.run()

run_client()
