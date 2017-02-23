INPUT_FILEPATH = "/home/xavierm/Documents/hashcode_files/stupid_af.in"


def get_lines(input_filepath):
    with open(input_filepath) as infile:
        lines = infile.read().splitlines()
    return lines


def read_data(lines):
    nb_video, nb_endpoints, nb_requests, nb_caches, cache_capacity = [int(el) for el in lines[0].split()]
    videos = {i: int(size) for i, size in enumerate(lines[1].split())}
    endpoints = {i: {"caches": {}, "requests": {}} for i in range(nb_endpoints)}
    current_endpoint_id = 0
    current_endpoint_data_center_latency = lines[2].split()[0]
    current_endpoint_cache_nb = int(lines[2].split()[1])
    current_line = 3
    current_endpoint_cache_index = 0
    endpoints[0]["data_center_latency"] = current_endpoint_data_center_latency
    while len(lines[current_line].split()) == 2:
        if current_endpoint_cache_index >= current_endpoint_cache_nb:
            current_endpoint_id += 1
            endpoints[current_endpoint_id]["data_center_latency"] = int(lines[current_line].split()[0])
            current_endpoint_cache_nb = int(lines[current_line].split()[1])
            current_endpoint_cache_index = 0
            current_line += 1
        else:
            cache_id, latency = [int(el) for el in lines[current_line].split()]
            endpoints[current_endpoint_id]["caches"][cache_id] = latency
            current_line += 1
            current_endpoint_cache_index += 1
    while current_line < len(lines):
        video_id, endpoint_id, requests_nb = [int(el) for el in lines[current_line].split()]
        endpoints[endpoint_id]["requests"][video_id] = requests_nb
        current_line += 1

    return endpoints, videos


lines = get_lines(INPUT_FILEPATH)
endpoints, videos = read_data(lines)
