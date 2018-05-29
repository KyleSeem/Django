Assignment: Survey Form

1. Build the wireframe (png provided) in a new Django project

2. Do not have a single URL handle BOTH the POST submission as well as render the view file.
    * the form that’s rendered should be submitted not to /result, but to /surveys/process.
    * The method that handles /surveys/process should do all the logic, process POST data, manipulate session data and redirect to another URL, say /result.
