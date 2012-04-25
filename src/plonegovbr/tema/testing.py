# -*- coding: utf-8 -*-

from plone.app.testing import PloneSandboxLayer
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import IntegrationTesting
from plone.app.testing import FunctionalTesting


class Fixture(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load ZCML
        import plone.app.theming
        self.loadZCML(package=plone.app.theming)
        import plonegovbr.tema
        self.loadZCML(package=plonegovbr.tema)

    def setUpPloneSite(self, portal):
        # Install into Plone site using portal_setup
        self.applyProfile(portal, 'plonegovbr.tema:default')


FIXTURE = Fixture()
INTEGRATION_TESTING = IntegrationTesting(
    bases=(FIXTURE,),
    name='plonegovbr.tema:Integration',
    )
FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(FIXTURE,),
    name='plonegovbr.tema:Functional',
    )
