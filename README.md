Finished Development: 01/04/2023

First 3 Years of Programming

# Summary
This was an application I made for my YouTube channel. At the time is really annoying to record me doing coding tutorials.
The typing from the keyboard would sometimes be picked up by the microphone, which did not sound professional. The other
big issue was that I made typing mistakes. So I would have to rerecord a segment if I said something wrong or if I made
a typing mistake. The hardest part of the typing mistakes is that I would sometimes not catch them until after I wrote
all the tutorial code. That meant I would have two options: rerecord the segment where that code is visible, or have a 
disclaimer at the end of the segment (or after I typed the mistake) that I made a mistake. With these problems in mind, 
I developed an automatic "typer." I could write the text from the template file to another file that was shown being typed
for the tutorial. If I did this writing at a slow, but constant rate, it would look like I was typing the file. Not a lot
of editors supported this kind of functionality because they only read the file from memory once when it was opened, not 
constantly. Thankfully, VS Code accomplished what I wanted. I could type stop characters: '&' into the file, so the program 
would stop typing until I told it to continue typing again. The stop characters allowed me to give some explanation for a
bit before I continued "typing."

# Running the Program
Run the 'main.py' file from the root directory of this project. The application's start screen allows you to select two 
files: the file that is being written to and the template file. Once those are selected, you can click the button that says 
'Start' at the bottom of the screen. This will open up the screen and start the automatic typer. Make sure you click on 
VS Code to 'focus' on the application. Otherwise, you may not see the typing. Once the automatic typer sees a '&' the 
typer will stop. Once you want it to continue typing, you can click on the 'Continue' button. Or you can click on the 
'Reset' button to play that section again. You can also click on the 'Go Back' button to go back to the first screen.

# Revisions 11/30/2023
I changed some of the file paths to work for more machines (not just my old linux machine). I also added an ability to 
change the stop character (which is pretty important). I also added some additional constants that can be controlled in 
the configuration files.