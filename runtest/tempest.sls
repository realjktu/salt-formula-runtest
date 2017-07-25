{% from "runtest/map.jinja" import tempest with context %}
{%- if tempest.enabled %}
myuser/myimage:mytag:
  cmd.run:
    - names:
      - docker build - < /tmp/Dockerfile
{%- endif %}
