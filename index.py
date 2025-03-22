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

cli.start()