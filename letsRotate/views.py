from django.shortcuts import render, redirect
import rotatescreen
import time

rotation = 0


def hey_you(request):
    global rotation
    if request.method == "POST":
        rotation += 90
        if rotation == 360:
            rotation = 0
        screen = rotatescreen.get_primary_display()

        for i in range(21):
            time.sleep(0.4)
            screen.rotate_to(i*90%360)

    return render(request, 'home.html')
