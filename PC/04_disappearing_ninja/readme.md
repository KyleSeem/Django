Assignment: Disappearing Ninjas

This exercise will help you practice using URLs to render templates and static content.

Here is your product backlog:

Default page (‘localhost:8000’) should display a view that displays “No ninjas here.”
Visiting /ninjas should display all four Ninja Turtles (Leonardo, Michelangelo, Raphael, and Donatello)
Visiting /ninjas/[ninja_color] should display the corresponding Ninja Turtle
Used named groups to grab the color parameter out of the requested URL
I.e. visiting /ninjas/blue should only display Leonardo
/ninjas/orange => Michelangelo.
/ninjas/red => Raphael
/ninjas/purple => Donatello
If a user tries to hack into your web app by specifying a color or string combination other than the colors (blue, orange, red, and purple) that you’re anticipating, then display Megan Fox.
All of the ninjas/[ninja_color] paths should just be one route (not 5 separate routes…)
