from os import walk
from os.path import join


class Monitor():
  def __init__(self):
    self.fund_settings = None
    self.funds = []

  def set_fund_settings(self, fund_settings):
    self.fund_settings = fund_settings

  def parse_fund_settings(self):
    def get_files_in_path(path):
      paths = []
      for root, dirs, files in walk(path):
        for file in files:
          full_path = join(root, file)
          paths.append(full_path)
      return paths

    for fund_name, settings in self.fund_settings.items():
      fund = {
        "name": fund_name,
        "paths": get_files_in_path(settings['path'])
      }
      self.funds.append(fund)



  def start(self):
    while(1):
      self.track_files()

  def track_files(self):
    for fund in self.funds:
      total_position = 0
      for path in fund['paths']:
        with open(path) as fd:
          # Only one line in the signal output file
          line = fd.readline()
          position = int(line.split(',')[1])
          total_position += position

if __name__ == "__main__":
  from config import *
  monitor = Monitor()
  monitor.set_fund_settings(fund_settings)
  monitor.parse_fund_settings()
  monitor.start()
