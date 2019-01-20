from radius_db import RadiusDB
from rules import Rules
import pandas as pd
from dataset import PROPERTY_DATA, REQUIREMENT_DATA, REQUIREMENT_QUE, PROPERTY_QUE
from PyInquirer import prompt


class Matching(object):

    def __init__(self, input_type, query_obj={}):
        """

        :param input_type: The type of input user has entered. Can be REQUIREMNT or PROPERTY
        :param query_obj: Answers to the questions asked.
        """
        self.input = input_type
        self.query_obj = query_obj

    def matching(self):
        """

        :return: Returns the matched items.
        """
        db = RadiusDB()
        if input_type == "PROPERTY":
            resoverall = db._fetch_all_from_table(REQUIREMENT_DATA)
            df = pd.DataFrame(resoverall.fetchall())
            df.columns = ['id'] + REQUIREMENT_DATA.get('COLUMN_NAMES')
        else:
            resoverall = db._fetch_all_from_table(PROPERTY_DATA)
            df = pd.DataFrame(resoverall.fetchall())
            df.columns = ['id'] + PROPERTY_DATA.get('COLUMN_NAMES')
        df1 = Rules.price_rules(query_obj, df).assign(score=30)
        df2 = Rules.room_rules(query_obj, df, 'bedrooms').assign(score=20)
        df3 = Rules.room_rules(query_obj, df, 'bathrooms').assign(score=20)
        df4 = Rules.distance_rules(query_obj, df).assign(score=30)
        df5 = pd.concat([df, df1[['score']], df2[['score']], df3[['score']], df4[['score']]], sort=True).groupby(
            level=0).sum()
        print("Following are your query matches: \n")
        print(df5[(df5['score'] >= 40)])


if __name__ == '__main__':
    print('Matching algorithm....')
    print("Enter the input type")
    input_type = input()
    if input_type == "REQUIREMENT":
        query_obj = prompt(REQUIREMENT_QUE)
    else:
        query_obj = prompt(PROPERTY_QUE)
    match_obj = Matching(input_type, query_obj)
    match_obj.matching()
