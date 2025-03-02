from core.System import System

class Network (System):
  def getAddrs(self):
    self.NIC_INFO = self.system.net_if_addrs()
    for nic in self.NIC_INFO:
      addrs = self.formatAddrs(self.NIC_INFO[nic])
      print("{0}:\n{1}".format(nic, addrs))

  def getCounters(self):
    self.COUNTERS = self.system.net_io_counters(pernic=True)
    for (nic, c) in self.COUNTERS.items():
      print("""{0}:
    Байтів надіслано: {1.bytes_sent}
    Байтів отримано: {1.bytes_recv}
    Пакетів надіслано: {1.packets_sent}
    Пакетів отримано: {1.packets_recv}
    Помилки (IN|OUT): {1.errin}|{1.errout}
    Відкинуті пакети (INT|OUT): {1.dropin}|{1.dropout}\n""".format(nic, c))

    
  def formatAddrs(self, info):
    formatedStr = ""
    for i in info:
      if i.family == 2:
        formatedStr += "IPv4: {0.address}\n {0.netmask}\n".format(i)
      
      if i.family == 10:
        formatedStr += "IPv6: {0.address}\n {0.netmask}\n".format(i)
      
      if i.family == 17:
        formatedStr += "MAC: {0.address}\n".format(i)
    return formatedStr        


