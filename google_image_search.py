
import requests
import json

CUSTOM_SEARCH_API_KEY = 'AIzaSyDwSiEXy7D2aWm_qwCHEduZltM6dNTJRLQ'
CUSTOM_SEARCH_CX = '017152473705186054595:lqw2ydttohs'

def search_images_urls(search_query, count=10):
    if type(count) != int:
        raise TypeError("Argument count must be of type int")
    if count < 1:
        raise ValueError("Argument count must be greater than zero")

    def get_search_url(start_index=1):
        key = CUSTOM_SEARCH_API_KEY
        cx = CUSTOM_SEARCH_CX
        return "https://www.googleapis.com/customsearch/v1?q=" + \
            search_query + "&start=" + str(start_index) + "&key=" + key + "&cx=" + cx + \
            "&searchType=image"

    def get_10_results(start_index=1):
        search_url = get_search_url(start_index)
        r = requests.get(search_url)
        response = r.content.decode('utf-8')
        result = json.loads(response)

        print(json.dumps(result,sort_keys=True, indent=4))

        if "items" in result:
            return list(map(lambda item: item["link"], result["items"]))
        else:
            return []

    result = []
    start_index = 1
    while count >= 10:
        ten_results = get_10_results(start_index)
        if ten_results:
            result += ten_results
        else:
            return result
        count -= 10
        start_index += 10
    
    if count > 0:
        ten_results = get_10_results(start_index)
        if ten_results:
            result += ten_results[:count] if len(ten_results) > count else ten_results
        else:
            return result

    return result
