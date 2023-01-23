# -*- coding: utf-8 -*-
# from odoo import http


# class Extremous(http.Controller):
#     @http.route('/extremous/extremous/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/extremous/extremous/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('extremous.listing', {
#             'root': '/extremous/extremous',
#             'objects': http.request.env['extremous.extremous'].search([]),
#         })

#     @http.route('/extremous/extremous/objects/<model("extremous.extremous"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('extremous.object', {
#             'object': obj
#         })
