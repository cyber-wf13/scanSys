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
con.addScenario('cpu_use', cpu.getUsage, '(cpu_use) Використання CPU', False)
con.addScenario('cpu_times', cpu.getTimes, '(cpu_times) Час використання CPU', True)
con.addScenario('cpu_count', cpu.getCount, '(cpu_count) Кількість фізичних ядер CPU')
con.addScenario('cpu_freq', cpu.getFreq, '(cpu_freq) Поточна частота CPU', True)
con.addScenario('net_addr', net.getAddrs, '(net_addr) IP адреси призначені на інтерфейсах')
con.addScenario('net_count', net.getCounters, '(net_count) Статистика мережевих інтерфейсів')
con.addScenario('mem_count', mem.getCounters, '(mem_count) Використання RAM')
con.addScenario('disk_part', disk.getParts, '(disk_part) Доступні диски')
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
  