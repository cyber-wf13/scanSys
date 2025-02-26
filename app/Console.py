class Console:
  def __init__(self):
    self.helloBanner = 'Інтерактивний сеанс. Виберіть доступний пункт\n(bye) Завершити'
    self.banner = ''
    self.userInput = ''
    self.scenarios = {'test': self.test, 'bye': self.bye}

  def execScenarios(self):
    key = str.lower(self.userInput) 
    if key in self.scenarios:
      print('Scene: ' + key + '\n')
      self.scenarios[key]()

  def addScenario(self, key, method, banner):
    self.updateHelloBanner(banner)
    self.scenarios[key] = method  
    
  def start(self):
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

  def test(self):
    self.printBanner('test string')
    print(repr(self.scenarios))
