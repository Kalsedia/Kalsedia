# -*- coding: utf-8 -*-
# Copyright (C) Softhealer Technologies.

from odoo import models, fields, api, _
from odoo.exceptions import Warning, UserError
from io import BytesIO
import base64

try:
    import qrcode
except ImportError:
    qrcode = None


class ShProductQRCodeGeneratorWizard(models.TransientModel):
    _name = 'sh.product.qrcode.generator.wizard'
    _description = 'Product QR Code Generator Wizard'


    # Generate Barcode for Existing Product
    is_overwrite_existing = fields.Boolean("Overwrite QR code If Exists")

    @api.model
    def default_get(self, fields):
        rec = super(ShProductQRCodeGeneratorWizard,
                    self).default_get(fields)

        active_ids = self._context.get('active_ids')
        active_model = self._context.get('active_model')

        if not active_ids:
            raise UserError(
                _("Programming error: wizard action executed without active_ids in context."))

        if not active_ids:
            return rec

        if active_model == 'stock.picking':
            products = self.env['stock.picking'].browse(active_ids)

            return rec
