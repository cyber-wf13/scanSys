from app.Console import Console
from core.System import System
from core.interfaces.Cpu import Cpu
from core.interfaces.Disk import Disk
from core.interfaces.Memory import Memory
from core.interfaces.Network import Network

sys = System()
cpu = Cpu()
mem = Memory()
disk = Disk()
net = Network()
con = Console()
con.addScenario('cpu', [cpu.getUsage, 'test', {'t': 1}, 4], '(cpu) Використання CPU')
con.addScenario('mem', [mem.getMem], '(mem) Використання ОЗУ')
# con.addScenario('test', cpu.getUsage, '(ss) Використання CPU')
con.start()

# print(cpu.USAGE, cpu.COUNT, cpu.FREQ)
# print(mem.VIRT)
# print(repr(disk.PATR))
# print(net.NIC_INFO)


# if (args.getValue('cpu', False)):
#   print (CPU_USAGE, CPU_COUNT, CPU_FREQ)

# if (args.getValue('mem', False)):
#   print(MEM_VIRT)

# if (args.getValue('disk', False)):
#   for disk in DISK_PATR:
#     print(disk.device)

# if (args.getValue('n', False)):
#   print(USERS)
  