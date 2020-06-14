import unittest

import Creature

class TestCreature(unittest.TestCase):

   def test_voice_not_empty(self):
       # Assume
       kind = "Test"
       name = "Creature"

       creature = Creature(kind, name)

       # Action
       result = creature.speak()

       # Assert
       self.assertEqual(result, "Hrmmmph")


if __name__ == '__main__':
    unittest.main()
