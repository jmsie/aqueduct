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
        "system_id": settings['system_id'],
        'api_key': settings['api_key'],
        "targets": {},
      }
      for target_name, target_settings in settings['targets'].items():
        target_settings['signal_files'] = get_files_in_path(target_settings['path'])
        fund['targets'][target_name] = target_settings
        target_settings['position'] = 0
      self.funds.append(fund)

      print("Init fund: " + fund_name)
      print("\tTrading target: " + target_name)
      print("\tSignal_files:")
      for signal_file in target_settings['signal_files']:
        print("\t\t"+signal_file)

  def append_api(self, api):
    self.APIs.append(api)

  def start(self):
    print("Start tracking...")
    while(1):
      self.track_files()

  def track_files(self):
    for fund in self.funds:
      targets = fund['targets']
      try:
        total_position = 0
        system_id = fund['system_id']
        api_key = fund['api_key']
        update = False

        for symbol, target in fund['targets'].items():
          for signal_file in target['signal_files']:
            with open(signal_file) as fd:
              # Only one line in the signal output file
              line = fd.readline()
              position = int(line.split(',')[1])
              total_position += position
          if target['position'] != total_position:
            target['position'] = total_position
            update = True

        if update:
          for api in self.APIs:
            api.reset()
            for symbol, target in fund['targets'].items():
              api.set_positions(symbol, target['symbol_type'], target['position'])
            api.commit_positions(system_id, api_key)
      except:
        print("Error while handling fund: {}, revert the targets status".format(fund['name']))
        fund['targets'] = targets

if __name__ == "__main__":
  from config import *
  from api.C2 import C2
  c2 = C2(c2_config)
  monitor = Monitor()
  monitor.append_api(c2)
  monitor.set_fund_settings(fund_settings)
  #monitor.start()