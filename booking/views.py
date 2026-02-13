

# Create your views here.
from django.shortcuts import render, redirect
from .models import Game, Booking, Contact

def home(request):
    games = Game.objects.all()

    if request.method == "POST":
        player_name = request.POST.get("player_name")
        game_id = request.POST.get("game")
        date = request.POST.get("date")
        time_slot = request.POST.get("time_slot")

        game = Game.objects.get(id=game_id)

        Booking.objects.create(
            player_name=player_name,
            game=game,
            date=date,
            time_slot=time_slot
        )
        return redirect('home')

    return render(request, "home.html", {"games": games})



def home(request):
    games = Game.objects.all()

    if request.method == "POST":
        # Booking Form
        if "player_name" in request.POST:
            player_name = request.POST.get("player_name")
            game_id = request.POST.get("game")
            date = request.POST.get("date")
            time_slot = request.POST.get("time_slot")

            game = Game.objects.get(id=game_id)

            Booking.objects.create(
                player_name=player_name,
                game=game,
                date=date,
                time_slot=time_slot
            )

        # Contact Form
        elif "contact_name" in request.POST:
            name = request.POST.get("contact_name")
            email = request.POST.get("contact_email")
            message = request.POST.get("contact_message")

            Contact.objects.create(
                name=name,
                email=email,
                message=message
            )

    return render(request, "home.html", {"games": games})
