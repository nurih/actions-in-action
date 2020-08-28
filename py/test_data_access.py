import unittest
from py.data_access import DataAccess


class TestDataAccess(unittest.TestCase):

    def test_constructor_default_uri(self):
        actual = DataAccess().MONGO_URI
        self.assertEqual(actual, 'mongodb://localhost:27017')

    def test_constructor_supplied_uri(self):
        actual = DataAccess('mongodb://example.com/?replSet=rs0').MONGO_URI
        self.assertEqual(actual, 'mongodb://example.com/?replSet=rs0')

    def test_ensure_dict_ok_on_dict(self):
        try:
            DataAccess.ensure_dict({'a': 1})
        except:
            self.fail('Should not raise exception')

    def test_ensure_dict_raises(self):
        for doc in None, {}, 1, [], (), "yo":
            with self.subTest(doc=doc):
                with self.assertRaises(ValueError):
                    DataAccess.ensure_dict(doc)


if __name__ == '__main__':
    unittest.main()
