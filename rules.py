from utils import haversine


class Rules(object):
    @staticmethod
    def price_rules(query_obj, df):
        """

        :param query_obj: The parameters queried by user
        :param df: Data frame
        :return: Filtered df
        """
        if 'min_price' in query_obj and 'max_price' in query_obj:
            return df[(df["price"] <= query_obj.get('max_price')) & (df["price"] >= query_obj.get('min_price'))]
        elif 'min_price' in query_obj:
            return df[
                (df["price"] <= (1.1 * query_obj.get('min_price'))) &
                (df["price"] >= (0.9 * query_obj.get('min_price')))
                ]
        elif 'price' in query_obj:
            return df[(query_obj["price"] <= df['max_price']) & (query_obj["price"] >= df['min_price'])]
        else:
            return df[
                (df["price"] <= (1.1 * query_obj.get('max_price'))) &
                (df["price"] >= (0.9 * query_obj.get('max_price')))
                ]

    @staticmethod
    def room_rules(query_obj, df, room_name):
        """

        :param query_obj: Parameters
        :param df: Data Frame
        :param room_name: The type of room given by user
        :return: Data frame filtered.
        """
        min_range_text, max_range_text = ('min_number_of_%s' % room_name, 'max_number_of_%s' % room_name)
        room_text = "number_of_%s" % room_name

        if min_range_text in query_obj and max_range_text in query_obj:
            return df[
                (df[room_text] <= query_obj.get(max_range_text)) &
                (df[room_text] >= query_obj.get(min_range_text))
                ]
        else:
            return df[
                (query_obj[room_text] <= df[max_range_text]) &
                (query_obj[room_text] >= df[min_range_text])
                ]

        return df

    @staticmethod
    def distance_rules(query_obj, df):
        """

        :param query_obj: LAtitude and longitude entered/
        :param df:
        :return: Filtered df according to lat and long
        """
        if 'latitude' in query_obj and 'longitude' in query_obj:
            df['distance_in_miles'] = df.apply(
                (lambda row: haversine(
                    row['latitude'], row['longitude'],
                    query_obj.get('latitude'), query_obj.get('longitude')
                )),
                axis=1
            )
            return df[
                (df['distance_in_miles'] <= 2)
            ]

        return df
