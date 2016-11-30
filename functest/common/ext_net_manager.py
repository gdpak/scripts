import base_manager
import utils
import xmltodict
import json
import os
import pdb
from jcsclient import requestify 
from jcsclient import config 

class ExtNetworkManager(base_manager.BaseManager):
    
    def __init__(self):
        self.url = config.get_service_url('vpc')
        self.headers = {}
        self.version = '2016-03-01'
        self.verb = 'GET'

    def create_ext_network(self, cidr_block, start, end, gatewayip):
        params = {}
        params['Version']= self.version
        params['Action'] = 'CreateExtnetwork'
        params['cidr_block'] = cidr_block
        params['start'] = start
        params['end'] = end
        params['gatewayip'] = gatewayip
        resp = requestify.make_request(self.url, self.verb,
                self.headers, params)
        if resp is not None:
            try:
                resp_dict = json.loads(resp.content)
            except:
                resp_dict = xmltodict.parse(resp.content)
                resp_json = json.dumps(resp_dict, indent=4, sort_keys=True)
                resp_dict = json.loads(resp_json)
            return resp_dict
        return 'FAIL'
