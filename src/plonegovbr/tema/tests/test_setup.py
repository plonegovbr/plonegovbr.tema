# -*- coding: utf-8 -*-

import unittest2 as unittest

from plone.app.testing import login
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.app.testing import TEST_USER_NAME

from plone.browserlayer.utils import registered_layers

from plonegovbr.tema.config import PROJECTNAME
from plonegovbr.tema.testing import INTEGRATION_TESTING

DEPENDENCIES = (
    'plone.app.theming',
    )

JS = [
    # XXX: Add JavaScript list here
    ]

CSS = [
    # XXX: Add Style Sheet list here
    ]


class BaseTestCase(unittest.TestCase):
    """base test case to be used by other tests"""

    layer = INTEGRATION_TESTING

    def setUpUser(self):
        setRoles(self.portal, TEST_USER_ID, ['Manager', 'Editor', 'Reviewer'])
        login(self.portal, TEST_USER_NAME)

    def setUp(self):
        portal = self.layer['portal']
        self.portal = portal
        self.qi = getattr(self.portal, 'portal_quickinstaller')
        self.pp = getattr(self.portal, 'portal_properties')
        self.wt = getattr(self.portal, 'portal_workflow')
        self.st = getattr(self.portal, 'portal_setup')
        self.setUpUser()


class TestInstall(BaseTestCase):
    """ensure product is properly installed"""

    def test_installed(self):
        self.assertTrue(self.qi.isProductInstalled(PROJECTNAME),
                        '%s not installed' % PROJECTNAME)

    def test_browserlayer(self):
        layers = [l.getName() for l in registered_layers()]
        self.assertTrue('IThemeSpecific' in layers,
                        'browser layer not installed')

    def test_javascript_registry(self):
        portal_javascripts = self.portal.portal_javascripts
        for js in JS:
            self.assertTrue(js in portal_javascripts.getResourceIds())

    def test_css_registry(self):
        portal_css = self.portal.portal_css
        for css in CSS:
            self.assertTrue(css in portal_css.getResourceIds())


class TestUninstall(BaseTestCase):
    """ensure product is properly uninstalled"""

    def setUp(self):
        BaseTestCase.setUp(self)
        self.qi.uninstallProducts(products=[PROJECTNAME])

    def test_uninstalled(self):
        self.assertFalse(self.qi.isProductInstalled(PROJECTNAME),
                         '%s not uninstalled' % PROJECTNAME)

    def test_browserlayer_removed(self):
        layers = [l.getName() for l in registered_layers()]
        self.assertFalse('IThemeSpecific' in layers,
                         'browser layer not removed')

    def test_javascript_registry_removed(self):
        portal_javascripts = self.portal.portal_javascripts
        for js in JS:
            self.assertFalse(js in portal_javascripts.getResourceIds())

    def test_css_registry_removed(self):
        portal_css = self.portal.portal_css
        for css in CSS:
            self.assertFalse(css in portal_css.getResourceIds())


def test_suite():
    return unittest.defaultTestLoader.loadTestsFromName(__name__)
