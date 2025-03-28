from argparse import ArgumentParser
from sys import argv

class CLI:
  def __init__(self):
    self.parser = ArgumentParser(description='Отримання інформації про систему')
    self.args = None
    self.argsCount = len(argv) - 1 
    self.scenarios = {}

  """ 
    Отримання аргументів в якості словника. Цей метод повинен завжди бути останній, після 
    додвання команд через CLI.addScenario
  """
  def initArgs(self):
    self.args = vars(self.parser.parse_args())

  """ 
    Виконання сценараїів - перевірка на наявність значення в словнику аргументів 
  """
  def execScenario(self):
    for key,val in self.args.items():
      if key in self.scenarios and  val != (False and None):
        self.scenarios[key]['method'](*self.scenarios[key]['args'], **self.scenarios[key]['kwargs'])
  
  """ 
    Додавання сценарції. Всі аргументи будуть передані безпосередньо
    до об'єкту ArgumentParser.
    Аргумент methodParams дозволяє прив'язати метод до переданого аргументу.
    Ключі args та kwargs в аргументі methodParams виступають, як передані аргументи для методу
  """
  def addScenario(self, *args, methodParams = None, **kwargs):
    self.parser.add_argument(*args, **kwargs)
    key = self.getKeyFromArgs(args[1])
    if methodParams:
      self.scenarios[key] = {}
      self.scenarios[key]['method'] = methodParams['name']
      self.scenarios[key]['args'] = methodParams['args'] if 'args' in methodParams else []     
      self.scenarios[key]['kwargs'] = methodParams['kwargs'] if 'kwargs' in methodParams else {}

  """ 
    Дане перетворення дозволяє коректно створювати ключі для сценаріїв
  """
  def getKeyFromArgs(self, argStr):
    return argStr[2:].replace('-', '_')