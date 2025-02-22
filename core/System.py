import psutil
from modules.system.CommandArgs import CommandArgs

class System:
  def __init__(self):
    self.args = CommandArgs("Отримання інформації про систему. За замовчуванням, використані опції -cmdn")
    self.args.setCommand({'params': ['-c', '--cpu'], 'subParams': {'help': 'Вивести інформацію про CPU', 'action': 'store_false'}})
    self.args.setCommand({'params': ['-m', '--mem'], 'subParams': {'help': "Вивести інформацію про використання пам'яті", 'action': 'store_false'}})
    self.args.setCommand({'params': ['-d', '--disk'], 'subParams': {'help': "Вивести інформацію про наявні диски", 'action': 'store_false'}})
    self.args.setCommand({'params': ['-n', '--net'], 'subParams': {'help': "Вивести інформацію про мережу", 'action': 'store_false'}})
    self.args.initCommandArgs()

    self.system = psutil

