from argparse import ArgumentParser

class CommandArgs():
  def __init__(self, descr='Default description'):
    self.descr = descr
    self.parser = ArgumentParser(description=descr)

  # params = {'params':() - задати назви прапорців, 'subParams':{} - задати додаткові параметри}
  def setCommand(self, params = {}):
    if params:
      self.parser.add_argument(*params['params'], **params['subParams'])

  # Отримати параметри скрипта, що подаються у вигляді словника isDict (default) або ні
  def initCommandArgs(self, isDict = True):
    if isDict:
      self.args = vars(self.parser.parse_args()) 
    else:
      self.args = self.parser.parse_args()
    return self.args
    
  """
    Отримати значення параметру за відповідним прапорцем. Якщо команда може отримувати
    декілька значень через кому, тому повернути їх можна словником (toList) 
  """
  def getValue(self, key, toList = True):
    if key in self.args.keys() and self.args[key] != None:
      if toList:
        return self.args[key].split(',')

      return self.args[key]
    else:
      return None
