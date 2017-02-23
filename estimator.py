import operator

def estimator(data):
    res = {}
    for endpoint_id in data.keys():
        if data[endpoint_id]["caches"] != {}:
            most_viewed_video_id = max(data[endpoint_id]["requests"].iteritems(), key=operator.itemgetter(1))[0]
            best_cache = min(data[endpoint_id]["caches"].iteritems(), key=operator.itemgetter(1))[0]
            temp_lst = res.get(best_cache,[])
            temp_lst.append(most_viewed_video_id)
            res[best_cache]=temp_lst
    return res