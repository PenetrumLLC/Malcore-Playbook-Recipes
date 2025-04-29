import malcore_playbook.lib.api as api
import malcore_playbook.lib.settings as settings


__version__ = "0.1"
__hashsum__ = "56154ea90ca2da5c4ee1fd4bed599ce5"
__author__ = "Thomas Perkins"
__excluded_plans__ = "free"


def plugin(*args, **kwargs):
    try:
        filename = args[0][0]
    except:
        filename = None
    try:
        if filename is None:
            settings.logger.fatal("No filename provided")
            return None
        _api = api.Api()
        req = _api.upload_file(filename, "strings")
        data = req['data']['data']['results']['strings']
        return data
    except:
        return None
