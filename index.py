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
  