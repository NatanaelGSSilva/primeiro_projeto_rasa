# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import util

class ActionCidade(Action):

    def name(self) -> Text:
        return "action_cidade"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        print(tracker.latest_message['entities'])
        if tracker.latest_message['entities']:
            cep = tracker.latest_message['entities'][0]['value']
            cidade = util.getCep(cep)
            dispatcher.utter_message('cidade: {} '.format(cidade['localidade']))
        else:    
            dispatcher.utter_message(text="Sou um Boot por favor digite um cep certo por favor")

        

        return []
