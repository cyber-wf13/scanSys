from core.System import System

class Disk (System):
  def getParts(self):
    self.PARTS = self.system.disk_partitions()
    for part in self.PARTS:
      print("""{0.device}
  Точка монтування: {0.mountpoint}
  Файлова система: {0.fstype}
  Додаткові опції: {0.opts}""".format(part))

