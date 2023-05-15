import uuid
# Inganji backend needs to have access
#  to the payment gateway's API credentials in order to process transactions(We will note send API post request
#  and plain text response)
# The backend should keep track of the payment status for each transaction, such as whether 
# it was successful, declined, or pending.
#  The backend should store information about each payment, such as the payment amount, payment method,
#   and customer information.
# The backend should be able to generate error messages in case there are issues 
# with processing a payment.

class Payments:
    def __init__(self, payment_gateway_credentials,payment_status,payment_information):

        self.payment_gateway_credentials= payment_gateway_credentials
        self.payment_status={} 
        # We used Dictionary on payment status, to show whether the transaction was successful,
        # declined or is on  progress with its corresponding transaction ID.
        self.payment_information={}
           
    #    Inganji  would like to track every transaction from the transaction ID
        
    def transaction_identifier(self):
        transactionID = str(uuid.uuid4())[:3].upper()
        return transactionID
   

    def process_payment(self, payment_info):
        self.payment_status[payment_info["payment_id"]]= payment_status
        self.payment_information[payment_info[payment_id]]= payment_info

        
        
    def refund_payment(self,payment_id):
        self.payment_status[payment_id] 
        return "refunded"   

    def know_receipt(self,payment_id):
        return (f"recived payment from{self.payment_id}")
    
    
    def send_payment_confirmation(self,payment_id):
        customer_email= self.payment_info[self.payment_id]["customer_email"]

   
    
   
