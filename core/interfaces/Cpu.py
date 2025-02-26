from core.System import System

class Cpu (System):
  def getUsage(self, percpu = False):
    self.USAGE = self.system.cpu_percent(interval=0.1, percpu=percpu)
    if percpu:
      formatedStr = "Використання ядра {0}: {1}"
      self.getInfoPerCpu(self.USAGE, formatedStr)
    else:
      print("Використання ядра: " + str(self.USAGE))
      
  def getTimes(self, percpu = False):
    self.TIMES = self.system.cpu_times(percpu)
    if percpu:
      formattedStr = "Витрачений час в ядрі {0} в секундах за процесами:\n користувача (user) {1.user}\n системи (system) {1.system}\n простоювання (idle) {1.idle}"
      self.getInfoPerCpu(self.TIMES, formattedStr)
    else:
      print("Витрачений час в секундах на процеси користувача (user): %s, системи (system): %s та простоювання (idle): %s" 
            % (self.TIMES.user, self.TIMES.system, self.TIMES.idle))
    
  def getInfoPerCpu(self, cpuInfo, message):
    cpuCount = len(cpuInfo)
    print("Загальна кількість ядер: %s" % cpuCount)
    for core in range(cpuCount):
      humanViewCore = core + 1
      print(message.format(humanViewCore, cpuInfo[core]))

  def getCount(self, logical = False):
    self.COUNT = self.system.cpu_count(logical=logical)
    print("Кількість ядер: {0}".format(self.COUNT))

  def getFreq(self, percpu = False):
    self.FREQ = self.system.cpu_freq(percpu=percpu)
    if percpu:
      formatedStr = "Поточна частота процесора (Mhz) {0}: {1.current}\n Мінімальна: {1.min} Максимальна: {1.max}"
      self.getInfoPerCpu(self.FREQ, formatedStr)
    else:
      print("Поточна частота процесора (Mhz): {0.current}".format(self.FREQ))

      