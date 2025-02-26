from core.System import System

class Cpu (System):
  def __init__(self):
    System.__init__(self)

    self.USAGE = self.system.cpu_percent(interval=0.1, percpu=True)
    self.TIMES = self.system.cpu_times()
    self.COUNT = self.system.cpu_count(logical=False)
    self.FREQ = self.system.cpu_freq()

  def getUsage(self, test, testDict, t2):
    print(repr(self.USAGE[0]))
    print(test, testDict['t'], t2)