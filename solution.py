import re

def range_validator(string):

    #creates an object w/ starting and ending points.
    class Interval:
        def __init__(self, start, end=None):
            self.start = start
            self.end = end or start

    #parses string to separate into interval objects
    def parse_input(input_string):
        regex = '\d+(?:\s*-\s*\d+)?(?:,\d+(?:-\d+)?)*'
        input_list = re.findall(regex, input_string)
        object_list = []
        for x in input_list:
            try:
                object_list.append(Interval(int(x)).__dict__)
            except:
                split_x = re.split(r'\D+', x)
                if split_x[0] <= split_x[1]:
                    object_list.append(Interval(int(split_x[0]), int(split_x[1])).__dict__)
        return object_list


    #reduces interval objects to remove overlap & redundancy
    def interval_synth(args):
        sorted_objects = sorted(args, key = lambda x: x['start'])
        i = 0
        while i < len(sorted_objects) - 1:
            if sorted_objects[i]['end'] >= sorted_objects[i + 1]['start']:
                if sorted_objects[i + 1]['end'] <= sorted_objects[i]['end']:
                    del sorted_objects[i + 1]
                else:
                    sorted_objects[i]['end'] = sorted_objects[i + 1]['end']
                    del sorted_objects[i + 1]
            else:
                i += 1
        return sorted_objects

    object_list = parse_input(string)
    return interval_synth(object_list)


print(range_validator('65-11, 1, 5, 3, 4-8, 7-10'))
