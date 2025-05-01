# Malcore Playbook Recipe Directory

This repository contains the Malcore Playbook recipe directory. If you don't know what the Malcore Playbook is, please see [HERE](https://github.com/PenetrumLLC/Malcore-Playbook).

### Creating a Recipe

Creating a recipe is fairly simple, all you will need to do is follow the below template:

```python
# These imports will import the API you will need (feel free to use your own)
import malcore_playbook.lib.api as api
# As well as the settings file so that you can use whatever settings you need
import malcore_playbook.lib.settings as settings


# Version of the plugins is required
__version__ = ""
# MD5 sum of the plugin is required
__hashsum__ = ""
# Whatever handle you want to use is up to you
__author__ = ""
# This can be None or you can choose what plans to exclude: free, cyber analyst, analyst, etc
# you can see the full plan list here: https://malcore.io/pricing
__excluded_plans__ = ""


# You may pass whatever arguments you want to this and pass them via CLI when calling the plugin
def plugin(*args, **kwargs):
    results = None
    try:
        filename = args[0][0]
    except:
        filename = None
    try:
        # Put your code here
    except:
        return results
```

This template will give you a good understanding of how to create your own recipes. 

### Contributing

Please make sure that after you have created your recipe and added it to the `recipes` directory you run the `python generate_json.py` file to add your recipe to the directory.