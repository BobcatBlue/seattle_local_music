import pandas as pd
import requests
import os
import json



class TicketMasterShows:
    TM_API_KEY = os.getenv("ticketmaster_api_1")

    def __init__(self, dataframe):
        self.df = dataframe

    def access_info(self):
        pass



df = pd.read_csv("Seattle_ticketmaster_venues - Sheet1.csv")

