import unittest
import count


class TestCount(unittest.TestCase):
    def test_no_flags(self):
        vals = ["test.txt"]
        test = {"b": 2, "a": 1, "o": 2, "n": 1}
        res = count.flags(vals)
        self.assertDictEqual(test, res)

    def test_c_flag(self):
        vals = ["-c", "test.txt"]
        test = {"B": 1, "a": 1, "b":1, "o":2, "n": 1}
        res = count.flags(vals)
        self.assertDictEqual(test, res)

    def test_z_flag(self):
        vals = ["-z", "test.txt"]
        test = {"b": 2, "a": 1, "o": 2, "n": 1, "c": 0, "d": 0, "e": 0, "f": 0, "g": 0, "h": 0, "i": 0, "j": 0, "k": 0, "l": 0, "m": 0, "p": 0, "q": 0, "r": 0, "s": 0, "t": 0, "u": 0, "v": 0, "w": 0, "x": 0, "y": 0, "z": 0}
        res = count.flags(vals)
        self.assertDictEqual(test, res)

    def test_l_flag(self):
        vals = ["-l", "bo", "test.txt"]
        test = {"b": 2, "o": 2}
        res = count.flags(vals)
        self.assertDictEqual(test, res)

    def test_c_z_flags(self):
        vals = ["-c", "-z", "test.txt"]
        test = {"B": 1, "a": 1, "b":1, "o": 2, "n": 1, "c": 0, "d": 0, "e": 0, "f": 0, "g": 0, "h": 0, "i": 0, "j": 0, "k": 0, "l": 0, "m": 0, "p": 0, "q": 0, "r": 0, "s": 0, "t": 0, "u": 0, "v": 0, "w": 0, "x": 0, "y": 0, "z": 0}
        res = count.flags(vals)
        self.assertDictEqual(test, res)

    def test_c_l_flags(self):
        vals = ["-c", "-l", "bo", "test.txt"]
        test = {"B": 1, "b": 1, "o": 2}
        res = count.flags(vals)
        self.assertDictEqual(test, res)

    def test_l_z_flags(self):
        vals = ["-z", "-l", "bo", "test.txt"]
        test = {"b": 2, "o": 2}
        res = count.flags(vals)
        self.assertDictEqual(test, res)

    def test_all_flags(self):
        vals = ["-c", "-z", "-l", "bo", "test.txt"]
        test = {"B": 1, "b": 1, "o": 2}
        res = count.flags(vals)
        self.assertDictEqual(test, res)

if __name__ == "__main__":
    unittest.main()
