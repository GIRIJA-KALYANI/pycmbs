# -*- coding: utf-8 -*-

import unittest
import tempfile
from pycmbs.benchmarking.models import CMIP5Data, CMIP5RAWData, CMIP3Data

class TestBenchmarkingPlots(unittest.TestCase):

    def run_model_validation(self, model):
        r = model._get_unique_name()
        self.assertEqual(r, 'MPI-ESM-historical')

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_cmip5_data(self):
        data_dir = tempfile.mkdtemp()
        varmethods = {'albedo' : 'get_albedo()'}
        M = CMIP5Data(data_dir, 'MPI-ES M', 'hist orical', varmethods, intervals='monthly')
        self.run_model_validation(M)

    def test_cmip3_data(self):
        data_dir = tempfile.mkdtemp()
        varmethods = {'albedo' : 'get_albedo()'}
        M = CMIP3Data(data_dir, 'MPI-ES M', 'hist orical', varmethods, intervals='monthly')
        self.run_model_validation(M)

    def test_cmip5raw_data(self):
        data_dir = tempfile.mkdtemp()
        varmethods = {'albedo' : 'get_albedo()'}
        M = CMIP5RAWData(data_dir, 'MPI-ES M', 'hist orical', varmethods, intervals='monthly')
        self.run_model_validation(M)





if __name__ == "__main__":
    unittest.main()

