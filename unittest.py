import unittest

class learn_test(unittest.TestCase):

    def test_fn1(self):
        pass

    def test_fn2(self):
        pass

class Another_learn_test(unittest.TestCase):

    def my_test1(self):
        pass

def sum(a,b):
    return a+b


class sumtest(unittest.TestCase):
    def setUp(self):
        print("setting up test data...")
        #Arrange
        self.a = 22
        self.b = 33

    def tearDown(self):
        print("Tear down called")



    def test_sum(self):
        print("test 1 is called")

        # #Arrange
        # a = 6
        # b = 9

        #Act
        result = sum(self.a, self.b)

        #Assert
        self.assertEqual(result, self.a + self.b)

    def test_sum2(self):
        print("test 2 is called")
        # #Arrange
        # a = 10
        # b = 20

        #Act
        result = sum(self.b, self.a)

        #Assert
        self.assertEqual(result, self.a + self.b)


if __name__ == "__main__":
    unittest.main()