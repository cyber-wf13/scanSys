from core.System import System

class Network (System):
  def __init__(self):
    System.__init__(self)  
    self.COUNTERS = self.system.net_io_counters()
    self.CONNECT = self.system.net_connections()
    self.NIC_INFO = self.system.net_if_addrs()
