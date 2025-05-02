import re
import base64
import hashlib

import requests

import malcore_playbook.lib.api as api
import malcore_playbook.lib.settings as settings


__version__ = "0.1"
__hashsum__ = "90255b236445a349da629e109db116ff"
__author__ = "Thomas Perkins"
__excluded_plans__ = None


def lookup_cert(certificate_hash):
    searcher = re.compile('\"color\:\#CC0000\"\>Revoked.')
    url = "https://crt.sh/?q="
    try:
        req = requests.get(url + certificate_hash)
    except:
        req = None
    if req is None:
        return None
    else:
        if searcher.search(req.text) is not None:
            return True
        else:
            return False


def plugin(*args, **kwargs):
    results = None
    try:
        filename = args[0][0]
    except:
        filename = None
    try:
        if filename is None:
            settings.logger.fatal("No file was passed to the script")
            return None
        api_ = api.Api()
        exif_data_request = api_.upload_file(filename, "exif")
        sig_data = exif_data_request['data']['data']['signature_info']
        if not sig_data['is_signed']:
            settings.logger.debug("File is not signed, returning None")
            return None
        else:
            settings.logger.info("File is signed parsing the certificates")
            for item in sig_data['signature_results']:
                key = list(item.keys())[0]
                for cert in item[key]:
                    pem_version = cert['certificate_pem_version'].split("-----")[2].replace("\n", "")
                    der_version = base64.b64decode(pem_version)
                    sha1 = hashlib.sha1(der_version).hexdigest()
                    sha256 = hashlib.sha256(der_version).hexdigest()
                    looked_up = [[lookup_cert(sha1), sha1], [lookup_cert(sha256), sha256]]
                    for lookup in looked_up:
                        if lookup[0]:
                            settings.logger.warning("Found a revoked signature in the file")
                            return lookup
            settings.logger.info("Did not find any revoked signatures in the file")
            return None
    except:
        return results
