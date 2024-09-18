
from django.shortcuts import render, redirect,get_object_or_404
from .models import Flight
from .forms import FlightForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import authenticate, login as auth_login

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # Use Django's built-in authentication
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # Check if the user is a superuser
            if user.is_superuser:
                # Log the user in
                auth_login(request, user)
                # Redirect to the admin dashboard
                return redirect('admin_dashboard')
            else:
                # Show error if the user is not a superuser
                return render(request, 'account/login.html', {'error': 'You are not authorized to access this page'})
        else:
            # Show error if credentials are invalid
            return render(request, 'account/login.html', {'error': 'Invalid credentials'})

    return render(request, 'account/login.html')

def admin_dashboard(request):
    # Ensure the user is authenticated and is a superuser
    if not request.user.is_authenticated or not request.user.is_superuser:
        return redirect('login')

    return render(request, 'account/admin_dashboard.html')

# View to list all flights
def flight_list(request):
    flights = Flight.objects.all()
    return render(request, 'account/flight_list.html', {'flights': flights})

# View to search flight by ID
def flight_search(request):
    if request.method == 'POST':
        flight_id = request.POST['flight_id']
        flight = Flight.objects.filter(flight_id=flight_id).first()
        return render(request, 'account/flight_search.html', {'flight': flight})
    return render(request, 'account/flight_search.html')

# View to add a new flight
def flight_add(request):
    if request.method == 'POST':
        form = FlightForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('flight_list')
    else:
        form = FlightForm()
    return render(request, 'account/flight_add.html', {'form': form})

# View to edit/update flight details
def flight_edit(request, pk):
    flight = get_object_or_404(Flight, pk=pk)
    if request.method == 'POST':
        form = FlightForm(request.POST, instance=flight)
        if form.is_valid():
            form.save()
            return redirect('flight_list')
    else:
        form = FlightForm(instance=flight)
    return render(request, 'account/flight_edit.html', {'form': form})
def logout(request):
    # Clear the session data
    request.session.flush()
    return redirect('login')

