# -*- coding:utf-8 -*-

from plone.theme.interfaces import IDefaultPloneLayer


class IThemeSpecific(IDefaultPloneLayer):
    """Marker interface that defines a Zope 3 skin layer bound to a Skin
    """
