Assignment: Friendships - Welcome to the ORM

PART 1
Load up
  (djangoenv)yourassignmentfolder> git clone https://github.com/MikeHannon/djangofriends.git

Filter
  1. Using models.Users.objects.filter(model_key=something). Filter all of the users such that we only get back users with the last_name of Rodriguez.

Exclude
  2. Using models.Users.objects.exclude(model_key=something). Filter all of the users such that we have all of the users except people with the last_name Rodriguez.

Let’s Practice Chaining
  3. Using filter, get all of the users with the last_name Rodriguez and all of the users with the first_name Daniel.
  4. Let’s get all of the Rodriquez’s except Madison.
  5. Let’s get everyone except Daniel and Michael.

Using get versus filter
  6. Try models.Users.objects.get(id=1). Have this users first_name and last_name print on the index.html.
  7. Try models.Users.objects.get(last_name=‘Rodriquez’).
  8. Try models.Users.objects.get(id=10000).  

Let’s explore a bit:
  9. Order the users by first_name.
  10. Order the users by reverse last_name.
  11. Print all the Friendship objects in your terminal.
  12. You know how to get a single friend by the id (#6), now retrieve the Friendships where the User at id 4 is the user in the friendships table! (hint: filter(user = …))
  13. Retrieve the Friendships where the User at id is 4 is the friend.
  14. Retrieve the Friendships where the user isn’t user 4, 5, or 6. So exclusive…

PART 2
* created part2.html in lieu of index.html for this section to easily differentiate assignments while maintaining all answers to questions.

1. Starting with Friendships, show all of the user and friend first and last names on your index.html page.
2. Print all of the friend’s first and last names associated with user__first_name = ‘Michael’ on your index.html page.
3. Print all of the friend’s first names who Daniel is not friends with on your index.html page.
4. Print all of the friend’s who are friends with both User with the id of 1 and with Users with the last name Hernandez.
5. Order these by friend first_name and print them on your index.html page.
6. In your views.py, try the following query:
    users = models.Users.objects.filter(usersfriend__friend__id=2)
    print (users.query)
    #don't forget to pass users in to the context dictionary!
7. Given this query, on your HTML page, try to print out the first and last name of Users with the id 2. 
8. Now that we can use related names to filter, let’s go back and try to get #4 but start with the Users!
