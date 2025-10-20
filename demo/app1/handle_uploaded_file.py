def handle_uploaded_file(f):
    with open('./formresponses/response.txt', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)