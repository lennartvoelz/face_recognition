This is a more complex project where i work on implementing a face recognition web app on my website.
The user can upload a picture and his/her name to be recognized by the web app via the camera.

Done:
- simple website is set up in html/css/js and hosted: https://database-dc7f0.web.app/
- input at https://database-dc7f0.web.app/project.html is streamed to storage and realtime database firebase using JavaScript
- files from the real-time database are retrieved with the Python library requests and stored in easily accessible pandas dataframe
- opencv is used to process the images
- git ignore file added to not store data in public github repo

Planned:
- implementation of recognition system in browser using flask
- use cloud services to not have to run server locally
