# -*- coding: utf-8 -*-
# from odoo import http


# class PickingModule(http.Controller):
#     @http.route('/picking_module/picking_module/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/picking_module/picking_module/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('picking_module.listing', {
#             'root': '/picking_module/picking_module',
#             'objects': http.request.env['picking_module.picking_module'].search([]),
#         })

#     @http.route('/picking_module/picking_module/objects/<model("picking_module.picking_module"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('picking_module.object', {
#             'object': obj
#         })
