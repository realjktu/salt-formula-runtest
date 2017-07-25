{% from "runtest/map.jinja" import runtest with context %}

runtest_pkgs:
  pkg.installed:
    - names: {{ runtest.pkgs }}
