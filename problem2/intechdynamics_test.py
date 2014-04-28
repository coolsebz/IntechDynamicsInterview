import unittest
from intechdynamics import IntechDynamics


class TestIntechDynamics(unittest.TestCase):

    def test_should_return_intech(self):
        self.assertEqual(IntechDynamics("I"), "INTECH")
        self.assertNotEqual(IntechDynamics("idee"), "INTECH")

    def test_should_return_dynamics(self):
        self.assertEqual(IntechDynamics("D"), "DYNAMICS")
        self.assertNotEqual(IntechDynamics("gold"), "DYNAMICS")

    def test_should_return_intech_dynamics(self):
        self.assertEqual(IntechDynamics("ID"), "INTECH DYNAMICS")
        self.assertNotEqual(IntechDynamics("iod"), "INTECH DYNAMICS")

if __name__ == '__main__':
    # automatically load all methods starting with "test_" as test methods
    suite = unittest.TestLoader().loadTestsFromTestCase(TestIntechDynamics)
    # run them with a certain verbosity
    unittest.TextTestRunner(verbosity=2).run(suite)
