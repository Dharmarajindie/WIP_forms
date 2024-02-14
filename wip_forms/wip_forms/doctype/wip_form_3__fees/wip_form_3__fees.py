# Copyright (c) 2024, Dharmaraj and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class WIPForm3Fees(Document):
	
	def validate(self):
		if self.deal_type == 'Outright/Sale' and self._of_deal_valueno_of_months_of_rentals and self.rate_unitrate_per_month and self.rateexpected_tenure_in_months:
			self.deal_value = self.arearate_per_month_per_seat * self.rateexpected_tenure_in_months * (self.rate_unitrate_per_month/self.area_unitno_of_seats) 
			if self.deal_value>0:
				self.fees_amount = self.deal_value * (self._of_deal_valueno_of_months_of_rentals/100) 

		elif self.deal_type == 'Outright/Sale' and self._of_deal_valueno_of_months_of_rentals and self.rate_unitrate_per_month and self.rateexpected_tenure_in_months:
			self.deal_value = self.arearate_per_month_per_seat * self.rateexpected_tenure_in_months 
			if self.deal_value>0:
				self.fees_amount = self.deal_value * (self.rateexpected_tenure_in_months*self.rate_unitrate_per_month) 

		elif self.deal_type == 'Outright/Sale' and self._of_deal_valueno_of_months_of_rentals and self.rate_unitrate_per_month and self.rateexpected_tenure_in_months:
			self.deal_value = self.area_unitno_of_seats * self.rateexpected_tenure_in_months * self.arearate_per_month_per_seat 
			if self.deal_value>0:
				self.fees_amount = self.deal_value * (self.rateexpected_tenure_in_months*self.rate_unitrate_per_month) 

		else:
			missing_fields = []
			if not self._of_deal_valueno_of_months_of_rentals:
				missing_fields.append("Number of months of rentals")
			if not self.rate_unitrate_per_month:
				missing_fields.append("Rate per month")
			if not self.rateexpected_tenure_in_months:
				missing_fields.append("Expected tenure in months")
		
			if missing_fields:
				frappe.throw(f"Please enter the following required fields: {', '.join(missing_fields)}")