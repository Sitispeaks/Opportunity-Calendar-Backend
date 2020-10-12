from django.conf import settings

DEFAULT_PAGINATION = settings.PAGINATION


def get_pagination_info(request, total_count):
    query_params = request.GET
    limit = int(query_params.get("limit", DEFAULT_PAGINATION["LIMIT"]))
    offset = int(query_params.get("offset", DEFAULT_PAGINATION["OFFSET"]))
    request_body = request.data if request.method != "GET" else {}

    next_offset = offset + limit
    previous_offset = offset - limit

    def build_paginated_url(offset, limit, parameters):
        url_path = request.path_info
        url_path += "?limit={}&offset={}".format(limit, offset)

        for query_key, query_value in parameters.items():
            if query_key not in ["limit", "offset"]:
                url_path += "&{}={}".format(query_key, query_value)

        return url_path

    pagination_info = {}

    if request_body:
        pagination_info["body"] = request_body
    if next_offset < total_count:
        pagination_info["nextURL"] = build_paginated_url(
            next_offset, limit, query_params
        )
    if previous_offset >= 0:
        pagination_info["previousURL"] = build_paginated_url(
            previous_offset, limit, query_params
        )

    return pagination_info
