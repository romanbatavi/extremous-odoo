from odoo import models, fields, api

class MasterKotaAdministrasi(models.Model):
    _name = 'master.kota.administrasi'
    _description = 'Master Kota Administrasi'

    nama_kota = fields.Char('Nama Kota')    
    is_kota = fields.Selection([
        ('timur', 'Jakarta Timur'),
        ('barat', 'Jakarta Barat'),
        ('selatan', 'Jakarta Selatan'),
        ('utara', 'Jakrta Utara'),
        ('pusat', 'Jakarta Pusat'),
        ('kep_seribu', 'Kep.Seribu')
    ], string='Kota Administrasi')

    def name_get(self):
        result = []
        for record in self:
            name = record.nama_kota
            result.append((record.id, name))
        return result