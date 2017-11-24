import unittest
import testpb


class TestStringMethods(unittest.TestCase):
    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # Проверим, что s.split не работает, если разделитель - не строка
        with self.assertRaises(TypeError):
            s.split(2)

    def test_add(self):
        testpb.message = ["добавить", "12345", "qwerty", "asd123"]
        testpb.add(testpb.message)

    def test_search(self):
        testpb.message = ["найти", "12345"]

    def test_delete(self):
        testpb.message = ["удалить", "12345"]		

    def test_close(self):
        testpb.close_db()
		

if __name__ == '__main__':
    unittest.main()
