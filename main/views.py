
# Create your views here.
from django.shortcuts import render

def home(request):
    return render(request, 'main/home.html')

def service_home_cleaning(request):
    return render(request, 'main/service_home_cleaning.html')

def booking_availability(request):
    return render(request, 'main/booking_availability.html')

def property_details(request):
    # if request.method == 'POST':
    #     floors = int(request.POST.get('floors', 1))
    #     rooms = int(request.POST.get('rooms', 4))
    #     bedrooms = int(request.POST.get('bedrooms', 4))
    #     toilets = int(request.POST.get('toilets', 3))
    #     ovens = int(request.POST.get('ovens', 1))
    #     doors = int(request.POST.get('doors', 1))

    #     base_cost = 100
    #     extras = (
    #         max(floors - 1, 0) +
    #         max(rooms - 4, 0) +
    #         max(bedrooms - 4, 0) +
    #         max(toilets - 3, 0) +
    #         max(ovens - 1, 0) +
    #         max(doors - 1, 0)
    #     )

    #     final_amount = base_cost + (extras * 5)

    #     # ✅ Save calculated amount to session
    #     request.session['final_amount'] = round(final_amount, 2)

    #     # ✅ Redirect to the client payment page
    #     return redirect('client_payment')

    return render(request, 'main/property_details.html')

from django.shortcuts import render, redirect


def client_payment(request):
    return render(request, 'main/client_payment.html')

def booking_confirm(request):
    if not request.session.get('booking_complete'):
        return redirect('client_payment')  # Prevent direct access

    booking = request.session.get('booking')

def booking_confirm(request):
    return render(request, 'main/booking_confirm.html')  # Create this templa

    # Optional: Clear session after confirmation
    request.session.pop('booking_complete', None)
    request.session.pop('booking', None)
    request.session.pop('final_amount', None)

    return render(request, 'main/booking_confirm.html', {'booking': booking})

from django.shortcuts import render

def services(request):
    services = [
        {'title': 'House Cleaning', 'description': 'Routine and deep cleaning for homes.', 'icon': '🏠', 'image': 'main/images/service1.png'},
        {'title': 'Office Cleaning', 'description': 'Professional cleaning for workspaces.', 'icon': '🏢', 'image': 'main/images/service2.png'},
        {'title': 'End of Tenancy', 'description': 'Move-out full cleaning.', 'icon': '🔁', 'image': 'main/images/service3.png'},
        {'title': 'Carpet Cleaning', 'description': 'Steam and stain removal for carpets.', 'icon': '🧼', 'image': 'main/images/service4.png'},
        {'title': 'Window Cleaning', 'description': 'Streak-free window washing.', 'icon': '🪟', 'image': 'main/images/service5.png'},
        {'title': 'After Party Cleaning', 'description': 'Post-event full clean-up.', 'icon': '🎉', 'image': 'main/images/service6.png'},
        {'title': 'Sofa Cleaning', 'description': 'Cleaning fabric and leather sofas.', 'icon': '🛋️', 'image': 'main/images/service1.png'},
        {'title': 'Kitchen Deep Clean', 'description': 'Degreasing appliances & counters.', 'icon': '🍳', 'image': 'main/images/service2.png'},
        {'title': 'Bathroom Sanitization', 'description': 'Disinfection of all bathroom surfaces.', 'icon': '🛁', 'image': 'main/images/service3.png'},
        {'title': 'Curtain Cleaning', 'description': 'Steam/dry cleaning of curtains.', 'icon': '🎭', 'image': 'main/images/service4.png'},
        {'title': 'Mattress Cleaning', 'description': 'Dust mite & stain removal.', 'icon': '🛏️', 'image': 'main/images/service5.png'},
        {'title': 'Balcony & Terrace', 'description': 'Cleaning garden and terrace areas.', 'icon': '🌿', 'image': 'main/images/service6.png'},
        {'title': 'Commercial Deep Clean', 'description': 'Heavy-duty commercial space cleaning.', 'icon': '🏬', 'image': 'main/images/service1.png'},
        {'title': 'Post-Renovation Cleaning', 'description': 'Clean-up after construction.', 'icon': '🚧', 'image': 'main/images/service2.png'},
        {'title': 'Move-In Cleaning', 'description': 'Pre-move deep cleaning.', 'icon': '📦', 'image': 'main/images/service3.png'},
        {'title': 'Fridge & Appliance', 'description': 'Cleaning kitchen equipment.', 'icon': '🧊', 'image': 'main/images/service4.png'},
    ]
    return render(request, 'main/services.html', {'services': services})

def about(request):
    return render(request, 'main/about.html')


from django.shortcuts import render
from django.contrib import messages

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        
        # For now, just show a success message
        messages.success(request, "Thank you for contacting us! We’ll get back to you shortly.")
        
        # You can later handle sending email here
        return render(request, 'main/contact.html', {'submitted': True})
    
    return render(request, 'main/contact.html')
