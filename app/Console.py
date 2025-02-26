class Console:
  def __init__(self):
    self.helloBanner = 'Інтерактивний сеанс. Виберіть доступний пункт\n'
    self.banner = ''
    self.userInput = ''
    self.scenarios = {'bye': {'method': self.bye, 'args': []}}

  def execScenarios(self):
    key = str.lower(self.userInput) 
    if key in self.scenarios:
#      print('Scene: ' + key)
      self.scenarios[key]['method'](*self.scenarios[key]['args'])

  def addScenario(self, key, method, banner):
    self.updateHelloBanner(banner)
    self.scenarios[key] = {}
    self.scenarios[key]['method'] = method[0]
    if len(method) > 1:
      self.scenarios[key]['args'] = method[1:]
    else:
      self.scenarios[key]['args'] = []

    
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
    self.printBanner('GoodBye')
    quit()

  # def test(self):
  #   self.printBanner('test string')
  #   print(repr(self.scenarios))
