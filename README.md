# Setup / Configuration Instructions

## Setup GitHub SSH key to Virtual Machine
https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent

https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account

Before git clone the project repo, make sure the github ssh key is already set up on the virtual machine. The steps on how to do so are mentioned in the link above.

## Initial Setup
---

1. Git clone the repo for FeedMe project

   `$ git clone git@github.com:Inri5x5/FeedMe.git FeedMe`

2. Go to FeedMe directory

   `$ cd FeedMe`

3. Install the required libraries for python

   `$ pip3 install -r requirements.txt`

4. Open a new terminal and change to FeedMe frontend directory
   
   `$ cd FeedMe/frontend`

5. Install the required libraries for React 

    `$ npm install`


Note: Having python3 on version 3.6 or above and NodeJs on version 8.5.0 is required to run the project.


## Running the project

---

1. Go to FeedMe backend directory
   
   `$ cd FeedMe/backend`

2. On FeedMe backend directory run
   
   `$ python3 app.py`

3. On FeedMe frontend directory run
   
   `$ npm start`

After running npm start, the default web browser will pop-up with the website running.

The project will usually run on http://localhost/3000 and backend will run on http://localhost/5000 but if there is another website running on the same port there will be an alert:

Press ‘Y’ and it will automatically run on any available port and also default browser will pop-up
