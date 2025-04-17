import psutil
from app.CLI import CLI

class System:
  def __init__(self):
    self.system = psutil
    self.formattedJson = {}

  def updateAndPrintResult(self, result, key, message = ''):
    if CLI.toJson:
      self.formattedJson[key] = result
      CLI.updateFormattedJson({key: self.formattedJson[key]})
      CLI.print()
    else:
      CLI.print(message)