from odoo import http


class SpaceMission(http.Controller):
    @http.route('/space_mission/', auth='public', website=True, sitemap=True)
    def index(self, **kw):
        return 'Welcome to the Odoo Space Mission Site'
    
    @http.route('/space_mission/missions/', auth='public', website=True, sitemap=False)
    def missions(self,**kw):
        missions = http.request.env['mission.info'].search([])
        return http.request.render('space_mission.mission_website',{
            'missions': missions,
        })
