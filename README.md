# Presidents-Keras-Tensorflow-Predictions
Models that have examined data about hands from the presidents and assholes game in order to make predictions about specific hands. This repo also contains a discord bot so that you can make predictions on hands on your server.

# How to use the models:
In the "discordBot.py" file, at the bottom, is a place for an API key. Put your discord bot API key there. Then invite your bot to whatever server you want it on and run discordBot.py.
This repository already contains models that have examined enough data to make accurate predictions, so there is no need to train your own models, however, that code is in here as well.

Commands:
:predict - this is the main command that starts a chain of asking you what you want to do predictions on.
The bot will ask you which type of prediction you want. "Normal" just predicts the class of the given hand and "UpperLower" predicts whether the hand will be upperclass or lowerclass.
The bot will then ask you for a hand. Input the hand you want and wait for the prediction!
