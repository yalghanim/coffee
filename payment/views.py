from django.shortcuts import redirect, render
from suds.client import Client # pip install suds-jurko
from cart.models import Order

# TAP API Documentation: https://www.tap.company/developers/

def pay(request, order_id):
	order = Order.objects.get(id=order_id)
	payment_url = money(True, **{'customer': request.user,
								'qty': '1',
								'currency':'KWD',
								'price': order.cart.total,
								'order_id': order.id})
	return redirect(payment_url or 'payment:unsuccessful_pmt')


def money(isTest, *args, **kwargs):
	if not isTest:
		client = Client('https://www.gotapnow.com/webservice/PayGatewayService.svc?wsdl')
	else:
		client = Client('http://live.gotapnow.com/webservice/PayGatewayService.svc?wsdl')

	payment_request = client.factory.create('ns0:PayRequestDC')

	customer = kwargs.get('customer')

	# Customer Info
	payment_request.CustomerDC.Email = customer.email
	payment_request.CustomerDC.Mobile = ''
	payment_request.CustomerDC.Name = '%s %s'%(customer.first_name, customer.last_name)

	# Merchant Info
	if not isTest:
		payment_request.MerMastDC.MerchantID = tap_merchant_id
		payment_request.MerMastDC.UserName = tap_user
		payment_request.MerMastDC.Password = tap_password
		payment_request.MerMastDC.AutoReturn = 'Y'
		payment_request.MerMastDC.ErrorURL = 'http://127.0.0.1:8000/payment/unsuccessful_pmt/'
		payment_request.MerMastDC.ReturnURL = 'http://127.0.0.1:8000/payment/successful_pmt/'
	else:
		payment_request.MerMastDC.MerchantID = "1014"
		payment_request.MerMastDC.UserName = 'test'
		payment_request.MerMastDC.Password = "4l3S3T5gQvo%3d"
		payment_request.MerMastDC.AutoReturn = 'N'
		payment_request.MerMastDC.ErrorURL = 'http://127.0.0.1:8000/payment/unsuccessful_pmt/'
		payment_request.MerMastDC.ReturnURL = 'http://127.0.0.1:8000/payment/successful_pmt/'

	# Product Info
	mapping = {'CurrencyCode': kwargs.get('currency'), 'Quantity': kwargs.get('qty'),
			   'UnitPrice': kwargs.get('price'),
			   'TotalPrice': float(kwargs.get('qty')) * float(kwargs.get('price')),
			   'UnitName': 'Order %s'%(kwargs.get('order_id'))}

	product_dc = {k: v for k, v in mapping.items()}
	payment_request.lstProductDC.ProductDC.append(product_dc)

	response = client.service.PaymentRequest(payment_request)
	paymentUrl = "%s?ref=%s"%(response.TapPayURL, response.ReferenceID)
	return paymentUrl

def successful_pmt(request): 
	ref_id = request.GET.get('ref', '')
	result = request.GET.get('result', '')
	pay_id = request.GET.get('payid', '')
	cardType = request.GET.get('crdtype', '')
	""" 	these are some of the parameters that TAP's API returns 
				under the create payment return URL section			""" 
	return redirect('/')

def unsuccessful_pmt(request):
	return render(request, 'unsuccessful_payment.html', {}) #html not done yet

