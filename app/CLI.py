from argparse import ArgumentParser
from sys import argv

class CLI:
  def __init__(self):
    self.parser = ArgumentParser(description='Отримання інформації про систему')
    self.args = None
    self.argsCount = len(argv) - 1 
    self.scenarios = {}

  def initArgs(self):
    self.args = vars(self.parser.parse_args())

  def execScenario(self):
    for key,val in self.args.items():
      if key in self.scenarios and  val != (False and None):
        self.scenarios[key]['method'](*self.scenarios[key]['args'], **self.scenarios[key]['kwargs'])
  
  def addScenario(self, *args, methodParams = None, **kwargs):
    self.parser.add_argument(*args, **kwargs)
    key = self.getKeyFromArgs(args[1])
    if methodParams:
      self.scenarios[key] = {}
      self.scenarios[key]['method'] = methodParams['name']
      self.scenarios[key]['args'] = methodParams['args'] if 'args' in methodParams else []     
      self.scenarios[key]['kwargs'] = methodParams['kwargs'] if 'kwargs' in methodParams else {}

  def getKeyFromArgs(self, argStr):
    return argStr[2:].replace('-', '_')