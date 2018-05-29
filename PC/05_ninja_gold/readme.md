Assignment: Ninja Gold (Django Version)
You’re going to create a mini-game that helps a ninja make some money!

When you start the game, your ninja should have 0 gold. The ninja can go to different places (farm, cave, house, casino) and earn different amounts of gold. In the case of a casino, your ninja can earn or lose up to 50 golds. Your job is to create a web app that allows this ninja to earn gold and to display past activities of this ninja.

Refer to the wireframe below.
Have the four forms appear when the user goes to http://localhost
For the farm, for example, your form would look something like:
  <form action="/process_money" method="post">
    <input type="hidden" name="building" value="farm" />
    <input type="submit" value="Find Gold!"/>
  </form>
In other words, use a hidden input tag value in the form to pass the relevant location to the server
Have /process_money determine how much gold the user should have (hint: you’ll have to set up a custom routing rule)
For this assignment, we’re not using a database. Just save the activity logs in session
Bonus
Refactor your code to remove the hidden input and instead use a route parameter
