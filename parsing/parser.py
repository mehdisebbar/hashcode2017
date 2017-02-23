

INPUT_FILEPATH = "/home/xavierm/Documents/hashcode_files/me_at_the_zoo.in"

def get_lines(input_filepath):
    with open(input_filepath) as infile:
        lines = infile.read().splitlines()
    return lines


def read_data(lines):
    nb_video, nb_endpoints, nb_requests, nb_caches, cache_capacity = [int(el) for el in lines[0].split()]
    videos = {i: int(size) for i, size in enumerate(lines[1].split())}
    endpoints = {}
    current_endpoint_id = 0
    current_endpoint_data_center_latency = lines[2].split()[0]
    current_endpoint_cache_nb = lines[2].split()[1]
    for line in lines[2:]:




    # return videos



    # return nb_video, nb_endpoints, nb_requests, nb_caches, cache_capacity



a = get_lines(INPUT_FILEPATH)
b = read_data(a)
print b