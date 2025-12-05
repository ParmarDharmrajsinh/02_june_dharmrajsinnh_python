from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect

User = get_user_model()

# Admin credentials
ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "admin123"

def alogin(request):
    error = ""
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
            return redirect("dashboard")
        else:
            error = "Invalid username or password"
    return render(request, "alogin.html", {"error": error})

def dashboard(request):
    users = User.objects.all()
    return render(request, "dashboard.html", {"users": users})

def admin_dashboard_redirect(request):
    """Redirect /adminapp to /admin_dashboard/"""
    return redirect("admin_dashboard")

def author_required(view_func):
    def wrapper(request, *args, **kwargs):
        if not hasattr(request.user, 'role') or request.user.role not in ['author', 'admin']:
            return redirect("no-access")
        return view_func(request, *args, **kwargs)
    return wrapper
