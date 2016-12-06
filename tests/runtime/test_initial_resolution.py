import unittest

from pyjvm.bytecode_readers import BytecodeFileReader
from pyjvm.class_parser import ClassParser
from pyjvm.runtime_classes import RuntimeClass
from pyjvm.runtime.initial_resolution import prepare_class


class TestInitialResolution(unittest.TestCase):
    def setUp(self):
        parser = ClassParser()
        bytecode = parser.parse(
            BytecodeFileReader('tests/res/SampleClass.class'))
        self.runtime_class = RuntimeClass(bytecode)

    def test_prepare_class(self):
        prepare_class(self.runtime_class)
        self.assertEqual(0, self.runtime_class.get_field('serialVersionUID'))
        self.assertEqual(0, self.runtime_class.get_field('value1'))
        self.assertEqual(0.0, self.runtime_class.get_field('value2'))


if __name__ == '__main__':
    unittest.main()
