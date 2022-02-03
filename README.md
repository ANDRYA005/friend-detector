# The Friend Detector

## Goal

The main purpose of this project was to play around with some of the tools needed for developing a multi-service system. Specifically:
* **Service 1:** `telegram` was used to for interfacing with users
* **Service 2:** `django` and `djangorestframework` were used for processing and storing user data (`serializers` and `viewsets` were used to simplify the process). Two API endpoints were exposed (see more on this later).
* `docker` was used for containerising the services and `docker-compose` was used to make local testing easier
* `heroku` was used to deploy both services.


## Desired functionality

Here is a high-level overview of the desired functionality:
1. A Telegram bot (`@FriendDetectorBot`) receives a name from a user.
2. The name is stored in a database
3. When a person-detecting CNN identifies a person, it says "Hello \<name\>". (this is incomplete) 

## Technical walk-through / demo

After a user starts a conversation with the telegram bot, you can then `\stage` a name. This entails:
1. Sending a `POST` request to an API endpoint exposed by the django app.
2. If the django app successfully adds the name to the database, the telegram bot notifies the user that the name was staged.

![Alt Text](https://github.com/rs-anderson/friend-detector/blob/main/demo/stage.gif)

In order to validate whether the name has been staged, you can use `\get_staged`. This does the following:
1. Sends a `GET` request to an API endpoint exposed by the django app.
2. Retrieves the most recent name in the database.
3. Returns the name to the telegram bot, which then sends it back to the user. 

![Alt Text](https://github.com/rs-anderson/friend-detector/blob/main/demo/get_staged.gif)

The entire process is demonstrated again here for the name "Anderson".

![Alt Text](https://github.com/rs-anderson/friend-detector/blob/main/demo/stage_and_get_staged.gif)
