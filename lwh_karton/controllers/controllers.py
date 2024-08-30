# -*- coding: utf-8 -*-
# from odoo import http


# class LwhKarton(http.Controller):
#     @http.route('/lwh_karton/lwh_karton', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/lwh_karton/lwh_karton/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('lwh_karton.listing', {
#             'root': '/lwh_karton/lwh_karton',
#             'objects': http.request.env['lwh_karton.lwh_karton'].search([]),
#         })

#     @http.route('/lwh_karton/lwh_karton/objects/<model("lwh_karton.lwh_karton"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('lwh_karton.object', {
#             'object': obj
#         })
