from modules.laravel.Request import LaravelRequest as Request


def read_learning_log(user_id: str):
    return Request.get(f'home',
                       params={'user_id': user_id,
                               #    'year': year,
                               #    'month': month
                               })


def create_learning_log(user_id: str, params: dict):
    return Request.post(f'home', params={'user_id': user_id}, json=params)
