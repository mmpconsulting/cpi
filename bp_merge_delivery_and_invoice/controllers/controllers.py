# -*- coding: utf-8 -*-
# from odoo import http


# class BpMergeDeliveryAndInvoice(http.Controller):
#     @http.route('/bp_merge_delivery_and_invoice/bp_merge_delivery_and_invoice', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/bp_merge_delivery_and_invoice/bp_merge_delivery_and_invoice/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('bp_merge_delivery_and_invoice.listing', {
#             'root': '/bp_merge_delivery_and_invoice/bp_merge_delivery_and_invoice',
#             'objects': http.request.env['bp_merge_delivery_and_invoice.bp_merge_delivery_and_invoice'].search([]),
#         })

#     @http.route('/bp_merge_delivery_and_invoice/bp_merge_delivery_and_invoice/objects/<model("bp_merge_delivery_and_invoice.bp_merge_delivery_and_invoice"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('bp_merge_delivery_and_invoice.object', {
#             'object': obj
#         })
