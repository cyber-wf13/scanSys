from core.System import System

class Memory (System):
  def getCounters(self):
    self.VIRT = self.system.virtual_memory()
    memInfo = {'total': self.VIRT.total, 'available': self.VIRT.available, 'percent': self.VIRT.percent}
    self.updateAndPrintResult(memInfo, 'mem_count', "Загалом: {0.total}\n Вільна: {0.available}\n Відсоток використання: {0.percent}".format(self.VIRT))