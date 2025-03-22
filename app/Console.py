from app.CLI import CLI

class Console (CLI):
  def __init__(self):
    CLI.__init__(self)
    self.helloBanner = 'Інтерактивний сеанс. Виберіть доступний пункт'
    self.banner = ''
    self.userInput = ''
    self.addScenario('-i', '--inter', help = 'Працювати в інтерактивному режимі', action='store_true')
    self.addScenario('-b', '--bye', help = 'Завершити', action='store_true', methodParams={'name': self.bye})

  def execScenario(self):
    if self.userInput in self.args:
      self.args[self.userInput] = True
    CLI.execScenario(self)
    self.args[self.userInput] = False
    
      
  def addScenario(self, *args, methodParams = None, **kwargs):
    bannerText = "({0}){1}".format(self.getKeyFromArgs(args[1]), kwargs['help'])
    self.updateHelloBanner(bannerText)
    CLI.addScenario(self, *args, methodParams=methodParams, **kwargs)
  
  def start(self):
    while True:
      try:
        self.userInput = str.lower(input(self.helloBanner + '\n'))
        self.execScenario()
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