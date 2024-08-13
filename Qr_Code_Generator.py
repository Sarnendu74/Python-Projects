# Import module
import qrcode

# Taking Upi ID from User
upi_id = input("Enter UPI ID = ")

# Intialize Payment_url to store format
payment_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'

# Making QR for GPAY,PAYTM,PHONE PE
payment_qr = qrcode.make(payment_url)


payment_qr.save("Payment.png")

payment_qr.show()
