from django.shortcuts import render
# from quickdraw import QuickDrawData

# qd = QuickDrawData()
# qd.get_name
# Create your views here.
def game(request):
    return render(request,'game/active_game.html')