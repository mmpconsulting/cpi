# -*- coding: utf-8 -*-
# from odoo import http


# class Addons\reportPenerimaan(http.Controller):
#     @http.route('/addons\report_penerimaan/addons\report_penerimaan', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/addons\report_penerimaan/addons\report_penerimaan/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('addons\report_penerimaan.listing', {
#             'root': '/addons\report_penerimaan/addons\report_penerimaan',
#             'objects': http.request.env['addons\report_penerimaan.addons\report_penerimaan'].search([]),
#         })

#     @http.route('/addons\report_penerimaan/addons\report_penerimaan/objects/<model("addons\report_penerimaan.addons\report_penerimaan"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('addons\report_penerimaan.object', {
#             'object': obj
#         })
