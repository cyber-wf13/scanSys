from app.CLI import CLI
from core.System import System

class Cpu (System):
  def getUsage(self, percpu = False):
    self.USAGE = self.system.cpu_percent(interval=0.1, percpu=percpu)
    if percpu:
      formatedStr = "Використання ядра {0}: {1}\n"
      cpuInfoByCore = self.getInfoPerCpu(self.USAGE, formatedStr)
      self.updateAndPrintResult(cpuInfoByCore, 'cpu_usage', cpuInfoByCore)
    else:
      self.updateAndPrintResult(self.USAGE, 'cpu_usage', "Використання ядра: " + str(self.USAGE))
      
  def getTimes(self, percpu = False):
    self.TIMES = self.system.cpu_times(percpu)
    if percpu:
      formattedStr = "Витрачений час в ядрі {0} в секундах за процесами:\n користувача (user) {1.user}\n системи (system) {1.system}\n простоювання (idle) {1.idle}\n"
      cpuInfoByCore = self.getInfoPerCpu(self.TIMES, formattedStr)
      self.updateAndPrintResult(cpuInfoByCore, 'cpu_times', cpuInfoByCore)
    else:
      formattedStr = "Витрачений час в секундах на процеси користувача (user): %s, системи (system): %s та простоювання (idle): %s" % (self.TIMES.user, self.TIMES.system, self.TIMES.idle)
      self.updateAndPrintResult(self.TIMES, 'cpu_times', formattedStr)
    
  def getInfoPerCpu(self, cpuInfo, message):
    cpuCount = len(cpuInfo)
    formattedStr = "Загальна кількість ядер: %s\n" % cpuCount
    cpuInfoByCore = {}
    for core in range(cpuCount):
      humanViewCore = core + 1
      cpuInfoByCore[humanViewCore] = cpuInfo[core]
      formattedStr += message.format(humanViewCore, cpuInfo[core])
    if CLI.toJson:
      return cpuInfoByCore
    return formattedStr
      

  def getCount(self, logical = False):
    self.COUNT = self.system.cpu_count(logical=logical)
    self.updateAndPrintResult(self.COUNT, 'cpu_count', "Кількість ядер: {0}".format(self.COUNT))

  def getFreq(self, percpu = False):
    self.FREQ = self.system.cpu_freq(percpu=percpu)
    if percpu:
      formatedStr = "Поточна частота процесора (Mhz) {0}: {1.current}\n Мінімальна: {1.min} Максимальна: {1.max}"
      cpuInfoByCore = self.getInfoPerCpu(self.FREQ, formatedStr)
      self.updateAndPrintResult(cpuInfoByCore, 'cpu_freq', cpuInfoByCore)
    else:
      self.updateAndPrintResult(self.FREQ, 'cpu_freq', "Поточна частота процесора (Mhz): {0.current}".format(self.FREQ))
    