# coding: utf-8
import sys
import os
from jinja2 import Template

template = Template("Your input: {}".format(sys.argv[1] if len(sys.argv) > 1 else '<empty>'))
template.globals['os'] = os

print template.render()