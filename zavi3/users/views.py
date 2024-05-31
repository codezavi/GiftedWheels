from django.shortcuts import render
from .models import Profile
# Create your views here.
def profiles(request):
    profiles=Profile.objects.all()
    context={'profiles':profiles}
    return render(request, 'users/profiles.html', context)


def userProfile(request, pk):
    profile = Profile.objects.get(id=pk)

    topSkills = profile.skill_set.exclude(description__exact="")
    otherSkills = profile.skill_set.filter(description="")  # Corrected variable name

    context = {'profile': profile, 'topSkills': topSkills, 'otherSkills': otherSkills}  # Corrected variable name
    return render(request, 'users/user.profile.html', context)