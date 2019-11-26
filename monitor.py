from os import walk
from os.path import join



class Monitor():
  def __init__(self):
    self.fund_settings = None
    self.funds = []
    self.APIs = []

  def set_fund_settings(self, fund_settings):
    self.fund_settings = fund_settings
    self.parse_fund_settings()

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

  def append_api(self, api):
    self.APIs.append(api)


  def start(self):
    while(1):
      self.track_files()

  def track_files(self):
    for fund in self.funds:
      total_position = 0
      fund_name = fund['name']
      fund_paths = fund['paths']
      for path in fund_paths:
        with open(path) as fd:
          # Only one line in the signal output file
          line = fd.readline()
          position = int(line.split(',')[1])
          total_position += position
      for api in self.APIs:
        system_id = self.fund_settings[fund_name]['system_id']
        symbol = self.fund_settings[fund_name]['symbol']
        api.set_positions(system_id, symbol, total_position)

if __name__ == "__main__":
  from config import *
  from api import C2
  c2 = C2.C2(c2_config)
  monitor = Monitor()
  monitor.append_api(c2)
  monitor.set_fund_settings(fund_settings)
  monitor.start()
