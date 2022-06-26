class PaypalPayment:
    payment_approval = True
    
    def is_approved(self):
        return self.payment_approval

class StripePayment:
    payment_approval = False
    
    def is_approved(self):
        return self.payment_approval
    
class PaymentVerification(PaypalPayment, StripePayment):
    pass

payment = PaymentVerification()
print(payment.is_approved())