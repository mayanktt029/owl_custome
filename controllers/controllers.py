# -*- coding: utf-8 -*-
from odoo import http


class OwlCustom(http.Controller):
    @http.route('/owl_custom/owl_custom', auth='public')
    def index(self, **kw):
        return "Hello, world"

    @http.route('/owl_custom/owl_custom/objects', auth='public')
    def list(self, **kw):
        return http.request.render('owl_custom.listing', {
            'root': '/owl_custom/owl_custom',
            'objects': http.request.env['owl_custom.owl_custom'].search([]),
        })

    @http.route('/owl_custom/owl_custom/objects/<model("owl_custom.owl_custom"):obj>', auth='public')
    def object(self, obj, **kw):
        return http.request.render('owl_custom.object', {
            'object': obj
        })
