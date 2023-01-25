from modules.laravel.Request import LaravelRequest as Request


def read_langs_contents():
    return Request.get(f'curriculums')
