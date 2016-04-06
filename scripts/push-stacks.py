# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import os
import subprocess


for name in os.listdir('stacks'):
    try:
        name, ext = name.split('.')
    except Exception:
        continue
    if ext != 'yml':
        continue
    command = ''
    command += 'tutum stack inspect {name} || '
    command += 'tutum stack create --sync -f stacks/{name}.yml -n {name} && '
    command += 'tutum stack update --sync -f stacks/{name}.yml {name}'
    command = command.format(name=name)
    subprocess.call(command, shell=True)
    print('Pushed stack: %s' % name)
