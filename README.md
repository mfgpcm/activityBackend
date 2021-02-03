# Activity Online

This is a WebApp to play the activity board game online.
One player has to describe, to paint, or to act (pantomime) a given phrase and the other players have to find out what that should be within a predefined time.
Note that this WebApp does not enforce who's turn it is, nor does it count points or check for correct answers.
It merely serves to provide words and a Skype, Teams, Zoom, Jitsi or similar session is required to explain words, draw them on a shared whiteboard, and to act in from of a webcam.
 
Try it online at [activity-online.herokuapp.com](https://activity-online.herokuapp.com).

The WebApp is implemented using pyhton flask and flask-socketio.
It is published under GNU Affero General Public License Version 3.
Players can meet in individual rooms.
For each room, the app reads a CSV file with words and serves each requesting client a word, 
removing it from the list and sending a guess time to all the clients.
The word list can be reloaded on request.

## TODOs:
* Change the default word list to a more common one
* Allow users to upload own word lists
* Allow users to change default times
