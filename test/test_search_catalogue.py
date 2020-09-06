import unittest

from src.catalogue import Catalogue
from src.compact_disc import CompactDisc


class SearchCatalogue(unittest.TestCase):
    def test_matching_cd_is_found(self):
        cd = CompactDisc("Peter Gabriel", "So")
        catalogue = Catalogue([cd])
        self.assertEqual(cd, catalogue.search("Peter Gabriel", "So"))


if __name__ == '__main__':
    unittest.main()
