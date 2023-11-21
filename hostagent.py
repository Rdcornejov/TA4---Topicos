import sys
import threading
import time
from PySide6.QtWidgets import QApplication
from pade.acl.aid import AID
from pade.behaviours.protocols import TimedBehaviour
from pade.misc.utility import start_loop
from carritoAgent import CarritoAgent
from pade.core.agent import Agent

from globals import Global
from gui import Gui

class TimeColision(TimedBehaviour):
    def __init__(self, agent, time):
        super(TimeColision, self).__init__(agent, time)
        self.agent = agent
    
    def on_time(self):
        super(MyTimedBehaviour, self).on_time()
        for fish in self.agent.fish_list:
            fish.detect_collision(self.agent.fish_list)

class MyTimedBehaviour(TimedBehaviour):
    def __init__(self, agent, time):
        super(MyTimedBehaviour, self).__init__(agent, time)
        self.agent = agent

    def on_time(self):
        super(MyTimedBehaviour, self).on_time()
        gui.update()

class movimientoCarro(TimedBehaviour):
    def __init__(self, agent, time):
        super(movimientoCarro, self).__init__(agent, time)
        self.agent = agent

    def on_time(self):
        super(movimientoCarro, self).on_time()
        self.agent.updateStatus()
        self.agent.swim()

class HostAgent(Agent):
    gui = None
    num_fishes = 20
    fish_list = []
    enabled = False
    agents = []
    port = int(sys.argv[1])
    def __init__(self, aid, agents):
        super(HostAgent, self).__init__(aid=aid, debug=False)
        self.agents = agents
        Global.x_center = 0

        for i in range(self.num_fishes):
            pes_agent_name = 'pes_agent_{}@localhost:{}'.format(port+i, port+i)
            fish = CarritoAgent(AID(name=pes_agent_name))
            self.fish_list.append(fish)
            self.behaviours.append(movimientoCarro(fish, .2))
            self.agents.append(fish)

        mytimed = MyTimedBehaviour(self, .2)
        self.behaviours.append(mytimed)    

def agentsexec():
    start_loop(agents)

if __name__ == '__main__':
    agents = list()
    port = int(sys.argv[1])
    host_agent_name = 'host_agent_{}@localhost:{}'.format(port+1000, port+1000)
    host_agent = HostAgent(AID(name=host_agent_name), agents)
    agents.append(host_agent)

    x = threading.Thread(target=agentsexec)
    x.start()
    app = QApplication([])
    gui = Gui(host_agent)
    gui.show()
    app.exec()
    x.join()
