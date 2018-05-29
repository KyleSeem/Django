Assignment: Disappearing Ninjas

Here is your product backlog:

1. Default page (‘localhost:8000’) should display a view that displays “No ninjas here.”

2. Visiting /ninjas should display all four Ninja Turtles (Leonardo, Michelangelo, Raphael, and Donatello)

3. Visiting /ninjas/[ninja_color] should display the corresponding Ninja Turtle
    * Used named groups to grab the color parameter out of the requested URL
    * I.e. visiting /ninjas/blue should only display Leonardo
    * /ninjas/orange => Michelangelo.
    * /ninjas/red => Raphael
    * /ninjas/purple => Donatello

4. If a user tries to hack into your web app by specifying a color or string combination other than the colors (blue, orange, red, and purple) that you’re anticipating, then display Megan Fox.

5. All of the ninjas/[ninja_color] paths should just be one route (not 5 separate routes…)
