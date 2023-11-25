import sys
import threading
import time
from PySide6.QtWidgets import QApplication
from pade.acl.aid import AID
from pade.behaviours.protocols import TimedBehaviour
from pade.misc.utility import start_loop
from carAgent import CarAgent
from pade.core.agent import Agent

from globals import Global
from gui import Gui

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



class ControlAgent(Agent):
    gui = None
    num_cars = 100
    delay = .2
    port = int(sys.argv[1])
    cars = []
    def __init__(self, aid):
        super(ControlAgent, self).__init__(aid=aid, debug=False)
        c = 0
        for i in range(self.num_cars):
            c += 1
            car_agent_name = 'car_agent_{}@localhost:{}'.format(port + c, port + c)
            car_agent = CarAgent(AID(name=car_agent_name), self.delay)
            self.cars.append(car_agent)
        mytimed = MyTimedBehaviour(self, self.delay)
        self.behaviours.append(mytimed)

def agentsexec():
    start_loop(agents)

if __name__ == '__main__':
    agents = []
    port = int(sys.argv[1])
    control_agent_name = 'control_agent_{}@localhost:{}'.format(port, port)
    control_agent = ControlAgent(AID(name=control_agent_name))
    agents.append(control_agent)
    agents += control_agent.cars
    x = threading.Thread(target=agentsexec)
    x.start()
    app = QApplication([])
    gui = Gui(control_agent)
    gui.show()
    app.exec()
    x.join()