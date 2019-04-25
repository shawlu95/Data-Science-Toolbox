import numpy as np
import pandas as pd
from sqlalchemy import create_engine

class Loader(object):
    
    def __init__(self):
        self.cat_cols = ["last_category", "event1", "month", "last_event1", "last_event2", "last_prodcat1", "last_prodcat2"]
        
        username = "privateuser"
        password = "***********"
        port = 7777

        self.engine = create_engine('mysql+mysqldb://%s:%s@localhost:%i/Shutterfly'%(username, password, port))
        
    def load(self, split="trn_set", ignore_categorical=False, nrows=None):
        sql = """
        SELECT o.*, f1.*, f2.*, f3.*, f4.*,
        EXTRACT(MONTH FROM o.dt) AS month
        FROM %s AS t 
        JOIN Online AS o 
            ON t.index = o.index 
        JOIN features_group_1 AS f1
            ON t.index = f1.index
        JOIN features_group_2 AS f2
            ON t.index = f2.index
        JOIN features_group_3 AS f3
            ON t.index = f3.index
        JOIN features_group_4 AS f4
            ON t.index = f4.index
        """%split
        if nrows:
            sql += "LIMIT %i;"%nrows

        df = pd.read_sql_query(sql.replace('\n', " ").replace("\t", " "), self.engine)
        df.event1 = df.event1.fillna(0)
        X = df.drop(["index", "event2", "dt", "day", "session", "visitor", "custno"], axis=1)

        if ignore_categorical:
            X = X.drop(self.cat_cols, axis=1)

        Y = df.event2
        return X, Y

    def encode(self, ohe, X):
        X_numeric = X.drop(self.cat_cols, axis=1)
        X_cat = ohe.transform(X[self.cat_cols].fillna(0)).todense()
        X_combined = np.concatenate([X_numeric.values, X_cat], axis=1)
        return X_combined