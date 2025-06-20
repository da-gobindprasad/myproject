
# Create your views here.
from django.shortcuts import render

def home(request):
    return render(request, 'main/home.html')

def service_home_cleaning(request):
    return render(request, 'main/service_home_cleaning.html')

def booking_availability(request):
    return render(request, 'main/booking_availability.html')

def property_details(request):
    if request.method == 'POST':
        floors = int(request.POST.get('floors', 1))
        rooms = int(request.POST.get('rooms', 4))
        bedrooms = int(request.POST.get('bedrooms', 4))
        toilets = int(request.POST.get('toilets', 3))
        ovens = int(request.POST.get('ovens', 1))
        doors = int(request.POST.get('doors', 1))

        base_cost = 100
        extras = (
            max(floors - 1, 0) +
            max(rooms - 4, 0) +
            max(bedrooms - 4, 0) +
            max(toilets - 3, 0) +
            max(ovens - 1, 0) +
            max(doors - 1, 0)
        )

        final_amount = base_cost + (extras * 5)

        # ✅ Save calculated amount to session
        request.session['final_amount'] = round(final_amount, 2)

        # ✅ Redirect to the client payment page
        return redirect('client_payment')

    return render(request, 'main/property_details.html')

from django.shortcuts import render, redirect

def client_payment(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        payment_option = request.POST.get('payment_option')
        final_amount = request.POST.get('final_amount')

        try:
            final_amount = float(final_amount)
        except (TypeError, ValueError):
            final_amount = 100.00

        # Save booking details only on POST
        booking_data = {
            'name': name,
            'email': email,
            'phone': phone,
            'address': address,
            'payment_option': payment_option,
            'final_amount': round(final_amount, 2),
        }

        request.session['booking'] = booking_data
        request.session['booking_complete'] = True  # Flag that payment step completed

        return redirect('booking_confirm')

    # If user tries to access GET directly, ensure flow integrity
    if not request.session.get('final_amount'):
        return redirect('select_property')  # Must come from property page

    # Do not show old booking details on GET
    request.session.pop('booking', None)
    request.session['booking_complete'] = False

    total = request.session.get('final_amount', 100.00)
    return render(request, 'main/client_payment.html', {'total': total})


def booking_confirm(request):
    if not request.session.get('booking_complete'):
        return redirect('client_payment')  # Prevent direct access

    booking = request.session.get('booking')

    if not booking:
        return redirect('client_payment')  # Also block if data missing

    # Optional: Clear session after confirmation
    request.session.pop('booking_complete', None)
    request.session.pop('booking', None)
    request.session.pop('final_amount', None)

    return render(request, 'main/booking_confirm.html', {'booking': booking})
