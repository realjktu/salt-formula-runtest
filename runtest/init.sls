{%- if pillar.runtest is defined %}
include:
- runtest.service
{%- if pillar.runtest.tempest is defined %}
- runtest.tempest
{%- endif %}
{%- if pillar.runtest.stepler is defined %}
- runtest.stepler
{%- endif %}
{%- endif %}
