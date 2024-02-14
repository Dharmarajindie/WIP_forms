# import frappe
from frappe.model.document import Document
from frappe import _
import frappe

class WIPForm1ClientDetails(Document):
    def validate(self):
        errors = []
        if self.mobile:
            mobile_error = self.validate_mobile()
            if mobile_error:
                errors.append(mobile_error)
        
        if self.email:
            email_error = self.validate_email()
            if email_error:
                errors.append(email_error)

        if errors:
            frappe.throw("\n".join(errors))

    def validate_mobile(self):
        if not self.mobile.isdigit() or len(self.mobile) != 10:
            return _("Mobile number must be a 10-digit numeric value")
        return None

    def validate_email(self):
        import re
        if not re.match(r"[^@]+@[^@]+\.[^@]+", self.email):
            return _("Invalid email format")
        return None
