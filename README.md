# YouTube Party

![YouTube Party](https://www.freepnglogos.com/uploads/youtube-logo-hd-8.png)

## Introduction
Have you ever wanted to connect with friends or family and watch youtube videos that isn't live streamed? Have you ever wanted a room with no distractions to study a Youtube Video with friends? Well Youtube Party is the place for you! With YouTube Party, anyone can create a room with a YouTube video, invite their friends, and chat about the video live!

## Inspiration
Our inspiration for this project was the current pandemic situation. Although some theaters are open, many of us are scared by the virus and try to stay at home as much as possible. However, when being stuck at home, you normally get very little social activity. This is our inspiration for YouTube Party - to connect people through what they love, watching YouTube.

## What it does
YouTube Party allows users to pick any video they want, create a live room for their peers to enter, and allow them to chat and share thoughts through realtime chat feature! 

## How we built it
YouTube Party was built using a Firebase database, Flask for web routing, SocketIO for realtime communication, and HTML, CSS, Bootstrap, and JavaScript for the frontend look and styles.

### Krishnan Shankar
I mainly worked on the backend of the project. I created the Flask routes to reference the HTML files, and coded the login functionality. I then connected the site to a Firebase database to store users and rooms. Finally, I implemented rooms and live chat using SocketIO!

### Joseph Attia
I worked on both the backend and the frontend. Implemented functionallity to the website and help create a connection with the backend to the the frontend. Additionally, I helped debug and fix errors that were in the app and helped it run smoother and faster! Finally, I helped style the website to make it more appealing and responsive!

### Rishav N.
I worked on the frontend of the website. I took care of setting up the HTML files, and linking them to the stylesheets. I also made custom styles for the site, to organize the elements and give it the YouTube feel!

## Challenges we ran into
One of the major challenges we ran into was setting up SocketIO. First, there were some issues with not being able to access the socket, which meant we needed to approve our domain to be used with SocketIO. And then, we had a lot of version compatibility issues, where the JavaScript SocketIO, Python SocketIO, and 

## Accomplishments that we're proud of
We're all very proud of the fact that we created such a big, multifunctional, realtime application in a short amount of time. We deci

## What we learned
Although we were comfortable using Flask, none of us had ever used SocketIO before, and we were dreding it. This project was our first time ever trying out SocketIO, and it was an amazing experience. After all the bugs were fixed, it was just so cool to watch the server update live!

## What's next for YouTube Party
In the future, we hope to implement realtime pause, play, and bookmark functionality to the app. We also hope to implement the limitation of anyone joining the room, meaning that the host has the ability to accept or deny accsess to the room through username broadcasting
