import sys
import json

sys.path.append('..')
from api.API import API

class C2(API):
  def __init__(self, context):
    super().__init__(context)
    self.positions = []

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
    print(payload)


if __name__ == "__main__":
  api_config = {
    'name': "C2",
    "base_url": "https://collective2.com/world/apiv3/",
    "api_key": "1kuBwZmJpHHHgJAHFSYGYFSYGHf1nvOV4hSGPWVwy8HuAshe",
  }
  c2 = C2(api_config)
