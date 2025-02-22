import subprocess
from modules.system.Logger import Logger

class SystemManager:
  logger = Logger()
  
  def commandRun(self, command = []):
    try:
      result = subprocess.run(command, capture_output=True, text=True)
    except Exception as err:
      self.logger.write('ERROR: Виникла помилка при виконанні команди <%s>: %s' % (command, err))
      quit()
  
    return result.stdout

  def saveToFile(self, file, fileName):
    if file:
      open(fileName, 'w+').write(file)
      self.logger.write("Result save to file: %s" % fileName)
    else:
      self.logger.write("Don't save to file: %s" % fileName)
      quit()
