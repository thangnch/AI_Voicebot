# Imports
#-----------
# rasa core
import logging
import rasa_core
from rasa_core import training
from rasa_core.actions import Action
from rasa_core.agent import Agent
from rasa_core.domain import Domain
from rasa_core.policies.keras_policy import KerasPolicy
from rasa_core.policies.memoization import MemoizationPolicy
from rasa_core.featurizers import MaxHistoryTrackerFeaturizer, BinarySingleStateFeaturizer
#from rasa_core.channels.console import ConsoleInputChannel
from rasa_core.interpreter import RegexInterpreter
from rasa_core.utils import EndpointConfig
from rasa_core.interpreter import RasaNLUInterpreter
import json
from rasa_core import utils, train, run

from rasa_core.training import interactive



def run_dialogue(serve_forever=True):
    interpreter = RasaNLUInterpreter('./models/nlu/default/chat')
    action_endpoint = EndpointConfig(url="http://localhost:5055/webhook")
    agent = Agent.load('./models/dialogue', interpreter=interpreter, action_endpoint=action_endpoint)
    rasa_core.run.serve_application(agent, channel='cmdline')
    return agent

def run_online_dialogue(serve_forever=True):
    interpreter = RasaNLUInterpreter('./models/nlu/default/chat')
    action_endpoint = EndpointConfig(url="http://localhost:5055/webhook")
    agent = Agent.load('./models/dialogue', interpreter=interpreter, action_endpoint=action_endpoint)
    interactive.run_interactive_learning(agent)#, channel='cmdline')
    return agent

run_dialogue()