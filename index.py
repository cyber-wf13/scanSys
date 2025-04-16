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
cli.addScenario('-cu', '--cpu-use', methodParams={'name': cpu.getUsage}, help = 'Використання CPU', nargs='?', const=False)
cli.addScenario('-ct', '--cpu-times', methodParams={'name': cpu.getTimes}, help = 'Час використання CPU', nargs='?', const=False)
cli.addScenario('-cc', '--cpu-count', methodParams={'name': cpu.getCount}, help = 'Кількість фізичних ядер CPU', nargs='?', const=False)
cli.addScenario('-cf', '--cpu-freq', methodParams={'name': cpu.getFreq}, help = 'Поточна частота CPU', nargs='?', const=False)
cli.addScenario('-na', '--net-addr', throwUserArg=False, methodParams={'name': net.getAddrs}, help = 'IP адреси призначені на інтерфейсах', nargs='?', const=False)
cli.addScenario('-nc', '--net-count', methodParams={'name': net.getCounters}, help = 'Статистика мережевих інтерфейсів', nargs='?', const=False, throwUserArg=False)
cli.addScenario('-mc', '--mem-count', methodParams={'name': mem.getCounters}, help = 'Використання RAM', nargs='?', const=False, throwUserArg=False)
cli.addScenario('-dp', '--disk-part', methodParams={'name': disk.getParts}, help = 'Доступні диски', nargs='?', const=False, throwUserArg=False)
cli.initArgs()
cli.start()