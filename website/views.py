from django.shortcuts import render
#from django.core.mail import send_mail

def home(request):
	return render(request, 'home.html', {})

def contact(request):
	return render(request, 'contact.html', {})

def galeria(request):
	return render(request, 'galeria.html', {})

def pricing(request):
	return render(request, 'pricing.html', {})

def service(request):
	return render(request, 'service.html', {})
'''
	if request.method == "POST":
		#they are filling up the form
		message_name = request.POST ['message-name']
		message_email = request.POST [' message-email']
		message_phone  = request.POST ['message-phone']
		message = request.POST ['message']


		#send e-mail
		send_mail (
			message_name, #email subject
			message, #message
			message_email, #from email
			['helenacarolinasanchez@gmail.com'], #to email
			fail_silently = True
			)
	else:
		if they just want to look at the contacts (method = GET)
'''
	
