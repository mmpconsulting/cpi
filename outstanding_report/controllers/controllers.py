# -*- coding: utf-8 -*-
# from odoo import http


# class OutstandingReport(http.Controller):
#     @http.route('/outstanding_report/outstanding_report', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/outstanding_report/outstanding_report/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('outstanding_report.listing', {
#             'root': '/outstanding_report/outstanding_report',
#             'objects': http.request.env['outstanding_report.outstanding_report'].search([]),
#         })

#     @http.route('/outstanding_report/outstanding_report/objects/<model("outstanding_report.outstanding_report"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('outstanding_report.object', {
#             'object': obj
#         })
