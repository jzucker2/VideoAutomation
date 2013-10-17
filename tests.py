import unittest
import video

class TestVideoClass(unittest.TestCase):
	def setUp(self):
		self.video = Video('/Users/jzucker/sample.mkv')

	def test_get_format(self):
		format = self.video.get_format()
		self.assertEqual()

if __name__ == '__main__':
	unittest.main()