import re
import unittest
import string

def range_validator(entry_string):

    #creates an object w/ starting and ending points.
    class Interval:
        def __init__(self, start, end=None):
            self.start = start
            self.end = end or start

    #parses string to separate into interval objects
    def parse_input(input_string):

        #check for invalid characters
        if re.match('^[\d\-,\s]*$', input_string) == None:
            raise ValueError('You have entered invalid characters')
        regex = '\d+(?:\s*-\s*\d+)?(?:,\d+(?:-\d+)?)*'
        input_list = re.findall(regex, input_string)
        object_list = []

        #check for errors in invidual range selections and create objects
        for x in input_list:            
            try:
                if int(x) <= 0:
                    raise ValueError('Pen number must be greater than or equal to 1')
                object_list.append(Interval(int(x)))
            except:
                split_x = re.split(r'\D+', x)
                if len(split_x) > 2:
                    raise ValueError('A range you have entered is invalid')
                start = int(split_x[0])
                end = int(split_x[1])
                if start <= 0:
                    raise ValueError('Pen number must be greater than or equal to 1')
                if start <= end:
                    object_list.append(Interval(start, end))
                else:
                    raise ValueError('A range you have entered is invalid')
        
        return object_list

    #reduces interval objects to remove overlap & redundancy
    def interval_synth(args):
        sorted_objects = sorted(args, key = lambda x: x.start)
        i = 0
        while i < len(sorted_objects) - 1:
            if sorted_objects[i].end >= sorted_objects[i + 1].start:
                if sorted_objects[i + 1].end <= sorted_objects[i].end:
                    del sorted_objects[i + 1]
                else:
                    sorted_objects[i].end = sorted_objects[i + 1].end
                    del sorted_objects[i + 1]
            else:
                i += 1
        return sorted_objects

    object_list = parse_input(entry_string)
    return interval_synth(object_list)


class TestCases(unittest.TestCase):
    def test_single(self):
        self.assertEqual(range_validator('6')[0].__dict__, {'start': 6, 'end': 6})

    def test_double(self):
        self.assertEqual(range_validator('1, 5')[0].__dict__, {'start': 1, 'end': 1})
        self.assertEqual(range_validator('1, 5')[1].__dict__, {'start': 5, 'end': 5})

    def test_single_order(self):
        self.assertEqual(range_validator('5, 1')[0].__dict__, {'start': 1, 'end': 1})
        self.assertEqual(range_validator('5, 1')[1].__dict__, {'start': 5, 'end': 5})

    def test_range(self):
        self.assertEqual(range_validator('4-8')[0].__dict__, {'start': 4, 'end': 8})

    def test_single_and_range(self):
        self.assertEqual(range_validator('2, 4-8')[0].__dict__, {'start': 2, 'end': 2})
        self.assertEqual(range_validator('2, 4-8')[1].__dict__, {'start': 4, 'end': 8})

    def test_same_start(self):
        self.assertEqual(range_validator('4, 4-8')[0].__dict__, {'start': 4, 'end': 8})

    def test_surrounded_single(self):
        self.assertEqual(range_validator('5, 4-8')[0].__dict__, {'start': 4, 'end': 8})

    def test_same_end(self):
        self.assertEqual(range_validator('8, 4-8')[0].__dict__, {'start': 4, 'end': 8})

    def test_overlapping_ranges(self):
        self.assertEqual(range_validator('4-8, 7-10')[0].__dict__, {'start': 4, 'end': 10})

    def test_surrounded_range(self):
        self.assertEqual(range_validator('4-8, 2-20')[0].__dict__, {'start': 2, 'end': 20})

    def test_range_order(self):
        self.assertEqual(range_validator('7-10, 2-5')[0].__dict__, {'start': 2, 'end': 5})
        self.assertEqual(range_validator('7-10, 2-5')[1].__dict__, {'start': 7, 'end': 10})

    def test_unpaired(self):
        self.assertEqual(range_validator('7-')[0].__dict__, {'start': 7, 'end': 7})
        self.assertEqual(range_validator('-7')[0].__dict__, {'start': 7, 'end': 7})

if __name__ == '__main__':
    unittest.main()
