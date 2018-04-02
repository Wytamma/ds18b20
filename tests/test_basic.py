# -*- coding: utf-8 -*-

from .context import ds18b20

import unittest


class BasicTestSuite(unittest.TestCase):
    """Basic test cases."""

    def all_probes_returns_list(self):
        self.assertIsInstance(ds18b20.all_probes(), list)
        
    def all_probes_returns_list_of_Probes(self):
        for p in ds18b20.all_probes():
            self.assertIsInstance(p, ds18b20.Probe)

if __name__ == '__main__':
    unittest.main()