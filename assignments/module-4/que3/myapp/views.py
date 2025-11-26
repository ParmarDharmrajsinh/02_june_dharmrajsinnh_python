from django.shortcuts import render

# Create your views here.
def index(request):
    success_message = None
    if request.method == 'POST':
        # Minimal server-side acceptance (client-side JS does validation)
        name = request.POST.get('name', '').strip()
        email = request.POST.get('email', '').strip()
        # In a real app you'd save the patient to the database here
        if name and email:
            success_message = f"Registration successful for {name}."

    return render(request, 'index.html', {'success_message': success_message})