from argparse import ArgumentParser
from sys import argv

class CLI:
  def __init__(self):
    self.parser = ArgumentParser(description='Отримання інформації про систему')
    self.args = None
    self.argsCount = len(argv) - 1 
    self.scenarios = {}
    self.addScenario('-i', '--inter', help = 'Працювати в інтерактивному режимі', action='store_true')

  def initArgs(self):
    self.args = vars(self.parser.parse_args())
    print(self.scenarios)

  def execScenario(self):
    for key,val in self.args.items():
      # if key in self.scenarios and val != (None and False):
      if val != (False and None):
        self.scenarios[key]['method'](*self.scenarios[key]['args'], **self.scenarios[key]['kwargs'])
        # elif key in self.defaultArgsCLI and key 
  
  def addScenario(self, *args, methodParams = None, **kwargs):
    self.parser.add_argument(*args, **kwargs)
    key = args[1][2:].replace('-', '_')
    if methodParams:
      self.scenarios[key] = {}
      self.scenarios[key]['method'] = methodParams['name']
      self.scenarios[key]['args'] = methodParams['args'] if 'args' in methodParams else []     
      self.scenarios[key]['kwargs'] = methodParams['kwargs'] if 'kwargs' in methodParams else {}