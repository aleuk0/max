import unittest
import phonebook


class TestStringMethods(unittest.TestCase):
    # def test_upper(self):
    #    self.assertEqual('foo'.upper(), 'FOO')

    # def test_isupper(self):
    #    self.assertTrue('FOO'.isupper())
    #    self.assertFalse('Foo'.isupper())

    # def test_split(self):
    #    s = 'hello world'
    #    self.assertEqual(s.split(), ['hello', 'world'])
    #    # Проверим, что s.split не работает, если разделитель - не строка
    #    with self.assertRaises(TypeError):
    #        s.split(2)

    #def test_add(self):
    #    phonebook.message = ["добавить", "12345", "qwerty", "asd123"]
    #    phonebook.add(phonebook.message)

    def test_search(self):
        phonebook.message = ["найти", "12345"]
        phonebook.search(phonebook.message)

    # def test_delete(self):
    #    phonebook.message = ["удалить", "12345"]
    #    phonebook.delete(phonebook.message)

    def test_close(self):
        phonebook.close_db()


if __name__ == '__main__':
    unittest.main()
