class Console:
  def __init__(self):
    self.helloBanner = 'Інтерактивний сеанс. Виберіть доступний пункт'
    self.banner = ''
    self.userInput = ''
    self.scenarios = {'bye': {'method': self.bye, 'args': [], 'kwargs': {}, 'cli': None}}
    print('console: ', repr(self.scenarios))

  def execScenarios(self):
    key = str.lower(self.userInput) 
    if key in self.scenarios:
      self.scenarios[key]['method'](*self.scenarios[key]['args'], **self.scenarios[key]['kwargs'])
      
  def addScenario(self, key, method, banner, *args, cli = None, **kwargs):
    self.updateHelloBanner(banner)
    self.scenarios[key] = {}
    self.scenarios[key]['method'] = method
    self.scenarios[key]['args'] = args 
    self.scenarios[key]['kwargs'] = kwargs 
    self.scenarios[key]['cli'] = cli or key
  
  def start(self):
    self.updateHelloBanner('(bye) Завершити')
    while True:
      try:
        self.userInput = input(self.helloBanner + '\n')
        self.execScenarios()
      except KeyboardInterrupt:
        print('Процес завершений перериванням через клавіатуру (CTRL + C)')
        quit()

  def printBanner(self, text):
    self.banner = text
    print(self.banner)
  
  def updateHelloBanner(self, text):
    self.helloBanner += '\n' + text

  def bye(self):
    self.printBanner('Good Bye')
    quit()