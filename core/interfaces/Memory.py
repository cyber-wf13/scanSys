from core.System import System

class Memory (System):
  def getCounters(self):
    self.VIRT = self.system.virtual_memory()
    print("Загалом: {0.total}\n Вільна: {0.available}\n Відсоток використання: {0.percent}".format(self.VIRT))