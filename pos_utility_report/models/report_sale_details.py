from odoo import api, fields, models


class ReportSaleDetails(models.AbstractModel):
   
    _inherit = 'report.point_of_sale.report_saledetails'

    @api.model
    def get_sale_details(self, date_start=False, date_stop=False, config_ids=False, session_ids=False):
        details_data = super(ReportSaleDetails, self).get_sale_details(date_start, date_stop, config_ids, session_ids)
        products = self.env['product.product']
        for prod in details_data['products']:
            product = products.search([('id', '=', prod['product_id'])])
            prod['standard_price'] = product.standard_price
        return details_data
