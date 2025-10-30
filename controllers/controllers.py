# from odoo import http


# class TrainingManagement(http.Controller):
#     @http.route('/training_management/training_management', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/training_management/training_management/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('training_management.listing', {
#             'root': '/training_management/training_management',
#             'objects': http.request.env['training_management.training_management'].search([]),
#         })

#     @http.route('/training_management/training_management/objects/<model("training_management.training_management"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('training_management.object', {
#             'object': obj
#         })

