# -*- coding: utf-8 -*-
# from odoo import http


# class FlowerApp(http.Controller):
#     @http.route('/flower_app/flower_app', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/flower_app/flower_app/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('flower_app.listing', {
#             'root': '/flower_app/flower_app',
#             'objects': http.request.env['flower_app.flower_app'].search([]),
#         })

#     @http.route('/flower_app/flower_app/objects/<model("flower_app.flower_app"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('flower_app.object', {
#             'object': obj
#         })
