import json
from datetime import datetime

class C2():
  def __init__(self, context):
    self.name = ""
    self.base_url = ""
    self.positions = []
    self.set_api_config(context)

  def set_api_config(self, context):
    try:
      self.name = context['name']
      self.base_url = context['base_url']
    except:
      print("Error in setting up API: " + self.name)

  def reset(self):
    self.positions = []

  def set_positions(self, symbol, symbol_type, position):
    self.positions.append({
      "symbol": symbol,
      "typeofsymbol": symbol_type,
      "quant": position,
    })

  def commit_positions(self, system_id, api_key):
    data = {
      "systemid": system_id,
      "apikey": api_key,
      "positions": self.positions,
    }
    payload = json.dumps(data)
    print("commit position: {}".format(datetime.now()))
    print(self.positions)



if __name__ == "__main__":
  api_config = {
    'name': "C2",
    "base_url": "https://collective2.com/world/apiv3/",
    "api_key": "1kuBwZmJpHHHgJAHFSYGYFSYGHf1nvOV4hSGPWVwy8HuAshe",
  }
  c2 = C2(api_config)
