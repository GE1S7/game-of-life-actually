from twisted.internet import reactor
import client
from curses import wrapper
from twisted.internet.task import LoopingCall
from interface import interface 
from threading import Thread
import time

def loadInterface(factory, interface):
    while True:
        wrapper(interface, factory)


def run_client():
    host = input("host ip: ")
    port = int(input("port : "))
    factory = client.PlayerClientFactory()
    thread = Thread(target = wrapper, args = (interface, factory)) 
    thread.start()
    #LoopingCall(lambda: print(factory.grid.grid_list.values())).start(1.0)
    #LoopingCall(wrapper, interface, factory).start(0)
    #reactor.callLater(0, wrapper, interface, factory)
    reactor.connectTCP(host, port, factory) 
    reactor.run()

run_client()
