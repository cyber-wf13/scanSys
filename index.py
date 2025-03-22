from app.CLI import CLI
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

# con.addScenario('cpu_use', cpu.getUsage, '(cpu_use) Використання CPU', False)
# con.addScenario('cpu_times', cpu.getTimes, '(cpu_times) Час використання CPU', False)
# con.addScenario('cpu_count', cpu.getCount, '(cpu_count) Кількість фізичних ядер CPU')
# con.addScenario('cpu_freq', cpu.getFreq, '(cpu_freq) Поточна частота CPU', True)
# con.addScenario('net_addr', net.getAddrs, '(net_addr) IP адреси призначені на інтерфейсах')
# con.addScenario('net_count', net.getCounters, '(net_count) Статистика мережевих інтерфейсів')
# con.addScenario('mem_count', mem.getCounters, '(mem_count) Використання RAM')
# con.addScenario('disk_part', disk.getParts, '(disk_part) Доступні диски')

cli = Console()
cli.addScenario('-cu', '--cpu-use', methodParams={'name': cpu.getUsage}, help = 'Використання CPU', action='store_true')
cli.addScenario('-ct', '--cpu-times', methodParams={'name': cpu.getTimes}, help = 'Час використання CPU', action='store_true')
cli.addScenario('-cc', '--cpu-count', methodParams={'name': cpu.getCount}, help = 'Кількість фізичних ядер CPU', action='store_true')
cli.addScenario('-cf', '--cpu-freq', methodParams={'name': cpu.getFreq}, help = 'Поточна частота CPU', action='store_true')
cli.addScenario('-na', '--net-addr', methodParams={'name': net.getAddrs}, help = 'IP адреси призначені на інтерфейсах', action='store_true')
cli.addScenario('-nc', '--net-count', methodParams={'name': net.getCounters}, help = 'Статистика мережевих інтерфейсів', action='store_true')
cli.addScenario('-mc', '--mem-count', methodParams={'name': mem.getCounters}, help = 'Використання RAM', action='store_true')
cli.addScenario('-dp', '--disk-part', methodParams={'name': disk.getParts}, help = 'Доступні диски', action='store_true')
cli.initArgs()

if cli.args['inter']:
  cli.start()
elif cli.argsCount == 0:
  cli.parser.print_help()
else:
  cli.execScenario()

