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
