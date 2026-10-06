from src import main

def test_request():
  assert main.request() == 200