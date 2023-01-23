from odoo import models, fields, api

class MasterKotaAdministrasi(models.Model):
    _name = 'master.kota.administrasi'
    _description = 'Master Kota Administrasi'

    # nama_kota = fields.Char(compute='_compute_nama_kota', string='nama_kota')
                
    is_kota = fields.Selection([
        ('timur', 'Jakarta Timur'),
        ('barat', 'Jakarta Barat'),
        ('selatan', 'Jakarta Selatan'),
        ('utara', 'Jakrta Utara'),
        ('pusat', 'Jakarta Pusat'),
        ('kep_seribu', 'Kep.Seribu')
    ], string='Kota Administrasi')

    # @api.depends('is_kota')
    # def _compute_nama_kota(self):
    #     for kota in self:
    #         if kota.is_kota == 'timur':
    #             kota.nama_kota = 'Jakarta Timur'
    #         if kota.is_kota == 'barat':
    #             kota.nama_kota = 'Jakarta Barat'
    #         if kota.is_kota == 'selatan':
    #             kota.nama_kota = 'Jakarta Selatan'
    #         if kota.is_kota == 'utara':
    #             kota.nama_kota = 'Jakarta Utara'
    #         if kota.is_kota == 'pusat':
    #             kota.nama_kota = 'Jakarta Pusat'
    #         if kota.is_kota == 'kep_seribu':
    #             kota.nama_kota = 'Kep.Seribu'

    # def name_get(self):
    #     result = []
    #     for record in self:
    #         name = record.is_kota.dict(record._fields['is_kota'].selection).get(record.is_kota)
    #         result.append((record.id, name))
    #     return result