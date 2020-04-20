import unittest

class build_test(unittest.TestCase):
  "Example Tests for CircleCI"

  def test_that_should_pass(self):
    self.assertEqual(1, 1, msg="1 should equal 1")

  def test_that_should_fail(self):
    self.assertEqual(1, 2, msg="1 should not equal 2")

unittest.main()