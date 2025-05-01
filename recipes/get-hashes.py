import malcore_playbook.lib.api as api
import malcore_playbook.lib.settings as settings


__version__ = "0.1"
__hashsum__ = "d58ff3a26adc62dfa8cee1dce02f38de"
__author__ = "Thomas Perkins"
__excluded_plans__ = "free"


def plugin(*args, **kwargs):
    results = None
    try:
        filename = args[0][0]
    except:
        filename = None
    try:
        if filename is None:
            settings.logger.fatal("Unable to execute recipe, returning None")
            return results
        else:
            _api = api.Api()
            req = _api.upload_file(filename, "gethash")
            return req['data']['data']['hashes']
    except:
        return results

