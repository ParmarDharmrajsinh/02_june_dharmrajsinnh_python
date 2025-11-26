from django.shortcuts import render


def index(request):
	"""Render a simple home page describing the project structure."""
	context = {
		'title': 'Simple Django Page',
		'message': 'Welcome — this is a minimal Django app showing project structure.'
	}
	return render(request, 'index.html', context)
