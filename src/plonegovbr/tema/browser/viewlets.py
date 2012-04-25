# -*- coding:utf-8 -*-

from plone.app.layout.viewlets import common

from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile


class FooterViewlet(common.FooterViewlet):
    index = ViewPageTemplateFile('templates/footer.pt')


class LogoViewlet(common.LogoViewlet):
    index = ViewPageTemplateFile('templates/logo.pt')

