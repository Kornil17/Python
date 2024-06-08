from unittest import TestCase, main
from main import func


class Test(TestCase):
    def test_postitve(self):
        self.assertEquals(func(3, 5, "+"), 8)
        self.assertEquals(func(3, 5, "-"), -2)
        self.assertEquals(func(3, 5, "*"), 15)
        self.assertEquals(func(3, 5, "/"), 0.6)
        self.assertEquals(func(3, 5, "%"), 3)

    def test_negative(self):
        with self.assertRaises(SyntaxError) as e:
            func(2, 3, "asdjkhsadjk")
        self.assertEquals("invalid syntax", e.exception.args[0])





if __name__ == "__main__":
    main()
