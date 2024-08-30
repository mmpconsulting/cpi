# -*- coding: utf-8 -*-
# from odoo import http


# class DymoNoprice(http.Controller):
#     @http.route('/dymo_noprice/dymo_noprice', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/dymo_noprice/dymo_noprice/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('dymo_noprice.listing', {
#             'root': '/dymo_noprice/dymo_noprice',
#             'objects': http.request.env['dymo_noprice.dymo_noprice'].search([]),
#         })

#     @http.route('/dymo_noprice/dymo_noprice/objects/<model("dymo_noprice.dymo_noprice"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('dymo_noprice.object', {
#             'object': obj
#         })
