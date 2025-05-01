# These imports will import the API you will need (feel free to use your own)
import malcore_playbook.lib.api as api
# As well as the settings file so that you can use whatever settings you need
import malcore_playbook.lib.settings as settings


# Version of the plugins is required
__version__ = "0.1"
# MD5 sum of the plugin is required
__hashsum__ = "a0b0fe453c837316d58cc733b32af30e"
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
        req = api_.upload_file(filename, "deepstatic")
        return req['data']['data']['results']
    except:
        return results
