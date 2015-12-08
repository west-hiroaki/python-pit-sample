# -*- coding: utf-8 -*-
from __future__ import absolute_import
# It is displayed and the '!!python/unicode' to enable
# from __future__ import unicode_literals

import pit
import os

if not os.environ.get('EDITOR'):
    os.environ['EDITOR'] = 'vi'

opts = {
    'require': {
        'id': 'your id',
        'password': 'your password',
    }
}
account = pit.Pit.get('test.account', opts)

print account['id']
print account['password']

