# -*- coding: utf-8 -*-
'''
'''

import jinja2
import logging

import salt.pillar

from runtest import tempest_sections

log = logging.getLogger(__name__)

__virtualname__ = 'runtest'


def __virtual__():
    return __virtualname__


CFG_TEMPLATE = """
{%- for section,options in config.items() -%}
[{{ section }}]
{%- for opt,val in options.items() %}
{{ opt }} = {{ val }}
{%- endfor %}

{% endfor %}
"""

def _get_pillar_for_live_minions(timeout=5, gather_job_timeout=15):
    client = salt.client.get_local_client(__opts__['conf_file'])
    pillars = client.cmd('*', 'pillar.items', timeout=timeout,
                         gather_job_timeout=gather_job_timeout)

    return pillars

def generate_tempest_config(dst, *args, **kwargs):

    pillars = _get_pillar_for_live_minions()
    this_node_pillar = __opts__['pillar']
    runtest_opts =  this_node_pillar.get(__virtualname__, {}).get('tempest', {})
    config = {}

    for ts in tempest_sections.SECTIONS:
        ts_inst = ts(pillars, runtest_opts)
        config[ts_inst.name] = {}
        opts = {}
        for opt in ts_inst.options:
            val = getattr(ts_inst, opt)
            if val is None:
                val = runtest_opts.get(ts_inst.name, {}).get(opt, None)

            if val is not None:
                opts[opt] = val

        config[ts_inst.name] = opts

    data = jinja2.Environment().from_string(CFG_TEMPLATE).render(config=config)
    with open(dst, 'w') as cfg_file:
        cfg_file.write(data)

    return config
