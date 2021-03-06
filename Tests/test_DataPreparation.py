from unittest import TestCase, mock
import sys, os
sys.path.append(os.getcwd().split('\Tests')[0])

from Domain.DataPreparation import DataPreparation
from Tests.StubDBAccess import StubDBAccess


class TestDataPreparation(TestCase):
    def setUp(self):
        self.dir_path = 'TestData/directories'
        self.dataPreparation = DataPreparation(self.dir_path, 'dataset.txt', 20, 360)
        self.dataPreparation.db = StubDBAccess()
        self.dataPreparation.DS_FOLDER = self.dir_path

    def test_get_csv_with_prepared_data(self):
        dataset_path = self.dataPreparation.get_csv_with_prepared_data({}, 'weather', ['summer', 'winter', 'spring'])
        with open(dataset_path, 'r') as file:
            prepared_data = file.readlines()
            self.assertEqual(prepared_data, ['3,360,summer,winter,spring\n',
                                             '-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,spring\n',
                                             '-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,summer\n',
                                             '-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,-1.75,7.45,29.5,winter\n'])
        self.dataPreparation.clear_data_folder()

    def test_isfloat(self):
        self.assertFalse(self.dataPreparation.isfloat("string"))
        self.assertTrue(self.dataPreparation.isfloat(0))
        self.assertTrue(self.dataPreparation.isfloat(2.4))

    def test_feature_padding(self):
        padding_size = 10
        too_small_list = []
        list = [1, 2, 3, 4, 5]
        with self.assertRaises(Exception) as context:
            self.dataPreparation.feature_padding(too_small_list, padding_size)
        self.assertEqual('feature_padding: features length is too small', context.exception.__str__())
        self.assertEqual(self.dataPreparation.feature_padding(list, padding_size),
                         [1, 2, 3, 4, 5, 3, 4, 5, 3, 4, 5, 3, 4, 5, 3])

    def test_fix_features_size(self):
        size = 10
        big_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
        small_list = [1, 2, 3, 4, 5]
        self.assertEqual(self.dataPreparation.fix_features_size(big_list, size),
                         [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        self.assertEqual(self.dataPreparation.fix_features_size(small_list, size),
                         [1, 2, 3, 4, 5, 3, 4, 5, 3, 4])



