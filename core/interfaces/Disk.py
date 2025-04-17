from core.System import System

class Disk (System):
  def getParts(self):
    self.PARTS = self.system.disk_partitions()
    disks = []
    formattedStr = ""
    for part in self.PARTS:
      diskInfo = {"mountpoint": part.mountpoint, "fstype": part.fstype, "opts": part.opts} 
      disk = {"name": part.device, "info": diskInfo}
      disks.append(disk)
      formattedStr += """{0.device}
        Точка монтування: {0.mountpoint}
        Файлова система: {0.fstype}
        Додаткові опції: {0.opts}
      """.format(part)

    self.updateAndPrintResult(disks, 'disk_part', formattedStr)

