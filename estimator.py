import operator
from collections import Counter


def estimator(data):
    res = {}
    for endpoint_id in data.keys():
        if data[endpoint_id]["caches"] != {}:
            most_viewed_video_id = max(data[endpoint_id]["requests"].iteritems(), key=operator.itemgetter(1))[0]
            best_cache = min(data[endpoint_id]["caches"].iteritems(), key=operator.itemgetter(1))[0]
            temp_lst = res.get(best_cache,[])
            if most_viewed_video_id not in temp_lst:
                temp_lst.append(most_viewed_video_id)
            res[best_cache]=temp_lst
    return res


def estimator_2(endpoints, videos, cache_size, nb_caches):
    res = {i: [] for i in range(nb_caches)}
    caches = {i: 0 for i in range(nb_caches)}
    for endpoint_id, endpoint_conf in endpoints.iteritems():
        if endpoint_conf["caches"]:
            most_viewed_videos = Counter(endpoint_conf["requests"]).most_common()
            best_caches = reversed(Counter(endpoint_conf["caches"]).most_common())
            for most_viewed_video_id, _ in most_viewed_videos:
                for best_cache, _ in best_caches:
                    if videos[most_viewed_video_id] + caches[best_cache] <= cache_size:
                        res[best_cache].append(most_viewed_video_id)
                        caches[best_cache] += videos[most_viewed_video_id]
    res = {key: list(set(val)) for key, val in res.iteritems()}
    print  float(sum(caches.values())) / (nb_caches * cache_size)
    return res


def estimator_3(endpoints, videos, cache_size, nb_caches):
    res = {i: [] for i in range(nb_caches)}
    caches = {i: 0 for i in range(nb_caches)}
    endpoints_lst = sorted(endpoints.items(), key=lambda (endpoint, endpoint_conf): sum(endpoint_conf["requests"].values()), reverse=True)
    for endpoint_id, endpoint_conf in endpoints_lst:
        if endpoint_conf["caches"]:
            most_viewed_videos = Counter(endpoint_conf["requests"]).most_common()
            best_caches = reversed(Counter(endpoint_conf["caches"]).most_common())
            for most_viewed_video_id, _ in most_viewed_videos:
                for best_cache, _ in best_caches:
                    if videos[most_viewed_video_id] + caches[best_cache] <= cache_size:
                        res[best_cache].append(most_viewed_video_id)
                        caches[best_cache] += videos[most_viewed_video_id]
    res = {key: list(set(val)) for key, val in res.iteritems()}
    print  float(sum(caches.values())) / (nb_caches * cache_size)
    return res


def estimator_4(endpoints, videos, cache_size, nb_caches):
    res = {i: [] for i in range(nb_caches)}
    caches = {i: 0 for i in range(nb_caches)}
    endpoints_lst = sorted(endpoints.items(), key=lambda (endpoint, endpoint_conf): sum(endpoint_conf["caches"].values()) * sum(endpoint_conf["requests"].values()))
    for endpoint_id, endpoint_conf in endpoints_lst:
        if endpoint_conf["caches"]:
            most_viewed_videos = Counter(endpoint_conf["requests"]).most_common()
            best_caches = reversed(Counter(endpoint_conf["caches"]).most_common())
            for most_viewed_video_id, _ in most_viewed_videos:
                for best_cache, _ in best_caches:
                    if videos[most_viewed_video_id] + caches[best_cache] <= cache_size:
                        res[best_cache].append(most_viewed_video_id)
                        caches[best_cache] += videos[most_viewed_video_id]
    res = {key: list(set(val)) for key, val in res.iteritems()}
    print  float(sum(caches.values())) / (nb_caches * cache_size)
    return res


def estimator_5(endpoints, videos, cache_size, nb_caches):
