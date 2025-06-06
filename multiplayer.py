from twisted.internet import reactor
import client
from curses import wrapper
from twisted.internet.task import LoopingCall
from interface import interface
from threading import Thread
import time
from dotenv import load_dotenv
from os import getenv

load_dotenv()
IP = getenv("IP")
P = int(getenv("P"))


def loadInterface(interface, factory):
    wrapper(interface, factory)
    reactor.callFromThread(reactor.stop)


def run_client():
    host = IP
    port = P
    factory = client.PlayerClientFactory()
    thread = Thread(target=loadInterface, args=(interface, factory))
    reactor.connectTCP(host, port, factory)
    thread.start()
    reactor.run()


run_client()
