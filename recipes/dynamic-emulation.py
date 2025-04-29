import malcore_playbook.lib.api as api
import malcore_playbook.lib.settings as settings


__version__ = "0.1"
__hashsum__ = "3be6e99cdbcd7056a76515cfe595aa20"
__author__ = "Thomas Perkins"
__excluded_plans__ = "free"


def plugin(*args, **kwargs):
    results = ""
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
        for part in data:
            eps = part['entry_points']
            for ep in eps:
                apis = ep['apis']
                for _api in apis:
                    results += f"{_api['pc']}: {_api['api_name']}({','.join(_api['args'])})->{_api['ret_val']}\n"
        return results
    except:
        return results
