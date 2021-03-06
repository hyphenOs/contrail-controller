#
# Copyright (c) 2014 Juniper Networks, Inc. All rights reserved.
#

"""
This file contains implementation of netconf interface for QFX physical router
configuration manager
"""

from qfx_conf import QfxConf

class Qfx5kConf(QfxConf):
    _products = ['qfx5100', 'qfx5110']

    def __init__(self, logger, params={}):
        self._logger = logger
        self.physical_router = params.get("physical_router")
        super(Qfx5kConf, self).__init__()
    # end __init__

    @classmethod
    def register(cls):
        qconf = {
              "vendor": cls._vendor,
              "products": cls._products,
              "class": cls
            }
        return super(Qfx5kConf, cls).register(qconf)
    # end register

    def set_product_specific_config(self):
        if self.global_switch_options_config is None:
            self.global_switch_options_config = SwitchOptions(comment=DMUtils.switch_options_comment())
        self.global_switch_options_config.set_route_distinguisher(self.bgp_params['identifier'])
    # end set_product_specific_config

    def push_conf(self, is_delete=False):
        if not self.physical_router:
            return 0
        if is_delete:
            return self.send_conf(is_delete=True)
        self.set_qfx_common_config()
        return self.send_conf()
    # end push_conf

# end Qfx5kConf
