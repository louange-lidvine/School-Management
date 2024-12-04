from django.shortcuts import render
from facilities.models import Facility, Booking
from events.models import Event
from members.models import Member
from django.db.models import Count
from datetime import datetime
import json

def dashboard(request):
    # Ensure user is authenticated
    if not request.user.is_authenticated:
        return render(request, 'login.html', {'error': 'Please log in to access the dashboard'})

    # Membership statistics for the logged-in user
    membership_data = Member.objects.filter(user=request.user).values('membership_type').annotate(count=Count('id')).values()
    for item in membership_data:
        item['join_date'] = item['join_date'].strftime('%Y-%m-%d')
    # Facility bookings for the logged-in user
    facility_data = Facility.objects.annotate(booking_count=Count('booking')).values()
    # Events associated with the logged-in user
    event_data = Event.objects.values('date__month').annotate(count=Count('id')).values()
    for item in event_data:
        item['date'] = item['date'].strftime('%Y-%m-%d')
    # Pass the filtered data to the context
    context = {
        'membership_data': json.dumps(list(membership_data)),  # Convert to list for JSON serialization
        'facility_data': json.dumps(list(facility_data)),      # Convert to list for JSON serialization
        'event_data': json.dumps(list(event_data)),            # Convert to list for JSON serialization
    }
    print(context)

    return render(request, 'dashboard.html', context)
     