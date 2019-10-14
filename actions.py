# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message("Hello World!")
#
#         return []

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

from weather import Weather, Unit

class ActionGetWeather(Action):

    def name(self):
        return 'action_get_weather' 
    
    def run(self, dispatcher, tracker, domain):
        weather = Weather(unit = Unit.CELSIUS)
        gpe = ('Auckland', tracker.get_slot('GPE'))[bool(tracker.get_slot('GPE'))]
        result = weather.lookup_by_location(gpe)

        if result:
            condition = result.condition
            city = result.location.city
            country = result.location.country
            dispatcher.utter_message('It is' + condition.text + 'and' + condition.temp + '°C in' + city + ', ' + country + '.')
        
        else:
            dispatcher.utter_message('I could not find any weather information for' + gpe + '\nTry searching by a city name. ')
            
        return         
