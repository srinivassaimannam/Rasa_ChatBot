from typing import Any, Text, Dict, List, Union
from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet, SessionStarted, ActionExecuted, EventType
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import UserUtteranceReverted
from rasa_sdk.forms import FormAction
import random
import pymysql


pick_up=str()
destination=str()
book_id=int()
mobile = str()

db=pymysql.connect(host="database-1.ciz6hepwqan2.us-east-2.rds.amazonaws.com",user="admin",password="password")
cursor=db.cursor()
query = "use rasa"
cursor.execute(query)

class ActionFormInfo(FormAction):

    def name(self) -> Text:
        return "form_info"

    @staticmethod   
    def required_slots(tracker: Tracker) -> List[Text]:

        return ["mobile","source","arrival"]

    def slot_mappings(self) -> Dict[Text, Any]:

        return {
             "mobile": [self.from_text(intent=None), self.from_text()],
             "source": [self.from_text(intent=None), self.from_text()],
             "arrival": [self.from_text(intent=None), self.from_text()]
              }

    def submit(self, dispatcher: CollectingDispatcher,
               tracker: Tracker,
               domain: Dict[Text, Any],) -> List[Dict]:

        global book_id
        book_id=random.randint(10000,99999)
        #databaseAPI

        query = "insert into cab_book (bookid,address,dest,mobile) values ({},'{}','{}',{})".format(book_id,
                                                                        tracker.get_slot('source'),
                                                                        tracker.get_slot('arrival'),
                                                                        tracker.get_slot('mobile'))
        cursor.execute(query)
        db.commit()
        dispatcher.utter_message(template="utter_booked",id=book_id,number=tracker.get_slot('mobile'),
                                 pick_up=tracker.get_slot('source'),
                                 destination=tracker.get_slot('arrival'))

        return []


class ActionFormCancel(FormAction):

    def name(self) -> Text:
        return "form_cancel"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:

        return ["bookingid"]

    def slot_mappings(self) -> Dict[Text, Any]:

        return {
             "bookingid": [self.from_text(intent=None), self.from_text()]
              }

    def submit(self, dispatcher: CollectingDispatcher,
               tracker: Tracker,
               domain: Dict[Text, Any],) -> List[Dict]:
         #cancelAPI

        query = "delete from cab_book where bookid={};".format(tracker.get_slot('bookingid'))
        cursor.execute(query)
        
        dispatcher.utter_message("Your booking has been cancelled. Have a good day")

        return []


class ActionFormDetails(FormAction):

    def name(self) -> Text:
        return "form_details"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:

        return ["bookingid"]

    def slot_mappings(self) -> Dict[Text, Any]:

        return {
             "bookingid": [self.from_text(intent=None), self.from_text()]
              }

    def submit(self, dispatcher: CollectingDispatcher,
               tracker: Tracker,
               domain: Dict[Text, Any],) -> List[Dict]:
        #detailsAPI
        details = "select bookid from cab_book where bookid={};".format(tracker.get_slot('bookingid'))
        cursor.execute(details)
        details=str(details)
        dispatcher.utter_message("Here are your booking details: ",details)

        return []
