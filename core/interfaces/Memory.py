from core.System import System

class Memory (System):
  def __init__(self):
    System.__init__(self)
    self.VIRT = self.system.virtual_memory()
