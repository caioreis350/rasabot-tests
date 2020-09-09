# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List, Union
#
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
from rasa_sdk.forms import FormAction
import requests
#
#


class AgendaForm(FormAction):

    def name(self):
        return "agenda_form"

    @staticmethod
    def required_slots(tracker):
        return ["agenda"]

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        return {"agenda": self.from_text(intent="escolher_dia_hora")}

    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:

        dispatcher.utter_message(f"Beleza, Você agendou")
        return []


class ActionAskRobot(Action):
    def name(self) -> Text:
        return "action_ask_agenda"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        message = "Which of these hours should me choose for you?"
        results = ["Dia 20-10-2020 Horário 10:00-11:00hrs",
                   "Dia 25-10-2020 Horário 11:00-12:00hrs",
                   "Dia 30-10-2020 Horário 14:00-15:00hrs"]

        buttons = [{"title": results[0], "payload":results[0]},
                   {"title": results[1], "payload":results[1]},
                   {"title": results[2], "payload":results[2]}]

        dispatcher.utter_message(text=message, buttons=buttons)

        return []


class ActionBuscarDiaHora(Action):
    def name(self):
        return "action_buscar_diahora"

    def run(self, dispatcher, tracker, domain):
        message = "Which of these hours should me choose for you?"
        agenda = ["Dia 20-10-2020 Horário 10:00-11:00hrs",
                  "Dia 25-10-2020 Horário 11:00-12:00hrs",
                  "Dia 30-10-2020 Horário 14:00-15:00hrs"]
        escolha_um = agenda[0]
        escolha_dois = agenda[1]
        escolha_tres = agenda[2]

        return [SlotSet("escolha_um", escolha_um), SlotSet("escolha_dois", escolha_dois), SlotSet("escolha_tres", escolha_tres)]


class ActionSalvaEscolha(Action):
    def name(self):
        return "action_salva_escolha"

    def run(self, dispatcher, tracker, domain):
        agenda_escolhida = tracker.latest_message['text']
        print(agenda_escolhida)
        return [SlotSet("agenda", agenda_escolhida)]
