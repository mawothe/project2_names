import os

import pandas as pd
import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from sqlalchemy import inspect

from flask import Flask, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
from sqlalchemy import create_engine
from sqlalchemy import inspect

db_uri = 'sqlite:///data2.sqlite'
engine = create_engine(db_uri)

print("engine created")

inspector = inspect(engine)

# Get table information
print(inspector.get_table_names())
#################################################
# Database Setup
#################################################

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db/data2.sqlite"
db = SQLAlchemy(app)

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(db.engine, reflect=True)

@app.route("/")
def index():
    """Return to homepage."""
    return render_template("index.html")

@app.route("/names")
def names():
    stmnt1 = 'Select state,gender,name,amount from names'
    df = pd.read_sql(stmnt1, db.session.bind)
    Alaska = []
    Alabama = []
    Arizona = []
    Arkansas = []
    California = []
    Colorado = []
    Connecticut = []
    Delaware = []
    Florida = []
    Georgia = []
    Hawaii = []
    Idaho = []
    Illinois = []
    Indiana = []
    Iowa = []
    Kansas = []
    Kentucky = []
    Louisiana = []
    Maine = []
    Maryland = []
    Massachusetts = []
    Michigan = []
    Minnesota = []
    Mississippi = []
    Missouri = []
    Montana = []
    Nebraska = []
    Nevada = []
    New_Hampshire = []
    New_Jersey = []
    New_Mexico = []
    New_York = []
    North_Carolina = []
    North_Dakota = []
    Ohio = []
    Oklahoma =[]
    Oregon = []
    Pennsylvania = []
    Rhode_Island = []
    South_Carolina = []
    South_Dakota = []
    Tennessee = []
    Texas = []
    Utah = []
    Vermont = []
    Virginia = []
    Washington = []
    West_Virginia = []
    Wisconsin = []
    Wyoming = []
    i=0
    while i < len(df):
        for states in df:
            if (df['state'])[i] == 'AK':
                ak_entry = {'name':list(df['name'])[i],
                            'gender':list(df['gender'])[i],
                            'size':list(df['amount'])[i]}
                Alaska.append(ak_entry)
                break
            if (df['state'])[i] == 'AL':
                al_entry = {'name':list(df['name'])[i],
                            'gender':list(df['gender'])[i],
                            'size':list(df['amount'])[i]}
                Alabama.append(al_entry)
                break
            if (df['state'])[i] == 'AZ':
                az_entry = {'name':list(df['name'])[i],
                            'gender':list(df['gender'])[i],
                            'size':list(df['amount'])[i]}
                Arizona.append(az_entry)
                break
            if (df['state'])[i] == 'AR':
                ar_entry = {'name':list(df['name'])[i],
                            'gender':list(df['gender'])[i],
                            'size':list(df['amount'])[i]}
                Arkansas.append(ar_entry)
                break
            if (df['state'])[i] == 'CA':
                ca_entry = {'name':list(df['name'])[i],
                            'gender':list(df['gender'])[i],
                            'size':list(df['amount'])[i]}
                California.append(ca_entry)
                break
            if (df['state'])[i] == 'CO':
                co_entry = {'name':list(df['name'])[i],
                            'gender':list(df['gender'])[i],
                            'size':list(df['amount'])[i]}
                Colorado.append(co_entry)
                break
            if (df['state'])[i] == 'CT':
                ct_entry = {'name':list(df['name'])[i],
                            'gender':list(df['gender'])[i],
                            'size':list(df['amount'])[i]}
                Connecticut.append(ct_entry)
                break
            if (df['state'])[i] == 'DE':
                de_entry = {'name':list(df['name'])[i],
                            'gender':list(df['gender'])[i],
                            'size':list(df['amount'])[i]}
                Delaware.append(de_entry)
                break
            if (df['state'])[i] == 'FL':
                fl_entry = {'name':list(df['name'])[i],
                            'gender':list(df['gender'])[i],
                            'size':list(df['amount'])[i]}
                Florida.append(fl_entry)
                break
            if (df['state'])[i] == 'GA':
                ga_entry = {'name':list(df['name'])[i],
                            'gender':list(df['gender'])[i],
                            'size':list(df['amount'])[i]}
                Georgia.append(ga_entry)
                break
            if (df['state'])[i] == 'HI':
                hi_entry = {'name':list(df['name'])[i],
                            'gender':list(df['gender'])[i],
                            'size':list(df['amount'])[i]}
                Hawaii.append(hi_entry)
                break
            if (df['state'])[i] == 'HI':
                hi_entry = {'name':list(df['name'])[i],
                            'gender':list(df['gender'])[i],
                            'size':list(df['amount'])[i]}
                Hawaii.append(hi_entry)
                break
            if (df['state'])[i] == 'ID':
                id_entry = {'name':list(df['name'])[i],
                            'gender':list(df['gender'])[i],
                            'size':list(df['amount'])[i]}
                Idaho.append(id_entry)
                break
            if (df['state'])[i] == 'IL':
                il_entry = {'name':list(df['name'])[i],
                            'gender':list(df['gender'])[i],
                            'size':list(df['amount'])[i]}
                Illinois.append(il_entry)
                break
            if (df['state'])[i] == 'IN':
                in_entry = {'name':list(df['name'])[i],
                            'gender':list(df['gender'])[i],
                            'size':list(df['amount'])[i]}
                Indiana.append(in_entry)
                break
            if (df['state'])[i] == 'IA':
                ia_entry = {'name':list(df['name'])[i],
                            'gender':list(df['gender'])[i],
                            'size':list(df['amount'])[i]}
                Iowa.append(ia_entry)
                break
            if (df['state'])[i] == 'KS':
                ks_entry = {'name':list(df['name'])[i],
                            'gender':list(df['gender'])[i],
                            'size':list(df['amount'])[i]}
                Kansas.append(ks_entry)
                break
            if (df['state'])[i] == 'KY':
                ky_entry = {'name':list(df['name'])[i],
                            'gender':list(df['gender'])[i],
                            'size':list(df['amount'])[i]}
                Kentucky.append(ky_entry)
                break
            if (df['state'])[i] == 'LA':
                la_entry = {'name':list(df['name'])[i],
                            'gender':list(df['gender'])[i],
                            'size':list(df['amount'])[i]}
                Louisiana.append(la_entry)
                break
            if (df['state'])[i] == 'ME':
                me_entry = {'name':list(df['name'])[i],
                            'gender':list(df['gender'])[i],
                            'size':list(df['amount'])[i]}
                Maine.append(me_entry)
                break
            if (df['state'])[i] == 'MD':
                md_entry = {'name':list(df['name'])[i],
                            'gender':list(df['gender'])[i],
                            'size':list(df['amount'])[i]}
                Maryland.append(md_entry)
                break
            if (df['state'])[i] == 'MA':
                ma_entry = {'name':list(df['name'])[i],
                            'gender':list(df['gender'])[i],
                            'size':list(df['amount'])[i]}
                Massachusetts.append(ma_entry)
                break
            if (df['state'])[i] == 'MI':
                mi_entry = {'name':list(df['name'])[i],
                            'gender':list(df['gender'])[i],
                            'size':list(df['amount'])[i]}
                Michigan.append(mi_entry)
                break
            if (df['state'])[i] == 'MN':
                mn_entry = {'name':list(df['name'])[i],
                            'gender':list(df['gender'])[i],
                            'size':list(df['amount'])[i]}
                Minnesota.append(mn_entry)
                break
            if (df['state'])[i] == 'MS':
                ms_entry = {'name':list(df['name'])[i],
                            'gender':list(df['gender'])[i],
                            'size':list(df['amount'])[i]}
                Mississippi.append(ms_entry)
                break
            if (df['state'])[i] == 'MO':
                mo_entry = {'name':list(df['name'])[i],
                            'gender':list(df['gender'])[i],
                            'size':list(df['amount'])[i]}
                Missouri.append(mo_entry)
                break
            if (df['state'])[i] == 'MT':
                mt_entry = {'name':list(df['name'])[i],
                            'gender':list(df['gender'])[i],
                            'size':list(df['amount'])[i]}
                Montana.append(mt_entry)
                break
            if (df['state'])[i] == 'NE':
                ne_entry = {'name':list(df['name'])[i],
                            'gender':list(df['gender'])[i],
                            'size':list(df['amount'])[i]}
                Nebraska.append(ne_entry)
                break
            if (df['state'])[i] == 'NV':
                nv_entry = {'name':list(df['name'])[i],
                            'gender':list(df['gender'])[i],
                            'size':list(df['amount'])[i]}
                Nevada.append(nv_entry)
                break
            if (df['state'])[i] == 'NH':
                nh_entry = {'name':list(df['name'])[i],
                            'gender':list(df['gender'])[i],
                            'size':list(df['amount'])[i]}
                New_Hampshire.append(nh_entry)
                break
            if (df['state'])[i] == 'NJ':
                nj_entry = {'name':list(df['name'])[i],
                            'gender':list(df['gender'])[i],
                            'size':list(df['amount'])[i]}
                New_Jersey.append(nj_entry)
                break
            if (df['state'])[i] == 'NM':
                nm_entry = {'name':list(df['name'])[i],
                            'gender':list(df['gender'])[i],
                            'size':list(df['amount'])[i]}
                New_Mexico.append(nm_entry)
                break
            if (df['state'])[i] == 'NY':
                ny_entry = {'name':list(df['name'])[i],
                            'gender':list(df['gender'])[i],
                            'size':list(df['amount'])[i]}
                New_York.append(ny_entry)
                break
            if (df['state'])[i] == 'NC':
                nc_entry = {'name':list(df['name'])[i],
                            'gender':list(df['gender'])[i],
                            'size':list(df['amount'])[i]}
                North_Carolina.append(nc_entry)
                break
            if (df['state'])[i] == 'ND':
                nd_entry = {'name':list(df['name'])[i],
                            'gender':list(df['gender'])[i],
                            'size':list(df['amount'])[i]}
                North_Dakota.append(nd_entry)
                break
            if (df['state'])[i] == 'OH':
                oh_entry = {'name':list(df['name'])[i],
                            'gender':list(df['gender'])[i],
                            'size':list(df['amount'])[i]}
                Ohio.append(oh_entry)
                break
            if (df['state'])[i] == 'OK':
                ok_entry = {'name':list(df['name'])[i],
                            'gender':list(df['gender'])[i],
                            'size':list(df['amount'])[i]}
                Oklahoma.append(ok_entry)
                break
            if (df['state'])[i] == 'OR':
                or_entry = {'name':list(df['name'])[i],
                            'gender':list(df['gender'])[i],
                            'size':list(df['amount'])[i]}
                Oregon.append(or_entry)
                break
            if (df['state'])[i] == 'PA':
                pa_entry = {'name':list(df['name'])[i],
                            'gender':list(df['gender'])[i],
                            'size':list(df['amount'])[i]}
                Pennsylvania.append(pa_entry)
                break
            if (df['state'])[i] == 'RI':
                ri_entry = {'name':list(df['name'])[i],
                            'gender':list(df['gender'])[i],
                            'size':list(df['amount'])[i]}
                Rhode_Island.append(ri_entry)
                break
            if (df['state'])[i] == 'SC':
                sc_entry = {'name':list(df['name'])[i],
                            'gender':list(df['gender'])[i],
                            'size':list(df['amount'])[i]}
                South_Carolina.append(sc_entry)
                break
            if (df['state'])[i] == 'SD':
                sd_entry = {'name':list(df['name'])[i],
                            'gender':list(df['gender'])[i],
                            'size':list(df['amount'])[i]}
                South_Dakota.append(sd_entry)
                break
            if (df['state'])[i] == 'TN':
                tn_entry = {'name':list(df['name'])[i],
                            'gender':list(df['gender'])[i],
                            'size':list(df['amount'])[i]}
                Tennessee.append(tn_entry)
                break
            if (df['state'])[i] == 'TX':
                tx_entry = {'name':list(df['name'])[i],
                            'gender':list(df['gender'])[i],
                            'size':list(df['amount'])[i]}
                Texas.append(tx_entry)
                break
            if (df['state'])[i] == 'UT':
                ut_entry = {'name':list(df['name'])[i],
                            'gender':list(df['gender'])[i],
                            'size':list(df['amount'])[i]}
                Utah.append(ut_entry)
                break
            if (df['state'])[i] == 'VT':
                vt_entry = {'name':list(df['name'])[i],
                            'gender':list(df['gender'])[i],
                            'size':list(df['amount'])[i]}
                Vermont.append(vt_entry)
                break
            if (df['state'])[i] == 'VA':
                va_entry = {'name':list(df['name'])[i],
                            'gender':list(df['gender'])[i],
                            'size':list(df['amount'])[i]}
                Virginia.append(va_entry)
                break
            if (df['state'])[i] == 'WA':
                wa_entry = {'name':list(df['name'])[i],
                            'gender':list(df['gender'])[i],
                            'size':list(df['amount'])[i]}
                Washington.append(wa_entry)
                break
            if (df['state'])[i] == 'WV':
                wv_entry = {'name':list(df['name'])[i],
                            'gender':list(df['gender'])[i],
                            'size':list(df['amount'])[i]}
                West_Virginia.append(wv_entry)
                break
            if (df['state'])[i] == 'WI':
                wi_entry = {'name':list(df['name'])[i],
                            'gender':list(df['gender'])[i],
                            'size':list(df['amount'])[i]}
                Wisconsin.append(wi_entry)
                break
            if (df['state'])[i] == 'WY':
                wy_entry = {'name':list(df['name'])[i],
                            'gender':list(df['gender'])[i],
                            'size':list(df['amount'])[i]}
                Wyoming.append(wy_entry)
                break
        
        non_contiguous_list = []
        pacific_list = []
        rocky_mountain_list = []
        southwest_list = []
        midwest_list = []
        southeast_list = []
        northeast_list = []

        non_contiguous = {"Alaska":Alaska, "Hawaii":Hawaii}
        for key, value in non_contiguous.items():
            noncontiguous_entry = {'name': key,
                                   'children': value}
            non_contiguous_list.append(noncontiguous_entry)

        pacific = {"Washington": Washington, "Oregon": Oregon, "California": California}
        for key, value in pacific.items():
            pacific_entry = {'name': key,
                             'children': value}
            pacific_list.append(pacific_entry)
        
        rocky_mountains = {"Montana": Montana,
                   "Idaho": Idaho,
                   "Nevada": Nevada,
                   "Utah": Utah,
                   "Colorado": Colorado}
        for key, value in rocky_mountains.items():
            rocky_entry = {'name': key,
                           'children': value}
            rocky_mountain_list.append(rocky_entry)

        southwest = {"New Mexico": New_Mexico,
                     "Texas": Texas,
                     "Oklahoma": Oklahoma}
        for key, value in southwest.items():
            southwest_entry = {'name': key,
                               'children': value}
            southwest_list.append(southwest_entry)
        
        midwest = {"Minnesota": Minnesota,
                   "Iowa": Iowa,
                   "Wisconsin": Wisconsin,
                   "Ohio": Ohio,
                   "North Dakota": North_Dakota,
                   "South Dakota": South_Dakota,
                   "Nebraska": Nebraska,
                   "Kansas": Kansas,
                   "Missouri": Missouri,
                   "Michigan": Michigan,
                   "Illinois": Illinois,
                   "Indiana": Indiana}
        for key, value in midwest.items():
            midwest_entry = {'name': key,
                             'children': value}
            midwest_list.append(midwest_entry)

        northeast = {"Maine": Maine,
                     "New Hampshire": New_Hampshire,
                     "Massachusetts": Massachusetts,
                     "Connecticut": Connecticut,
                     "Rhode Island": Rhode_Island,
                     "New York": New_York,
                     "Pennsylvania": Pennsylvania,
                     "New Jersey": New_Jersey}
        for key, value in northeast.items():
            northeast_entry = {'name': key,
                               'children': value}
            northeast_list.append(northeast_entry)
        
        southeast = {"West Virginia": West_Virginia,
                     "Delaware": Delaware,
                     "Maryland": Maryland,
                     "Virginia": Virginia,
                     "Kentucky": Kentucky,
                     "Tennessee": Tennessee,
                     "North Carolina": North_Carolina,
                     "Arkansas": Arkansas,
                     "Louisiana": Louisiana,
                     "Mississippi": Mississippi,
                     "Alabama": Alabama,
                     "Georgia": Georgia,
                     "South Carolina": South_Carolina,
                     "Florida": Florida}
        for key, value in southeast.items():
            southeast_entry = {'name': key,
                               'children': value}
            southeast_list.append(southeast_entry)
        i+=1
    return jsonify({'name': 'United States',
                    'children': [
                        {'name': 'Non-Contiguous', 'children': non_contiguous_list},
                        {'name': 'Pacific', 'children': pacific_list},
                        {'name': 'Rocky Mountains', 'children': rocky_mountain_list},
                        {'name': 'Southwest', 'children': southeast_list},
                        {'name': 'Midwest', 'children': midwest_list},
                        {'name': 'Northeast', 'children': northeast_list},
                        {'name': 'Southeast', 'children': southeast_list}
                        ]
                    })

if __name__ == "__main__":
    app.run()