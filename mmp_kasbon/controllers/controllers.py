# -*- coding: utf-8 -*-
# from odoo import http


# class YmKasbon(http.Controller):
#     @http.route('/mmp_kasbon/mmp_kasbon', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/mmp_kasbon/mmp_kasbon/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('mmp_kasbon.listing', {
#             'root': '/mmp_kasbon/mmp_kasbon',
#             'objects': http.request.env['mmp_kasbon.mmp_kasbon'].search([]),
#         })

#     @http.route('/mmp_kasbon/mmp_kasbon/objects/<model("mmp_kasbon.mmp_kasbon"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('mmp_kasbon.object', {
#             'object': obj
#         })
