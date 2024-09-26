# -*- coding: utf-8 -*-
# from odoo import http


# class QuotationsPdfReport(http.Controller):
#     @http.route('/quotations_pdf_report/quotations_pdf_report', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/quotations_pdf_report/quotations_pdf_report/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('quotations_pdf_report.listing', {
#             'root': '/quotations_pdf_report/quotations_pdf_report',
#             'objects': http.request.env['quotations_pdf_report.quotations_pdf_report'].search([]),
#         })

#     @http.route('/quotations_pdf_report/quotations_pdf_report/objects/<model("quotations_pdf_report.quotations_pdf_report"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('quotations_pdf_report.object', {
#             'object': obj
#         })
