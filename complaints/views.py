from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Complaint
from .forms import ComplaintForm
from django.http import HttpResponseForbidden

@login_required
def create_complaint(request):
    if request.method == 'POST':
        form = ComplaintForm(request.POST)
        if form.is_valid():
            complaint = form.save(commit=False)
            complaint.created_by = request.user
            complaint.save()
            return redirect('my_complaints')
    else:
        form = ComplaintForm()

    return render(request, 'complaints/create_complaint.html', {'form': form})


@login_required
def my_complaints(request):
    complaints = Complaint.objects.filter(created_by=request.user)
    return render(request, 'complaints/my_complaints.html', {'complaints': complaints})


@login_required
def all_complaints(request):
    if request.user.profile.role != 'ADMIN':
        return HttpResponseForbidden("You are not authorized to view this page.")

    complaints = Complaint.objects.all()
    return render(request, 'complaints/all_complaints.html', {'complaints': complaints})


@login_required
def update_status(request, complaint_id):
    if request.user.profile.role != 'ADMIN':
        return HttpResponseForbidden("You are not authorized to update complaints.")

    complaint = Complaint.objects.get(id=complaint_id)

    if request.method == 'POST':
        new_status = request.POST.get('status')
        complaint.status = new_status
        complaint.save()
        return redirect('all_complaints')

    return render(request, 'complaints/update_status.html', {'complaint': complaint})
