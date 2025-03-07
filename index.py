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
con.addScenario('cpu_times', cpu.getTimes, '(cpu_times) Час використання CPU', False)
con.addScenario('cpu_count', cpu.getCount, '(cpu_count) Кількість фізичних ядер CPU')
con.addScenario('cpu_freq', cpu.getFreq, '(cpu_freq) Поточна частота CPU', True)
con.addScenario('net_addr', net.getAddrs, '(net_addr) IP адреси призначені на інтерфейсах')
con.addScenario('net_count', net.getCounters, '(net_count) Статистика мережевих інтерфейсів')
con.addScenario('mem_count', mem.getCounters, '(mem_count) Використання RAM')
con.addScenario('disk_part', disk.getParts, '(disk_part) Доступні диски')

con.addCliScenario('-i', '--inter', help = 'Працювати в інтерактивному режимі', action='store_true')
con.addCliScenario('-cu', '--cpu-use', help = 'Використання CPU', action='store_true')
con.addCliScenario('-ct', '--cpu-times', help = 'Час використання CPU', action='store_true')
con.addCliScenario('-cc', '--cpu-count', help = 'Кількість фізичних ядер CPU', action='store_true')
con.addCliScenario('-cf', '--cpu-freq', help = 'Поточна частота CPU', action='store_true')
con.addCliScenario('-na', '--net-addr', help = 'IP адреси призначені на інтерфейсах', action='store_true')
con.addCliScenario('-nc', '--net-count', help = 'Статистика мережевих інтерфейсів', action='store_true')
con.addCliScenario('-mc', '--mem-count', help = 'Використання RAM', action='store_true')
con.addCliScenario('-dp', '--disk-part', help = 'Доступні диски', action='store_true')
con.initCLIArgs()

if con.argsCLI['inter']:
  con.start()
else:
  con.execCLIScenario()

