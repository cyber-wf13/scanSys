from argparse import ArgumentParser
from sys import argv

class CLI:
  toJson = False
  formattedJson = {}
  
  def __init__(self):
    self.parser = ArgumentParser(description='Отримання інформації про систему')
    self.args = None
    self.argsCount = len(argv) - 1 
    self.scenarios = {}
    self.addScenario('-j', '--json', action='store_true', onlyCLI=True, methodParams={'name': self.setOuputToJson}, help = 'Збереження результатів у форматі json')
  
  def setOuputToJson(self, toJson):
    print('set to json', toJson)
    CLI.toJson = toJson

  def updateFormattedJson(json):
    CLI.formattedJson = json

  def print(*values):
    print(CLI.toJson)
    if CLI.toJson:
      print('save to json', CLI.formattedJson)
    else:
      print(*values)


  """ 
    Отримання аргументів в якості словника. Цей метод повинен завжди бути останній, після 
    додвання команд через CLI.addScenario
  """
  def initArgs(self):
    self.args = vars(self.parser.parse_args())
    print(self.args)

  """ 
    Виконання сценараїів - перевірка на наявність значення в словнику аргументів 
    Також виконується перевірка чи потрібно передавати в метод значення користувача
  """
  def execScenario(self):
    for key,val in self.args.items():
      if key in self.scenarios and  val != None:
        if self.scenarios[key]['userArg']:
          self.scenarios[key]['method'](self.args[key], *self.scenarios[key]['args'], **self.scenarios[key]['kwargs'])
        else:
          self.scenarios[key]['method'](*self.scenarios[key]['args'], **self.scenarios[key]['kwargs'])
          
  
  """ 
    Додавання сценарції. Всі аргументи будуть передані безпосередньо
    до об'єкту ArgumentParser.
    Аргумент methodParams дозволяє прив'язати метод до переданого аргументу.
    Параметр throwUserArg повідомляє чи потрібно передавати аргумент користувача до методу
    Ключі args та kwargs в аргументі methodParams виступають, як передані аргументи для методу
  """
  def addScenario(self, *args, methodParams = None, throwUserArg = True, **kwargs):
    self.parser.add_argument(*args, **kwargs)
    key = self.getKeyFromArgs(args[1])
    if methodParams:
      self.scenarios[key] = {}
      self.scenarios[key]['method'] = methodParams['name']
      self.scenarios[key]['args'] = methodParams['args'] if 'args' in methodParams else []     
      self.scenarios[key]['kwargs'] = methodParams['kwargs'] if 'kwargs' in methodParams else {}
      self.scenarios[key]['userArg'] = throwUserArg if throwUserArg else None

  """ 
    Дане перетворення дозволяє коректно створювати ключі для сценаріїв
  """
  def getKeyFromArgs(self, argStr):
    return argStr[2:].replace('-', '_')