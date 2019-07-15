import unittest
from mock import Mock, patch
from executors import BaseExecutor, HumanExecutor, InodeExecutor
from parsers import BaseParser, HumanParser, InodeParser
import test_data


class TestBaseParser(unittest.TestCase):
    """unittests for class BaseParser"""

    def setUp(self):
        """creation of two test strings - one with data, second with error"""
        self.testobj = BaseExecutor().result(test_data.TEST_RESULT_OUTPUT,
                                             test_data.ERROR_MESSAGE_OK,
                                             test_data.RETURN_CODE_OK)
        self.testobj_error = BaseExecutor().result(None, test_data.ERROR_MESSAGE_IF_ERROR,
                                                   test_data.RETURN_CODE_ERROR)

    def test_make_string_as_dict(self):
        """testing of the correct transformation of string to dict"""
        actual_result = BaseParser(
            test_data.SUB_DF_OUTPUT).make_dict_from_string()
        self.assertIsNotNone(actual_result)
        self.assertIsInstance(actual_result, dict)
        self.assertDictEqual(actual_result, test_data.EXPECTED_BaseExecutor_OK)

    def result(self):
        """testing of the correct output in json"""
        actual_result = self.testobj
        self.assertIsInstance(actual_result, str)
        self.assertIsNotNone(actual_result)
        self.assertIn('/boot', test_data.TEST_RESULT_EXPECTED)
        self.assertNotIn('None', test_data.TEST_RESULT_EXPECTED)
        self.assertEqual(actual_result, test_data.TEST_RESULT_EXPECTED)

    def result_when_error(self):
        """testing of the correct output in json with error returncode"""
        actual_result = self.testobj_error
        self.assertIsInstance(actual_result, str)
        self.assertIsNotNone(actual_result)
        self.assertIn('null', test_data.TEST_RESULT_EXP_ERROR)
        self.assertEqual(actual_result, test_data.TEST_RESULT_EXP_ERROR)


class TestHumanParser(unittest.TestCase):
    """unittests for class HumanParser"""

    def test_make_string_as_dict(self):
        """testing of the correct transformation of string to dict"""
        actual_result = HumanParser(test_data.SUB_DF_H_OUTPUT)\
            .make_dict_from_string()
        self.assertIsNotNone(actual_result)
        self.assertIsInstance(actual_result, dict)
        self.assertDictEqual(actual_result, test_data.EXPECTED_HUMAN_OK)


class TestInodeParser(unittest.TestCase):
    """unittests for class HumanParser"""

    def test_make_string_as_dict(self):
        """testing of the correct transformation of string to dict"""
        actual_result = InodeParser(
            test_data.SUB_DF_I_OUTPUT).make_dict_from_string()
        self.assertIsNotNone(actual_result)
        self.assertIsInstance(actual_result, dict)
        self.assertDictEqual(actual_result, test_data.EXPECTED_INODEPARSER)


class TestBaseExecutor(unittest.TestCase):
    """unittests for class BaseExecutor"""

    def test_command_maker(self):
        """testing of the correct convertation list of args from *args"""
        self.assertEqual(BaseExecutor().cmd, 'df')
        self.assertEqual(BaseExecutor('ls', 'arg1', 'arg2').args,
                         ('arg1', 'arg2'))
        self.assertIsInstance(BaseExecutor('df', '-i').command_maker(), list)
        self.assertEqual(BaseExecutor('df', 'h', 'r', 'q').command_maker(),
                         ['df', 'h', 'r', 'q'],
                         'Error in command_maker() method')


class TestHumanExecutor(unittest.TestCase):
    """unittests for class HumanExecutor"""

    def test_command_maker(self):
        """testing of the correct convertation to list of args from *args"""
        self.assertEqual(HumanExecutor().cmd, 'df',
                         'Error in HumanBuilder cmd')
        self.assertEqual(HumanExecutor().args, ('-h',),
                         'Error in HumanBuilder arg')
        self.assertEqual(HumanExecutor().command_maker(), ['df', '-h'],
                         'Error in command_maker() method')


if __name__ == '__main__':
    unittest.main(exit=False)
