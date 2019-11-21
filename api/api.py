class API():
  def __init__(self):
    self.name = ""
    self.base_url = ""
    self.api_key = ""
    self.api_config = None

  def set_api_config(self, api_config):
    self.api_config = api_config
    try:
      self.name = api_config['name']
      self.base_url = api_config['base_url']
      self.api_key = api_config['api_key']
    except:
      print("Error in setting up API: " + self.name)

if __name__ == "__main__":
  api_config = {
    'name': "C2",
    "base_url": "https://collective2.com/world/apiv3/",
    "api_key": "1kuBwZmJpHHHgJAHFSYGYFSYGHf1nvOV4hSGPWVwy8HuAshe",
  }
  api = API()
  api.set_api_config(api_config)

