
# result_dict example
# result_dict = {0:[1,2],1:[2,3]}


def write_output(result_dict):
    nb_cache_server = len(result_dict.keys())
    with open('output', 'w+') as infile:
        infile.write(str(nb_cache_server) + '\n')
        for key, values in result_dict.iteritems():
            values_to_string = [str(value) for value in values]
            infile.write(str(key) + ' ' + ' '.join(values_to_string) + '\n')
