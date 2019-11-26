import sys
sys.path.append('..')

from api.API import API

class C2(API):
  def __init__(self, context):
    super().__init__(context)



if __name__ == "__main__":
  api_config = {
    'name': "C2",
    "base_url": "https://collective2.com/world/apiv3/",
    "api_key": "1kuBwZmJpHHHgJAHFSYGYFSYGHf1nvOV4hSGPWVwy8HuAshe",
  }
  c2 = C2(api_config)
