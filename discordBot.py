import discord
from discord.ext import commands
import tensorflow as tf
from tensorflow import keras
import numpy as np
import pandas as pd
from kerasPredictions import *
from kerasPredictionsEveryone import *

from player import *
from game import *
from decks_and_cards import *
from presRound import *
from randomPlayer import *
from worstPlayer import *
from noTwoPlayer import *
from twoerPlayer import *
from personInputPlayer import *
from oldPlayer import *

client = commands.Bot(command_prefix=':')

@client.event
async def on_ready():
    print('ready')

@client.command(aliases=['make prediction', 'makeprediction', 'predict'])
async def makePrediction (ctx):
    # everyoneModel = keras.models.load_model('kerasModelEveryone')
    normalModel = keras.models.load_model('kerasModel')
    upperLowerModel = keras.models.load_model('kerasModelUpperLower')

    await ctx.send('Please tell me which type of prediction you want to see: (normal or upperlower)')

    typeOfModelMessage = await client.wait_for('message')
    answer = str(typeOfModelMessage.content)

    if answer == 'normal' or answer == 'upperlower':

        await ctx.send('Is the player starting? (0 for no, or 1 for yes)')

        startingMessage = await client.wait_for('message')
        isStarting = str(startingMessage.content)
        await ctx.send('''Please input the player's hand. (ei. "2,4,6,7,2,10,11,13,13,14,14,12,5")''')

        handMessage = await client.wait_for('message')
        hand = str(handMessage.content)

        if answer == 'normal':
            modelToUse = normalModel
            prediction = makeNormalPrediction(modelToUse, isStarting, hand)
            classes = {
                0: 'Pres',
                1: 'Vice-Pres',
                2: 'Vice-Ass',
                3: 'Ass',
            }
            predictionStr = classes[prediction]
        elif answer == 'upperlower':
            modelToUse = upperLowerModel
            prediction = makeNormalPrediction(modelToUse, isStarting, hand)
            classes = {
                0: 'Upper Class',
                1: 'Lower Class'
            }
            predictionStr = classes[prediction]

        await ctx.send('Here is the prediction:')
        await ctx.send(predictionStr)

client.run('token')
