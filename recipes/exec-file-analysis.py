import time

# These imports will import the API you will need (feel free to use your own)
import malcore_playbook.lib.api as api
# As well as the settings file so that you can use whatever settings you need
import malcore_playbook.lib.settings as settings


# Version of the plugins is required
__version__ = "0.1"
# MD5 sum of the plugin is required
__hashsum__ = "9d4ffa87d3dabd8a4468d0b3b43161f9"
# Whatever handle you want to use is up to you
__author__ = "Thomas Perkins"
# This can be None or you can choose what plans to exclude: free, cyber analyst, analyst, etc
# you can see the full plan list here: https://malcore.io/pricing
__excluded_plans__ = "free"


# You may pass whatever arguments you want to this and pass them via CLI when calling the plugin
def plugin(*args, **kwargs):
    results = None
    try:
        filename = args[0][0]
    except:
        filename = None
    try:
        api_ = api.Api()
        req = api_.upload_file(filename, "upload")
        status = req['data']['data']['status']
        uuid = req['data']['data']['uuid']
        settings.logger.info(f"Analysis is currently: {status} with UUID: {uuid}")
        is_done = False
        while not is_done:
            status_req = api_.status_check(uuid)
            try:
                status_check = status_req['data']['status']
                if status_check == 'running':
                    settings.logger.debug("Status is running, will sleep for 15 seconds and wait")
                    time.sleep(15)
            except KeyError:
                return status_req['data']['output']
    except:
        return results
