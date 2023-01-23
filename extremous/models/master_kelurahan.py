from odoo import models, fields, api

class MasterKelurahan(models.Model):
    _name = 'Master Kelurahan'
    _description = 'Master Kelurahan'

    master_kecamatan_id = fields.Many2one('master.kecamatan', string='Master Kecamatan')
    is_kelurahan = fields.Selection([
        ('cem_putih_barat', 'Cempaka Putih Barat'),
        ('cem_putih_timur', 'Cempaka Putih Timur'),
        ('rawasari', 'Rawasari'),
        ('cideng', 'Cideng'),
        ('duri_pulo', 'Duri Pulo'),
        ('gambir', 'Gambir'),
        ('kebon_kelapa', 'Kebon Kelapa'),
        ('petojo_selatan', 'Petojo Selatan'),
        ('petojo_utara', 'Petojo Utara'),
        ('cempaka_baru', 'Cempaka Baru'),
        ('gunung_sahari_selatan', 'Gunung Sahari Selatan'),
        ('harapan_mulya', 'Harapan Mulya'),
        ('kebon_kosong', 'Kebon Kosong'),
        ('kemayoran', 'Kemayoran'),
        ('serdang', 'Serdang'),
        ('sumur_batu', 'Sumur Batu'),
        ('utan_panjang', 'Utan Panjang')
    ], string='Kelurahan')