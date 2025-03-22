from app.CLI import CLI

class Console (CLI):
  def __init__(self):
    CLI.__init__(self)
    self.helloBanner = 'Інтерактивний сеанс. Виберіть доступний пункт'
    self.banner = ''
    self.userInput = ''
    self.addScenario('-i', '--inter', help = 'Працювати в інтерактивному режимі', action='store_true', onlyCLI=True)
    self.setByeMessage()
    """  
      Режим: 
      CLI - звичайне виконання програми в командному рядку 
      INTER - виконання програми в інтерактивному режимі, поки користувач не завершить роботу
    """
    self.mode = 'CLI'

  def initArgs(self):
    CLI.initArgs(self)
    if self.args['inter']:
      self.mode = 'INTER'

  """ 
    На основі вводу користувача виконується команда.
    Команда для завершення програми визначена окремим elif, щоб не опрацьовуатися основною логікою CLI
    Текст та повідомлення про завершення роботи можна змінити через setByeMessage
  """
  def execScenario(self):
    if self.userInput in self.args:
      self.args[self.userInput] = True
    elif self.userInput == self.byeTrigger:
      self.bye()
    CLI.execScenario(self)
    self.args[self.userInput] = False
    
  """ 
    Параметр onlyCLI дозволяє не відображати повідомлення в інтерактивній підсказці.
    Сама підсказка формується за допомогою опрацювання параметру help та ключа, який визначили при створенні
    аргументу
  """
  def addScenario(self, *args, onlyCLI = False, methodParams = None, **kwargs):
    if onlyCLI == False:
      bannerText = "({0}){1}".format(self.getKeyFromArgs(args[1]), kwargs['help'])
      self.updateHelloBanner(bannerText)
    CLI.addScenario(self, *args, methodParams=methodParams, **kwargs)
  
  """ 
    Основний цикл програми. На основі вибраного режиму виконується відповідна логіка
  """
  def start(self):
    if self.mode == 'INTER':
      self.args.pop('inter')
      while True:
        try:
          self.userInput = str.lower(input(self.helloBanner + '\n'))
          self.execScenario()
        except KeyboardInterrupt:
          print('Процес завершений перериванням через клавіатуру (CTRL + C)')
          quit()
    elif self.argsCount == 0:
      self.parser.print_help()
    else:
      self.execScenario()
    
  def printBanner(self, text):
    self.banner = text
    print(self.banner)
  
  def updateHelloBanner(self, text):
    self.helloBanner += '\n' + text

  """ 
    Створення умови завершення інтерактивної програми
    trigger - символи, які користувач вводить для завершення програми
  """
  def setByeMessage(self, trigger = 'bye', text = 'Good Bye', banner = 'Завершити'):
    banner = "({0}) {1}".format(trigger, banner)
    self.byeTrigger = trigger
    self.byeText= text
    self.updateHelloBanner(banner)

  def bye(self):
    self.printBanner(self.byeText)
    quit()