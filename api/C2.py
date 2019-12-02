from datetime import datetime
import requests

class C2():
  def __init__(self, context):
    self.name = ""
    self.base_url = ""
    self.commit_position_api = ""
    self.positions = []
    self.set_api_config(context)
    self.log = open("C2.log", "a")

  def set_api_config(self, context):
    try:
      self.name = context['name']
      self.base_url = context['base_url']
      self.commit_position_api = self.base_url + "setDesiredPositions"
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
    print("\ncommit position: {}".format(datetime.now()))
    self.log.write("commit position: {}\n".format(datetime.now()))
    print(self.positions)
    self.log.write(str(self.positions) + "\n")

    response = requests.post(url=self.commit_position_api, json=data)
    print(response.json())
    self.log.write(str(response.json()) + "\n")
    self.log.flush()

