# -*- coding: utf-8 -*-

from odoo import models, fields, api


class extremous(models.Model):
    _name = 'data.warga'
    _description = 'Data Warga'

    # DATA DIRI =======================================================================
    name = fields.Char('Nama Lengkap')
    nik = fields.Char('NIK')
    tempat_lahir = fields.Char('Tempat Lahir')
    tanggal_lahir = fields.Date('Tanggal Lahir')
    agama = fields.Selection([('islam', 'Islam'),('kristen', 'Kristen'),('katolik', 'Katolik'),('hindu', 'Hindu'),('budha', 'Budha'),('konghucu', 'Konghucu')], string='Agama')
    pendidikan_terakhir = fields.Selection([('sd', 'Sekolah Dasar'),('sma_smk', 'SMA / SMK / Sederajat'),('d3', 'D3'),('d4', 'D4'),('s1', 'S1'),('s2', 'S2'),('s3', 'S3'),('lainnya', 'Lainnya'),], string='Pendidikan Terakhir')
    nomor_telepon = fields.Char('Nomor Telepon')
    email = fields.Char('Email', help='BILA MEMPUNYAI EMAIL')
    
    # ALAMAT ==========================================================================
    # KOTA ADMINISTRASI ===============================================================
    kota_administrasi = fields.Selection([('jkt_timur', 'Jakarta Timur'),('jkt_barat', 'Jakarta Barat'),('jkt_selatan', 'Jakarta Selatan'),('jkt_utara', 'Jakarta Utara'),('jkt_pusat', 'Jakarta Pusat'),('kep_seribu', 'Kepulauan Seribu'),], string='Kota Administrasi')

    # KECAMATAN =======================================================================
    kec_jkt_timur = fields.Selection([('cakung', 'Cakung'),('cipayung', 'Cipayung'),('ciracas', 'Ciracas'),('duren_sawit', 'Duren Sawit'),('jatinegara', 'Jatinegara'),('kramat_jati', 'Kramat Jati'),('makasar', 'Makasar'),('matraman', 'Matraman'),('pasar_rebo', 'Pasar Rebo'),('pulogadung', 'Pulogadung')], string='Kecamatan')
    kec_jkt_barat = fields.Selection([('cengkareng', 'Cengkareng'),('grogol_petamburan', 'Grogol Petamburan'),('taman_sari', 'Taman Sari'),('tambora', 'Tambora'),('kebon_jeruk', 'Kebon Jeruk'),('kalideres', 'Kalideres'),('palmerah', 'palmerah'),('kembangan', 'Kembangan')], string='Kecamatan')
    kec_jkt_selatan = fields.Selection([('cilandak', 'Cilandak'),('jagakarsa', 'Jagakarsa'),('keb_baru', 'Keb. Baru'),('keb_lama', 'Keb. Lama'),('mampang_prap', 'Mampang Prapatan'),('pancoran', 'Pancoran'),('pasar_minggu', 'Pasar Minggu'),('setia_budi', 'Setia Budi'),('tebet', 'Tebet')], string='Kecamatan')
    kec_jkt_utara = fields.Selection([('cilincing', 'Cilincing'),('kelapa_gading', 'Kelapa Gading'),('koja', 'Koja'),('pademangan', 'Pademangan'),('penjaringan', 'Penjaringan'),('tanjung_priok', 'Tanjung Priok')], string='Kecamatan')
    kec_jkt_pusat = fields.Selection([('cempaka_putih', 'Cempaka Putih'),('gambir', 'Gambir'),('johar_baru', 'Johar Baru'),('kemayoran', 'Kemayoran'),('menteng', 'Menteng'),('sawah_besar', 'Sawah Besar'),('senen', 'Senen'),('tanah_abang', 'Tanah Abang')], string='Kecamatan')
    kec_kep_seribu = fields.Selection([('kep_seribu_utara', 'Kepulauan Seribu Utara'),('kep_seribu_selatan', 'Kepulauan Seribu Selatan')], string='Kecamatan')
    
    # KELURAHAN JAKARTA TIMUR ==========================================================
    kel_cakung = fields.Selection([('cakung_barat', 'Cakung Barat'),('cakung_timur', 'Cakung Timur'),('jatinegara', 'Jatinegara'),('penggilingan', 'Penggilingan'),('pulo_gebang', 'Pulo Gebang'),('pulogadung', 'Rawa Terate'),('ujung_menteng', 'Ujung Menteng')], string='Kelurahan')
    kel_cipayung = fields.Selection([('bambu_apus', 'Bambu Apus'),('ceger', 'Ceger'),('cilangkap', 'Cilangkap'),('cipayung', 'Cipayung'),('lubang_buaya', 'Lubang Buaya'),('munjul', 'Munjul'),('pondok_ranggon', 'Pondok Ranggon'),('setu', 'Setu')], string='Kelurahan')
    kel_ciracas = fields.Selection([('cibubur', 'Cibubur'),('ciracas', 'Ciracas'),('kelapa_dua_wetan', 'Kelapa Dua Wetan'),('rambutan', 'Rambutan'),('susukan', 'Susukan')], string='Kelurahan')
    kel_duren_sawit = fields.Selection([('duren_sawit', 'Duren Sawit'),('klender', 'Klender'),('malaka_jaya', 'Malaka Jaya'),('malaka_sari', 'Malaka Sari'),('pondok_kopi', 'Pondok Bambu'),('pondok_kelapa', 'Pondok Kelapa'),('pondok_kopi', 'Pondok Kopi')], string='Kelurahan')
    kel_jatinegara = fields.Selection([('bali_mester', 'Bali Mester'),('bidara_cina', 'Bidara Cina'),('cipinang_besar_selatan', 'Cipinang Besar Selatan'),('cipinang_besar_utara', 'Cipinang Besar Utara'),('cipinang_cempedak', 'Cipinang Cempedak'),('cipinang_muara', 'Cipinang Muara'),('kampung_melayu', 'Kampung Melayu'),('rawa_bunga', 'Rawa Bunga')], string='Kelurahan')
    kel_kramat_jati = fields.Selection([('balekambang', 'Balekambang'),('batu_ampar', 'Batu Ampar'),('cawang', 'Cawang'),('cililitan', 'Cililitan'),('dukuh', 'Dukuh'),('kramat_jati', 'Kramat Jati'),('tengah', 'Tengah')], string='Kelurahan')
    kel_makasar = fields.Selection([('cipinang_melayu', 'Cipinang Melayu'),('halim_perdana_kusuma', 'Halim Perdana Kusuma'),('kebon_pala', 'Kebon Pala'),('makasar', 'Makasar'),('pinang_ranti', 'Pinang Ranti')], string='Kelurahan')
    kel_matraman = fields.Selection([('kayu_manis', 'Kayu Manis'),('kebon_manggis', 'Kebon Manggis'),('pal_meriam', 'Pal Meriam'),('pisangan_baru', 'Pisangan Baru'),('utan_kayu_selatan', 'Utan Kayu Selatan'),('utan_kayu_utara', 'Utan Kayu Utara')], string='Kelurahan')
    kel_pasar_rebo = fields.Selection([('baru', 'Baru'),('cijantung', 'Cijantung'),('gedong', 'Gedong'),('kalisari', 'Kalisari'),('pekayon', 'Pekayon')], string='Kelurahan')
    kel_pulogadung = fields.Selection([('cipinang', 'Cipinang'),('jati', 'Jati'),('jatinegara_kaum', 'Jatinegara Kaum'),('kayu_putih', 'Kayu Putih'),('pisangan_timur', 'Pisangan Timur'),('pulogadung', 'Pulo Gadung'),('rawamangun', 'Rawamangun')], string='Kelurahan')

    # KELURAHAN JAKARTA BARAT ==========================================================
    @api.onchange('kota_administrasi')
    def _onchange_kota_administrasi(self):
        if self.kota_administrasi:
            self.kec_jkt_timur = False
            self.kec_jkt_barat = False
            self.kec_jkt_selatan = False
            self.kec_jkt_utara = False
            self.kec_kep_seribu = False
    
    @api.onchange('kec_jkt_timur')
    def _onchange_kec_jkt_timur(self):
        if self.kec_jkt_timur:
            self.kel_cakung == False
            self.kel_cipayung == False
            self.kel_ciracas == False
            self.kel_duren_sawit == False
            self.kel_jatinegara == False
            self.kel_kramat_jati == False
            self.kel_makasar == False
            self.kel_matraman == False
            self.kel_pasar_rebo == False
            self.kel_pulogadung == False