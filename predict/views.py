from django.shortcuts import render
from django.http.response import StreamingHttpResponse
from django.http import JsonResponse, HttpResponse
from predict.preview import VideoCamera, Model
from django.contrib.auth.decorators import login_required

image = None
model = Model()


def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def pre(request):
    return render(request, 'preview.html')


def output(request):
    if request.is_ajax():
        result = Model()
        return render(request, 'predict.html', {'output': result.predict()})


def gen_preview(camera):
    while True:
        global image
        image = camera.get_image()
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')


def preview(request):
    return StreamingHttpResponse(gen_preview(VideoCamera()), content_type='multipart/x-mixed-replace; boundary=frame')


def predict(request):
    return HttpResponse(model.predict(image))


def service(request):
    return render(request, 'service.html')


def team(request):
    name = ["Zeeshan Siddique", "Abdul Rehman",
            "Olivia Bell", "Amanda Jepson"]
    position = ["Software Developer"]*4
    description = ["I am a self motivated software developer."]*4
    image = ["assets/img/team/team1.jpeg", 'assets/img/team/team-3.jpg',
             'assets/img/team/team-2.jpg', 'assets/img/team/team-4.jpg']
    detail = zip(name, position, description, image)
    return render(request, 'team.html', {'detail': detail})


def cam_front(request):
    return render(request, 'cam_prev.html')
