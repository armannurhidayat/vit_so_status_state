# -*- coding: utf-8 -*-
from odoo import http

# class VitSoStatus(http.Controller):
#     @http.route('/vit_so_status/vit_so_status/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/vit_so_status/vit_so_status/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('vit_so_status.listing', {
#             'root': '/vit_so_status/vit_so_status',
#             'objects': http.request.env['vit_so_status.vit_so_status'].search([]),
#         })

#     @http.route('/vit_so_status/vit_so_status/objects/<model("vit_so_status.vit_so_status"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('vit_so_status.object', {
#             'object': obj
#         })