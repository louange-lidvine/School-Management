from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Facility, Booking
from .forms import FacilityForm, BookingForm

def facility_list(request):
    facilities = Facility.objects.all()
    return render(request, 'facilities/facility_list.html', {'facilities': facilities})

# def facility_detail(request, facility_id):
#     facility = get_object_or_404(Facility, id=facility_id)
#     return render(request, 'facilities/book_facility.html', {'facility': facility})

@login_required
def facility_booking(request, facility_id):
    facility = get_object_or_404(Facility, id=facility_id)
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.facility = facility
            booking.member = request.user.member
            booking.save()
            # Redirect to the facility list or any other appropriate page after booking
            return redirect('facility_list')  # or 'facility_booking', facility_id=facility.id if rebooking
    else:
        form = BookingForm()
    return render(request, 'facilities/facility_booking.html', {'facility': facility, 'form': form})


@login_required
def book_facility(request, facility_id):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            book = form.save(commit=False)
            book.facility_id = facility_id  # Associate with the facility if needed
            book.save()
            return redirect('facility_list',facility_id=facility.id)  # or specify where to redirect after booking
    else:
        form = BookingForm()
    return render(request, 'facilities/book_facility.html', {'form': form})

@login_required
def create_facility(request):
    if request.method == 'POST':
        form = FacilityForm(request.POST)
        if form.is_valid():
            facility = form.save()
            return redirect('facility_booking', facility_id=facility.id)
    else:
        form = FacilityForm()
    
    # Ensure you always return an HttpResponse
    return render(request, 'facilities/facility_booking.html', {'form': form})

from django.shortcuts import render, get_object_or_404, redirect
from .models import Facility
from .forms import FacilityForm
from django.contrib.auth.decorators import login_required

@login_required
def update_facility(request, facility_id):
    facility = get_object_or_404(Facility, id=facility_id)
    if request.method == 'POST':
        form = FacilityForm(request.POST, instance=facility)
        if form.is_valid():
            form.save()
            return redirect('facility_list')  # Redirect to the facility list after update
    else:
        form = FacilityForm(instance=facility)
    return render(request, 'facilities/update_facility.html', {'form': form, 'facility': facility})

@login_required
def delete_facility(request, facility_id):
    facility = get_object_or_404(Facility, id=facility_id)
    if request.method == 'POST':
        facility.delete()
        return redirect('facility_list')  # Redirect to the facility list after deletion
    return render(request, 'facilities/delete_facility.html', {'facility': facility})
