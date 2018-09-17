# -*- coding: utf-8 -*-

from pydpkg import Dpkg



deb = Dpkg("debs/clutch20rc_2.0.4.deb")
# deb = Dpkg("debs/audioenglish_1.0.deb")

print deb.headers
print dir(deb)
print deb