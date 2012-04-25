# -*- coding: utf-8 -*-
import logging

from collective.grok import gs

from plonegovbr.tema.config import PROJECTNAME


@gs.upgradestep(title=u'Initial upgrade steo',
                description=u'Upgrade step run at install time',
                source='0.0', destination='1000', sortkey=1,
                profile='plonegovbr.tema:default')
def fromZero(context):
    """ Upgrade from Zero to version 1000
    """
    pass