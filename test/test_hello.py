import unittest
from hello import hello

class HelloTest(unittest.TestCase):
  def test(self):
    self.assertEquals(hello(),'Hello, world.')
