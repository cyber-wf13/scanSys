import json
from app.CLI import CLI
from core.System import System

class Network (System):
  def getAddrs(self):
    self.NIC_INFO = self.system.net_if_addrs()
    addrInfo = self.formatAddrs()
    self.updateAndPrintResult(addrInfo, 'net_addr', addrInfo)

  # TODO: Реалізувати представлення в JSON. Як приклад - Disk.getParts
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

    
  def formatAddrs(self):
    formatedStr = ""
    addrInfo = []
    for nic in self.NIC_INFO:
      addrInfoByIface = {'name': nic, 'IPv4': None, 'IPv6': None, 'MAC': None}
      formatedStr += "{0}:\n".format(nic)
      for iface in self.NIC_INFO[nic]:
        if iface.family == 2:
          formatedStr += "IPv4: {0.address}\n {0.netmask}\n".format(iface)
          addrInfoByIface["IPv4"] = {"address": iface.address, "netmask": iface.netmask}
      
        if iface.family == 10:
          formatedStr += "IPv6: {0.address}\n {0.netmask}\n".format(iface)
          addrInfoByIface["IPv6"] = {"address": iface.address, "netmask": iface.netmask}
      
        if iface.family == 17:
          formatedStr += "MAC: {0.address}\n".format(iface)
          addrInfoByIface["MAC"] = iface.address
      
      addrInfo.append(addrInfoByIface)
    if CLI.toJson:
      return addrInfo
    return formatedStr        


