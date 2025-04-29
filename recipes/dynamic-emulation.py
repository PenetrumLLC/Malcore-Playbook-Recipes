import malcore_playbook.lib.api as api
import malcore_playbook.lib.settings as settings


__version__ = "0.1"
__hashsum__ = "8311e49cce322aef0102c929aa00fda2"
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
        api_ = api.Api()
        req = api_.upload_file(filename, "dynamicanalysis")
        data = req['data']['data'][0]['dynamic_analysis']
        results = data
        return results
    except:
        return results
