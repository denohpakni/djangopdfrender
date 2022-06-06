[How to Render and Open PDF file in Django](https://www.csestack.org/render-open-pdf-file-django/)

## Steps
1. Create project and app.
2. Join the `urls`
3. Create the views

        from django.http import FileResponse
        import os
        
        def show_pdf(request):
            filepath = os.path.join('static', 'sample.pdf')
            return FileResponse(open(filepath, 'rb'), content_type='application/pdf'

This works well.
