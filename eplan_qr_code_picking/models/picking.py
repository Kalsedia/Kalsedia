from odoo import models, fields, api
from io import BytesIO
import base64

try:
    import qrcode
except ImportError:
    qrcode = None


class StockPicking(models.Model):
    _inherit = "stock.picking"

    @api.model
    def create(self, vals):
        res = super(StockPicking, self).create(vals)
        is_create_qr_code = self.env['ir.config_parameter'].sudo().get_param(
            'sh_product_qrcode_generator.is_sh_product_qrcode_generator_when_create')
        if is_create_qr_code:
            qr_sequence = self.env['ir.sequence'].next_by_code(
                'seq.sh_product_qrcode_generator')
            if qr_sequence:
                qr_code = qr_sequence
                qr = qrcode.QRCode(
                    version=1,
                    error_correction=qrcode.constants.ERROR_CORRECT_L,
                    box_size=10,
                    border=4,
                )
                qr.add_data(qr_code)
                qr.make(fit=True)

                img = qr.make_image()
                temp = BytesIO()
                img.save(temp, format="PNG")
                qr_code_image = base64.b64encode(temp.getvalue())

                res.x_studio_qr_code = qr_code
                res.x_studio_qr_code_image = qr_code_image

        return res

    @api.onchange('x_studio_qr_code')
    def onchange_sh_qr_code(self):
        if self:
            if self.x_studio_qr_code:
                qr_code = self.x_studio_qr_code
                qr = qrcode.QRCode(
                    version=1,
                    error_correction=qrcode.constants.ERROR_CORRECT_L,
                    box_size=10,
                    border=4,
                )
                qr.add_data(qr_code)
                qr.make(fit=True)

                img = qr.make_image()
                temp = BytesIO()
                img.save(temp, format="PNG")
                qr_code_image = base64.b64encode(temp.getvalue())

                self.x_studio_qr_code_image = qr_code_image

            else:
                self.x_studio_qr_code = False
                self.x_studio_qr_code_image = False
