from odoo import models, fields, api


class MasterKecamatan(models.Model):
    _name = 'master.kecamatan'
    _description = 'Master Kecamatan'

    master_kota_administrasi_id = fields.Many2one('master.kota.administrasi', string='Kota Administrasi')
    is_kecamatan = fields.Selection([
        ('cempaka_putih', 'Cempaka Putih'),
        ('gambir', 'Gambir'),
        ('johar_baru', 'Johar Baru'),
        ('kemayoran', 'Kemayoran'),
        ('menteng', 'Menteng'),
        ('sawah_besar', 'Sawah Besar'),
        ('senen', 'Senen'),
        ('tanah_abang', 'Tanah Abang'),
        ('cilincing', 'Cilincing'),
        ('kelapa_gading', 'Kelapa Gading'),
        ('koja', 'Koja'),
        ('pademangan', 'Pademangan'),
        ('penjaringan', 'Penjaringan'),
        ('tanjung_priok', 'Tanjung Priok'),
        ('cakung', 'Cakung'),
        ('cipayung', 'Cipayung'),
        ('ciracas', 'Ciracas'),
        ('duren_sawit', 'Duren Sawit'),
        ('jatinegara', 'Jatinegara'),
        ('kramat_jati', 'Kramat Jati'),
        ('makasar', 'Makasar'),
        ('matraman', 'Matraman'),
        ('pasar_rebo', 'Pasar Rebo'),
        ('pulo_gadung', 'Pulo Gadung')
    ], string='Kecamatan')
    