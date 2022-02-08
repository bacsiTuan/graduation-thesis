# coding: utf8
def paginate_format(pagination):
    pagination.__dict__['pages'] = int(pagination.total / pagination.per_page) + (
        1 if pagination.total % pagination.per_page > 0 else 0)
    pagination.__dict__['has_previous'] = True if pagination.page > 1 else False
    pagination.__dict__['has_next'] = True if pagination.page < pagination.pages else False
    pagination.__dict__['next_page'] = pagination.page + 1 if pagination.has_next is True else None
    pagination.__dict__['previous_page'] = pagination.page - 1 if pagination.has_previous is True else None
    return pagination


def format_response_paging(data):
    return {
        "items": [item.json for item in data.items],
        "has_next": data.has_next,
        "has_previous": data.has_previous,
        "next_page": data.next_page,
        "previous_page": data.previous_page,
        "page": data.page,
        "pages": data.pages,
        "per_page": data.per_page,
        "total": data.total
    }


def ResponseSuccess(data):
    return {
               'success': True,
               'data': data
           }, 200


def ResponseError():
    return {
               'success': False
           }, 200
