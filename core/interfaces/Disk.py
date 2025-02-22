from core.System import System

class Disk (System):
  def __init__(self):
    System.__init__(self)
    self.PATR = self.system.disk_partitions()
