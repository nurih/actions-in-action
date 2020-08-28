import unittest
from py.data_access import DataAccess


class TestDataAccessIntegration(unittest.TestCase):

    def test_insert(self):
        db = DataAccess()
        try:
            db.insert({'marklar': True})
        except:
            self.fail('Should not raise exception')

    def test_find(self):
        # arrange
        TEST_VALUE = 123456
        db = DataAccess()
        db.insert({'test_find': TEST_VALUE})

        # act
        actual = db.find({'test_find': TEST_VALUE})[0]

        # assert
        self.assertEqual(actual['test_find'], TEST_VALUE)


if __name__ == '__main__':
    unittest.main()
