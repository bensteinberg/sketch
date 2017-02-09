import os
import sketch
import unittest
import tempfile

class SketchTestCase(unittest.TestCase):

    def setUp(self):
        # self.db_fd, sketch.app.config['DATABASE'] = tempfile.mkstemp()
        sketch.app.config['TESTING'] = True
        self.app = sketch.app.test_client()
        # with flaskr.app.app_context():
        #     flaskr.init_db()

    def tearDown(self):
        pass
        # os.close(self.db_fd)
        # os.unlink(flaskr.app.config['DATABASE'])

    def test_index(self):
        rv = self.app.get('/')
        assert b'Hello, world!' in rv.data

if __name__ == '__main__':
    unittest.main()

