#!/usr/bin/env python

from common import client
from common import ext_net_manager
from common import utils
import netaddr
import unittest
import settings
import logging

logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger('External Network Test')

class ExtNetworkCreate(unittest.TestCase):
    def setUp(self):
        self.jclient = client.Client()
        self.ext_net_manager = ext_net_manager.ExtNetworkManager()
	
    def test_check_ext_network_create(self):
	resp = self.ext_net_manager.create_ext_network(
                                                 '15.15.15.0/24',
                                                 '15.15.15.3',
                                                 '15.15.15.250',
                                                 '15.15.15.1')

        if resp.get('floatingip') == '15':
           log.info("Test: Floating-up Update: PASS");
           return
        else:
           log.error('Failed to update: FIP='+resp.get('floatingip'))
           self.fail(resp)

    def tearDown(self):
	print "...... Leave the quota updated Nothing to be done : "

if __name__ == '__main__':
    unittest.main()


