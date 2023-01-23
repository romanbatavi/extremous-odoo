# -*- coding: utf-8 -*-

from odoo import models, fields, api


class extremous(models.Model):
    _name = 'data.warga'
    _description = 'Data Warga'

    # DATA DIRI
    name = fields.Char('Nama Lengkap')
    nik = fields.Char('NIK')
    tempat_lahir = fields.Char('Tempat Lahir')
    tanggal_lahir = fields.Date('Tanggal Lahir')
    agama = fields.Selection([
        ('islam', 'Islam'),
        ('kristen', 'Kristen'),
        ('katolik', 'Katolik'),
        ('hindu', 'Hindu'),
        ('budha', 'Budha'),
        ('konghucu', 'Konghucu')
    ], string='Agama')
    pendidikan_terakhir = fields.Selection([
        ('sd', 'Sekolah Dasar'),
        ('sma_smk', 'SMA / SMK / Sederajat'),
        ('d3', 'D3'),
        ('d4', 'D4'),
        ('s1', 'S1'),
        ('s2', 'S2'),
        ('s3', 'S3'),
        ('lainnya', 'Lainnya'),
    ], string='Pendidikan Terakhir')
    nomor_telepon = fields.Char('Nomor Telepon')
    email = fields.Char('Email', help='BILA MEMPUNYAI EMAIL')
    
    # =================================== ALAMAT ===================================
    # ===================================ALAMAT===================================
    kota_administrasi = fields.Selection([
        ('jkt_timur', 'Jakarta Timur'),
        ('jkt_barat', 'Jakarta Barat'),
        ('jkt_selatan', 'Jakarta Selatan'),
        ('jkt_utara', 'Jakarta Utara'),
        ('jkt_pusat', 'Jakarta Pusat'),
        ('kep_seribu', 'Kepulauan Seribu'),
    ], string='Kota Administrasi')
    kec_jkt_timur = fields.Selection([
        ('cakung', 'Cakung'),
        ('cipayung', 'Cipayung'),
        ('ciracas', 'Ciracas'),
        ('duren_sawit', 'Duren Sawit'),
        ('jatinegara', 'Jatinegara'),
        ('kramat_jati', 'Kramat Jati'),
        ('makasar', 'Makasar'),
        ('matraman', 'Matraman'),
        ('pasar_rebo', 'Pasar Rebo'),
        ('pulogadung', 'Pulogadung')
    ], string='Kecamatan')
    kec_jkt_barat = fields.Selection([
        ('cengkareng', 'Cengkareng'),
        ('grogol_petamburan', 'Grogol Petamburan'),
        ('taman_sari', 'Taman Sari'),
        ('tambora', 'Tambora'),
        ('kebon_jeruk', 'Kebon Jeruk'),
        ('kalideres', 'Kalideres'),
        ('palmerah', 'palmerah'),
        ('kembangan', 'Kembangan')
    ], string='Kecamatan')
    kec_jkt_selatan = fields.Selection([
        ('cilandak', 'Cilandak'),
        ('jagakarsa', 'Jagakarsa'),
        ('keb_baru', 'Keb. Baru'),
        ('keb_lama', 'Keb. Lama'),
        ('mampang_prap', 'Mampang Prapatan'),
        ('pancoran', 'Pancoran'),
        ('pasar_minggu', 'Pasar Minggu'),
        ('setia_budi', 'Setia Budi'),
        ('tebet', 'Tebet')
    ], string='Kecamatan')
    kec_jkt_utara = fields.Selection([
        ('cilincing', 'Cilincing'),
        ('kelapa_gading', 'Kelapa Gading'),
        ('koja', 'Koja'),
        ('pademangan', 'Pademangan'),
        ('penjaringan', 'Penjaringan'),
        ('tanjung_priok', 'Tanjung Priok')
    ], string='Kecamatan')
    kec_jkt_pusat = fields.Selection([
        ('cempaka_putih', 'Cempaka Putih'),
        ('gambir', 'Gambir'),
        ('johar_baru', 'Johar Baru'),
        ('kemayoran', 'Kemayoran'),
        ('menteng', 'Menteng'),
        ('sawah_besar', 'Sawah Besar'),
        ('senen', 'Senen'),
        ('tanah_abang', 'Tanah Abang')
    ], string='Kecamatan')
    kec_kep_seribu = fields.Selection([
        ('kep_seribu_utara', 'Kepulauan Seribu Utara'),
        ('kep_seribu_selatan', 'Kepulauan Seribu Selatan')
    ], string='Kecamatan')