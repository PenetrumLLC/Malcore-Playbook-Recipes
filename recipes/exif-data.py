import malcore_playbook.lib.api as api
import malcore_playbook.lib.settings as settings


__version__ = "0.1"
__hashsum__ = "da785a19eca0ec95d1dafd13b6355bc0"
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
            req = _api.upload_file(filename, "exif")
            data = req['data']['data']
            with open('test.json', 'w') as fh:
                import json
                json.dump(data, fh, indent=4)
            results = data
    except:
        return results

    return results
