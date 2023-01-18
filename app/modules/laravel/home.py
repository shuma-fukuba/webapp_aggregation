from modules.laravel.Request import LaravelRequest as Request


def read_home(user_id: str):
    return Request.get(f'home',
                       params={'user_id': user_id,
                            #    'year': year,
                            #    'month': month
                               })
