from main import logger

nested_list = [
	['a', 'b', 'c'],
	['d', 'e', 'f', 'h', False],
	[1, 2, None],
]

@logger(name_file='log_generator.txt')
def flatten_generator(arr):

    for i in arr:
        if isinstance(i, list):
            yield from flatten_generator(i)
        else:
            yield i


if __name__ == '__main__':
    for item in flatten_generator(nested_list):
        print(item)
    flat_list = [item for item in flatten_generator(nested_list)]
    print(flat_list)
