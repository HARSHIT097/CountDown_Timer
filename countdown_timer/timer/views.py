# timer/views.py

from django.shortcuts import render
#from django.utils import timezone
#from datetime import datetime, timedelta, timezone as dt_timezone

"""
def countdown_view(request):
    # Set your target countdown time and make it timezone-aware
    target_time = datetime(2024, 12, 31, 23, 59, 59, tzinfo=dt_timezone.utc)

    # Calculate remaining time
    current_time = timezone.now()
    time_difference = target_time - current_time

    # Pass the remaining seconds to the frontend
    context = {
        'target_time': target_time,
        'remaining_seconds': int(time_difference.total_seconds())
    }
    return render(request, 'timer/index.html', context)

def countdown_view(request):
    # Set your target time as desired
    target_time = datetime(2024, 12, 31, 23, 59, 59, tzinfo=dt_timezone.utc)
    context = {
        'target_time': target_time,
    }
    return render(request, 'timer/index.html', context)
"""
def countdown_view(request):
    return render(request, 'timer/index.html')