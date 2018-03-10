# -*- coding: utf-8 -*-

import enchant

d = enchant.Dict("en_US")

print (d.check("Hello"))