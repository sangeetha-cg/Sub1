from odoo import api, fields, models, _


class AccountAsset(models.Model):
    _inherit = "account.asset"

    manually_cancelled = fields.Boolean(string="Manually Cancelled")

    def cg_asset_cancel(self):
        for rec in self:
            if rec.depreciation_move_ids:
                for move in rec.depreciation_move_ids:
                    move.asset_id = False
                    move.button_cancel()
                rec.manually_cancelled = True
                rec.message_post(body=_("Asset Depreciation Cancelled by") % self.env.user.name)



