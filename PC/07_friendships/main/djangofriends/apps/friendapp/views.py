from django.shortcuts import render
from . import models
# Create your views here.
def index(req):
    users = models.Users.objects.all()
    # rods = models.Users.objects.filter(last_name = 'Rodriguez')
    # notRods = models.Users.objects.exclude(last_name = 'Rodriguez')
    # q3 = models.Users.objects.filter(last_name='Rodriguez') | models.Users.objects.filter(first_name='Daniel')
    # q4 = models.Users.objects.filter(last_name='Rodriguez').exclude(first_name='Madison')
    # q5 = models.Users.objects.exclude(first_name='Daniel').exclude(first_name='Michael')
    # q6 = models.Users.objects.get(id=1)
    # q7 = models.Users.objects.get(last_name='Rodriguez') # returns error due to multiple objects returned
    # q8 = models.Users.objects.get(id=10000) # returns error as id does not exist
    # q9 = models.Users.objects.all().order_by('first_name')
    # q10 = models.Users.objects.all().order_by('-last_name')
    # q11 = models.Friendships.objects.all()# print all Friendship objects in terminal
    # q12 = models.Friendships.objects.filter(user=4)
    # q13 = models.Friendships.objects.filter(friend=4)
    q14 = models.Friendships.objects.exclude(user=4).exclude(user=5).exclude(user=6)

    print('*'*80)
    # print(q12.query)
    print('*'*80)
    context = {
        'users':users,
        # 'users':rods, 
        # 'users':notRods,
        # 'users':q3,
        # 'users':q4,
        # 'users':q5,
        # 'qstn':q6,
        # 'qstn':q7,
        # 'qstn':q8,
        # 'users':q9,
        # 'users':q10,
        # 'friendships':q11,
        # 'friendships':q12,
        # 'friendships':q13,
        'friendships':q14,
    }
    return render(req, "friendapp/index.html",context)

def part2(request):
    # q1 = models.Friendships.objects.all()
    # q2 = models.Friendships.objects.filter(user__first_name='Michael')
    # q3 = models.Friendships.objects.exclude(user__first_name='Daniel')
    # q4 = models.Friendships.objects.filter(user__id=1) | models.Friendships.objects.filter(user__last_name='Hernandez')
    # q5 = models.Friendships.objects.filter(user__id=1).order_by('friend__first_name') | models.Friendships.objects.filter(user__last_name='Hernandez')
        # made several attempts to solve question 5 (using .distinct()), but even after reading django documentation and forum searches, i was unable to resolve in a reasonable amount of time - will try to return at a later date
    # q6 = users statement below
    # users = models.Users.objects.filter(usersfriend__friend__id=2)
    # q7 = completed on part2.html page
    # users = models.Users.objects.filter(usersfriend__friend__id=1)
    # users = models.Users.objects.filter(friendsfriend__friend__id=1)
    users = models.Users.objects.filter(friendsfriend__friend__id=1) | models.Users.objects.filter(friendsfriend__friend__last_name='Hernandez')


    print('*'*80)
    print(users.query)
    print('*'*80)

    context = {
        # 'friendships':q1,
        # 'friendships':q2,
        # 'friendships':q3,
        # 'friendships':q4,
        # 'friendships':q5,
        'users':users,
    }
    return render(request, "friendapp/part2.html", context)
