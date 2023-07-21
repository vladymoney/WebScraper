# ScrapeApp/views.py

import requests
from django.shortcuts import render
from django.http import HttpResponse
from .forms import URLForm

def index(request):
    if request.method == 'POST':
        form = URLForm(request.POST)
        if form.is_valid():
            url = form.cleaned_data['url']
            try:
                response = requests.get(url)
                response.raise_for_status()  # Check if the request was successful

                # Save the source code to an HTML file
                filename = 'source_code.html'
                with open(filename, 'w', encoding='utf-8') as htmlfile:
                    htmlfile.write(response.text)

                # Prepare the HTML file for download
                with open(filename, 'rb') as htmlfile:
                    response = HttpResponse(htmlfile.read(), content_type='text/html')
                    response['Content-Disposition'] = 'attachment; filename="' + filename + '"'

                # Delete the temporary HTML file
                import os
                os.remove(filename)

                return response
            except requests.exceptions.HTTPError:
                error_message = "Error: Could not fetch data from the provided URL."
                return render(request, 'index.html', {'form': form, 'error_message': error_message})

    else:
        form = URLForm()

    return render(request, 'index.html', {'form': form})
