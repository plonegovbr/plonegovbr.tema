# -*- coding:utf-8 -*-
from collective.grok import gs

PROJECTNAME = 'plonegovbr.tema'
PROFILE_ID = 'plonegovbr.tema:default'


# Default Profile
gs.profile(name=u'default',
           title=u'Tema PloneGov.Br',
           description=u'Tema modelo para portais do Governo Brasileiro',
           directory='profiles/default')

# Uninstall Profile
gs.profile(name=u'uninstall',
           title=u'Uninstall: Tema PloneGov.Br',
           description=u'Desinstala plonegovbr.tema',
           directory='profiles/uninstall')
