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

@app.route("/girls")
def girl_names():

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
    Oklahoma = []
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
            if (df['state'])[i] == 'AK' and (df['gender'])[i] == 'F':
                ak_entry = {'name':list(df['name'])[i],
                            'gender':list(df['gender'])[i],
                            'size':list(df['amount'])[i]}
                Alaska.append(ak_entry)
                break
            if (df['state'])[i] == 'AL' and (df['gender'])[i] == 'F':
                al_entry = {'name':list(df['name'])[i],
                            'gender':list(df['gender'])[i],
                            'size':list(df['amount'])[i]}
                Alabama.append(al_entry)
                break
            if (df['state'])[i] == 'AZ' and (df['gender'])[i] == 'F':
                az_entry = {'name':list(df['name'])[i],
                            'gender':list(df['gender'])[i],
                            'size':list(df['amount'])[i]}
                Arizona.append(az_entry)
                break
            if (df['state'])[i] == 'AR' and (df['gender'])[i] == 'F':
                ar_entry = {'name':list(df['name'])[i],
                            'gender':list(df['gender'])[i],
                            'size':list(df['amount'])[i]}
                Arkansas.append(ar_entry)
                break
            if (df['state'])[i] == 'CA' and (df['gender'])[i] == 'F':
                ca_entry = {'name':list(df['name'])[i],
                            'gender':list(df['gender'])[i],
                            'size':list(df['amount'])[i]}
                California.append(ca_entry)
                break
            if (df['state'])[i] == 'CO' and (df['gender'])[i] == 'F':
                co_entry = {'name':list(df['name'])[i],
                            'gender':list(df['gender'])[i],
                            'size':list(df['amount'])[i]}
                Colorado.append(co_entry)
                break
            if (df['state'])[i] == 'CT' and (df['gender'])[i] == 'F':
                ct_entry = {'name':list(df['name'])[i],
                            'gender':list(df['gender'])[i],
                            'size':list(df['amount'])[i]}
                Connecticut.append(ct_entry)
                break
            if (df['state'])[i] == 'DE' and (df['gender'])[i] == 'F':
                de_entry = {'name':list(df['name'])[i],
                            'gender':list(df['gender'])[i],
                            'size':list(df['amount'])[i]}
                Delaware.append(de_entry)
                break
            if (df['state'])[i] == 'FL' and (df['gender'])[i] == 'F':
                fl_entry = {'name':list(df['name'])[i],
                            'gender':list(df['gender'])[i],
                            'size':list(df['amount'])[i]}
                Florida.append(fl_entry)
                break
            if (df['state'])[i] == 'GA' and (df['gender'])[i] == 'F':
                ga_entry = {'name':list(df['name'])[i],
                            'gender':list(df['gender'])[i],
                            'size':list(df['amount'])[i]}
                Georgia.append(ga_entry)
                break
            if (df['state'])[i] == 'HI' and (df['gender'])[i] == 'F':
                hi_entry = {'name':list(df['name'])[i],
                            'gender':list(df['gender'])[i],
                            'size':list(df['amount'])[i]}
                Hawaii.append(hi_entry)
                break
            if (df['state'])[i] == 'ID' and (df['gender'])[i] == 'F':
                id_entry = {'name':list(df['name'])[i],
                            'gender':list(df['gender'])[i],
                            'size':list(df['amount'])[i]}
                Idaho.append(id_entry)
                break
            if (df['state'])[i] == 'IL' and (df['gender'])[i] == 'F':
                il_entry = {'name':list(df['name'])[i],
                            'gender':list(df['gender'])[i],
                            'size':list(df['amount'])[i]}
                Illinois.append(il_entry)
                break
            if (df['state'])[i] == 'IN' and (df['gender'])[i] == 'F':
                in_entry = {'name':list(df['name'])[i],
                            'gender':list(df['gender'])[i],
                            'size':list(df['amount'])[i]}
                Indiana.append(in_entry)
                break
            if (df['state'])[i] == 'IA' and (df['gender'])[i] == 'F':
                ia_entry = {'name':list(df['name'])[i],
                            'gender':list(df['gender'])[i],
                            'size':list(df['amount'])[i]}
                Iowa.append(ia_entry)
                break
            if (df['state'])[i] == 'KS' and (df['gender'])[i] == 'F':
                ks_entry = {'name':list(df['name'])[i],
                            'gender':list(df['gender'])[i],
                            'size':list(df['amount'])[i]}
                Kansas.append(ks_entry)
                break
            if (df['state'])[i] == 'KY' and (df['gender'])[i] == 'F':
                ky_entry = {'name':list(df['name'])[i],
                            'gender':list(df['gender'])[i],
                            'size':list(df['amount'])[i]}
                Kentucky.append(ky_entry)
                break
            if (df['state'])[i] == 'LA' and (df['gender'])[i] == 'F':
                la_entry = {'name':list(df['name'])[i],
                            'gender':list(df['gender'])[i],
                            'size':list(df['amount'])[i]}
                Louisiana.append(la_entry)
                break
            if (df['state'])[i] == 'ME' and (df['gender'])[i] == 'F':
                me_entry = {'name':list(df['name'])[i],
                            'gender':list(df['gender'])[i],
                            'size':list(df['amount'])[i]}
                Maine.append(me_entry)
                break
            if (df['state'])[i] == 'MD' and (df['gender'])[i] == 'F':
                md_entry = {'name':list(df['name'])[i],
                            'gender':list(df['gender'])[i],
                            'size':list(df['amount'])[i]}
                Maryland.append(md_entry)
                break
            if (df['state'])[i] == 'MA' and (df['gender'])[i] == 'F':
                ma_entry = {'name':list(df['name'])[i],
                            'gender':list(df['gender'])[i],
                            'size':list(df['amount'])[i]}
                Massachusetts.append(ma_entry)
                break
            if (df['state'])[i] == 'MI' and (df['gender'])[i] == 'F':
                mi_entry = {'name':list(df['name'])[i],
                            'gender':list(df['gender'])[i],
                            'size':list(df['amount'])[i]}
                Michigan.append(mi_entry)
                break
            if (df['state'])[i] == 'MN' and (df['gender'])[i] == 'F':
                mn_entry = {'name':list(df['name'])[i],
                            'gender':list(df['gender'])[i],
                            'size':list(df['amount'])[i]}
                Minnesota.append(mn_entry)
                break
            if (df['state'])[i] == 'MS' and (df['gender'])[i] == 'F':
                ms_entry = {'name':list(df['name'])[i],
                            'gender':list(df['gender'])[i],
                            'size':list(df['amount'])[i]}
                Mississippi.append(ms_entry)
                break
            if (df['state'])[i] == 'MO' and (df['gender'])[i] == 'F':
                mo_entry = {'name':list(df['name'])[i],
                            'gender':list(df['gender'])[i],
                            'size':list(df['amount'])[i]}
                Missouri.append(mo_entry)
                break
            if (df['state'])[i] == 'MT' and (df['gender'])[i] == 'F':
                mt_entry = {'name':list(df['name'])[i],
                            'gender':list(df['gender'])[i],
                            'size':list(df['amount'])[i]}
                Montana.append(mt_entry)
                break
            if (df['state'])[i] == 'NE' and (df['gender'])[i] == 'F':
                ne_entry = {'name':list(df['name'])[i],
                            'gender':list(df['gender'])[i],
                            'size':list(df['amount'])[i]}
                Nebraska.append(ne_entry)
                break
            if (df['state'])[i] == 'NV' and (df['gender'])[i] == 'F':
                nv_entry = {'name':list(df['name'])[i],
                            'gender':list(df['gender'])[i],
                            'size':list(df['amount'])[i]}
                Nevada.append(nv_entry)
                break
            if (df['state'])[i] == 'NH' and (df['gender'])[i] == 'F':
                nh_entry = {'name':list(df['name'])[i],
                            'gender':list(df['gender'])[i],
                            'size':list(df['amount'])[i]}
                New_Hampshire.append(nh_entry)
                break
            if (df['state'])[i] == 'NJ' and (df['gender'])[i] == 'F':
                nj_entry = {'name':list(df['name'])[i],
                            'gender':list(df['gender'])[i],
                            'size':list(df['amount'])[i]}
                New_Jersey.append(nj_entry)
                break
            if (df['state'])[i] == 'NM' and (df['gender'])[i] == 'F':
                nm_entry = {'name':list(df['name'])[i],
                            'gender':list(df['gender'])[i],
                            'size':list(df['amount'])[i]}
                New_Mexico.append(nm_entry)
                break
            if (df['state'])[i] == 'NY' and (df['gender'])[i] == 'F':
                ny_entry = {'name':list(df['name'])[i],
                            'gender':list(df['gender'])[i],
                            'size':list(df['amount'])[i]}
                New_York.append(ny_entry)
                break
            if (df['state'])[i] == 'NC' and (df['gender'])[i] == 'F':
                nc_entry = {'name':list(df['name'])[i],
                            'gender':list(df['gender'])[i],
                            'size':list(df['amount'])[i]}
                North_Carolina.append(nc_entry)
                break
            if (df['state'])[i] == 'ND' and (df['gender'])[i] == 'F':
                nd_entry = {'name':list(df['name'])[i],
                            'gender':list(df['gender'])[i],
                            'size':list(df['amount'])[i]}
                North_Dakota.append(nd_entry)
                break
            if (df['state'])[i] == 'OH' and (df['gender'])[i] == 'F':
                oh_entry = {'name':list(df['name'])[i],
                            'gender':list(df['gender'])[i],
                            'size':list(df['amount'])[i]}
                Ohio.append(oh_entry)
                break
            if (df['state'])[i] == 'OK' and (df['gender'])[i] == 'F':
                ok_entry = {'name':list(df['name'])[i],
                            'gender':list(df['gender'])[i],
                            'size':list(df['amount'])[i]}
                Oklahoma.append(ok_entry)
                break
            if (df['state'])[i] == 'OR' and (df['gender'])[i] == 'F':
                or_entry = {'name':list(df['name'])[i],
                            'gender':list(df['gender'])[i],
                            'size':list(df['amount'])[i]}
                Oregon.append(or_entry)
                break
            if (df['state'])[i] == 'PA' and (df['gender'])[i] == 'F':
                pa_entry = {'name':list(df['name'])[i],
                            'gender':list(df['gender'])[i],
                            'size':list(df['amount'])[i]}
                Pennsylvania.append(pa_entry)
                break
            if (df['state'])[i] == 'RI' and (df['gender'])[i] == 'F':
                ri_entry = {'name':list(df['name'])[i],
                            'gender':list(df['gender'])[i],
                            'size':list(df['amount'])[i]}
                Rhode_Island.append(ri_entry)
                break
            if (df['state'])[i] == 'SC' and (df['gender'])[i] == 'F':
                sc_entry = {'name':list(df['name'])[i],
                            'gender':list(df['gender'])[i],
                            'size':list(df['amount'])[i]}
                South_Carolina.append(sc_entry)
                break
            if (df['state'])[i] == 'SD' and (df['gender'])[i] == 'F':
                sd_entry = {'name':list(df['name'])[i],
                            'gender':list(df['gender'])[i],
                            'size':list(df['amount'])[i]}
                South_Dakota.append(sd_entry)
                break
            if (df['state'])[i] == 'TN' and (df['gender'])[i] == 'F':
                tn_entry = {'name':list(df['name'])[i],
                            'gender':list(df['gender'])[i],
                            'size':list(df['amount'])[i]}
                Tennessee.append(tn_entry)
                break
            if (df['state'])[i] == 'TX' and (df['gender'])[i] == 'F':
                tx_entry = {'name':list(df['name'])[i],
                            'gender':list(df['gender'])[i],
                            'size':list(df['amount'])[i]}
                Texas.append(tx_entry)
                break
            if (df['state'])[i] == 'UT' and (df['gender'])[i] == 'F':
                ut_entry = {'name':list(df['name'])[i],
                            'gender':list(df['gender'])[i],
                            'size':list(df['amount'])[i]}
                Utah.append(ut_entry)
                break
            if (df['state'])[i] == 'VT' and (df['gender'])[i] == 'F':
                vt_entry = {'name':list(df['name'])[i],
                            'gender':list(df['gender'])[i],
                            'size':list(df['amount'])[i]}
                Vermont.append(vt_entry)
                break
            if (df['state'])[i] == 'VA' and (df['gender'])[i] == 'F':
                va_entry = {'name':list(df['name'])[i],
                            'gender':list(df['gender'])[i],
                            'size':list(df['amount'])[i]}
                Virginia.append(va_entry)
                break
            if (df['state'])[i] == 'WA' and (df['gender'])[i] == 'F':
                wa_entry = {'name':list(df['name'])[i],
                            'gender':list(df['gender'])[i],
                            'size':list(df['amount'])[i]}
                Washington.append(wa_entry)
                break
            if (df['state'])[i] == 'WV' and (df['gender'])[i] == 'F':
                wv_entry = {'name':list(df['name'])[i],
                            'gender':list(df['gender'])[i],
                            'size':list(df['amount'])[i]}
                West_Virginia.append(wv_entry)
                break
            if (df['state'])[i] == 'WI' and (df['gender'])[i] == 'F':
                wi_entry = {'name':list(df['name'])[i],
                            'gender':list(df['gender'])[i],
                            'size':list(df['amount'])[i]}
                Wisconsin.append(wi_entry)
                break
            if (df['state'])[i] == 'WY' and (df['gender'])[i] == 'F':
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

@app.route("/boys")
def boy_names():

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
    Oklahoma = []
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
            if (df['state'])[i] == 'AK' and (df['gender'])[i] == 'M':
                ak_entry = {'name':list(df['name'])[i],
                            'gender':list(df['gender'])[i],
                            'size':list(df['amount'])[i]}
                Alaska.append(ak_entry)
                break
            if (df['state'])[i] == 'AL' and (df['gender'])[i] == 'M':
                al_entry = {'name':list(df['name'])[i],
                            'gender':list(df['gender'])[i],
                            'size':list(df['amount'])[i]}
                Alabama.append(al_entry)
                break
            if (df['state'])[i] == 'AZ' and (df['gender'])[i] == 'M':
                az_entry = {'name':list(df['name'])[i],
                            'gender':list(df['gender'])[i],
                            'size':list(df['amount'])[i]}
                Arizona.append(az_entry)
                break
            if (df['state'])[i] == 'AR' and (df['gender'])[i] == 'M':
                ar_entry = {'name':list(df['name'])[i],
                            'gender':list(df['gender'])[i],
                            'size':list(df['amount'])[i]}
                Arkansas.append(ar_entry)
                break
            if (df['state'])[i] == 'CA' and (df['gender'])[i] == 'M':
                ca_entry = {'name':list(df['name'])[i],
                            'gender':list(df['gender'])[i],
                            'size':list(df['amount'])[i]}
                California.append(ca_entry)
                break
            if (df['state'])[i] == 'CO' and (df['gender'])[i] == 'M':
                co_entry = {'name':list(df['name'])[i],
                            'gender':list(df['gender'])[i],
                            'size':list(df['amount'])[i]}
                Colorado.append(co_entry)
                break
            if (df['state'])[i] == 'CT' and (df['gender'])[i] == 'M':
                ct_entry = {'name':list(df['name'])[i],
                            'gender':list(df['gender'])[i],
                            'size':list(df['amount'])[i]}
                Connecticut.append(ct_entry)
                break
            if (df['state'])[i] == 'DE' and (df['gender'])[i] == 'M':
                de_entry = {'name':list(df['name'])[i],
                            'gender':list(df['gender'])[i],
                            'size':list(df['amount'])[i]}
                Delaware.append(de_entry)
                break
            if (df['state'])[i] == 'FL' and (df['gender'])[i] == 'M':
                fl_entry = {'name':list(df['name'])[i],
                            'gender':list(df['gender'])[i],
                            'size':list(df['amount'])[i]}
                Florida.append(fl_entry)
                break
            if (df['state'])[i] == 'GA' and (df['gender'])[i] == 'M':
                ga_entry = {'name':list(df['name'])[i],
                            'gender':list(df['gender'])[i],
                            'size':list(df['amount'])[i]}
                Georgia.append(ga_entry)
                break
            if (df['state'])[i] == 'HI' and (df['gender'])[i] == 'M':
                hi_entry = {'name':list(df['name'])[i],
                            'gender':list(df['gender'])[i],
                            'size':list(df['amount'])[i]}
                Hawaii.append(hi_entry)
                break
            if (df['state'])[i] == 'ID' and (df['gender'])[i] == 'M':
                id_entry = {'name':list(df['name'])[i],
                            'gender':list(df['gender'])[i],
                            'size':list(df['amount'])[i]}
                Idaho.append(id_entry)
                break
            if (df['state'])[i] == 'IL' and (df['gender'])[i] == 'M':
                il_entry = {'name':list(df['name'])[i],
                            'gender':list(df['gender'])[i],
                            'size':list(df['amount'])[i]}
                Illinois.append(il_entry)
                break
            if (df['state'])[i] == 'IN' and (df['gender'])[i] == 'M':
                in_entry = {'name':list(df['name'])[i],
                            'gender':list(df['gender'])[i],
                            'size':list(df['amount'])[i]}
                Indiana.append(in_entry)
                break
            if (df['state'])[i] == 'IA' and (df['gender'])[i] == 'M':
                ia_entry = {'name':list(df['name'])[i],
                            'gender':list(df['gender'])[i],
                            'size':list(df['amount'])[i]}
                Iowa.append(ia_entry)
                break
            if (df['state'])[i] == 'KS' and (df['gender'])[i] == 'M':
                ks_entry = {'name':list(df['name'])[i],
                            'gender':list(df['gender'])[i],
                            'size':list(df['amount'])[i]}
                Kansas.append(ks_entry)
                break
            if (df['state'])[i] == 'KY' and (df['gender'])[i] == 'M':
                ky_entry = {'name':list(df['name'])[i],
                            'gender':list(df['gender'])[i],
                            'size':list(df['amount'])[i]}
                Kentucky.append(ky_entry)
                break
            if (df['state'])[i] == 'LA' and (df['gender'])[i] == 'M':
                la_entry = {'name':list(df['name'])[i],
                            'gender':list(df['gender'])[i],
                            'size':list(df['amount'])[i]}
                Louisiana.append(la_entry)
                break
            if (df['state'])[i] == 'ME' and (df['gender'])[i] == 'M':
                me_entry = {'name':list(df['name'])[i],
                            'gender':list(df['gender'])[i],
                            'size':list(df['amount'])[i]}
                Maine.append(me_entry)
                break
            if (df['state'])[i] == 'MD' and (df['gender'])[i] == 'M':
                md_entry = {'name':list(df['name'])[i],
                            'gender':list(df['gender'])[i],
                            'size':list(df['amount'])[i]}
                Maryland.append(md_entry)
                break
            if (df['state'])[i] == 'MA' and (df['gender'])[i] == 'M':
                ma_entry = {'name':list(df['name'])[i],
                            'gender':list(df['gender'])[i],
                            'size':list(df['amount'])[i]}
                Massachusetts.append(ma_entry)
                break
            if (df['state'])[i] == 'MI' and (df['gender'])[i] == 'M':
                mi_entry = {'name':list(df['name'])[i],
                            'gender':list(df['gender'])[i],
                            'size':list(df['amount'])[i]}
                Michigan.append(mi_entry)
                break
            if (df['state'])[i] == 'MN' and (df['gender'])[i] == 'M':
                mn_entry = {'name':list(df['name'])[i],
                            'gender':list(df['gender'])[i],
                            'size':list(df['amount'])[i]}
                Minnesota.append(mn_entry)
                break
            if (df['state'])[i] == 'MS' and (df['gender'])[i] == 'M':
                ms_entry = {'name':list(df['name'])[i],
                            'gender':list(df['gender'])[i],
                            'size':list(df['amount'])[i]}
                Mississippi.append(ms_entry)
                break
            if (df['state'])[i] == 'MO' and (df['gender'])[i] == 'M':
                mo_entry = {'name':list(df['name'])[i],
                            'gender':list(df['gender'])[i],
                            'size':list(df['amount'])[i]}
                Missouri.append(mo_entry)
                break
            if (df['state'])[i] == 'MT' and (df['gender'])[i] == 'M':
                mt_entry = {'name':list(df['name'])[i],
                            'gender':list(df['gender'])[i],
                            'size':list(df['amount'])[i]}
                Montana.append(mt_entry)
                break
            if (df['state'])[i] == 'NE' and (df['gender'])[i] == 'M':
                ne_entry = {'name':list(df['name'])[i],
                            'gender':list(df['gender'])[i],
                            'size':list(df['amount'])[i]}
                Nebraska.append(ne_entry)
                break
            if (df['state'])[i] == 'NV' and (df['gender'])[i] == 'M':
                nv_entry = {'name':list(df['name'])[i],
                            'gender':list(df['gender'])[i],
                            'size':list(df['amount'])[i]}
                Nevada.append(nv_entry)
                break
            if (df['state'])[i] == 'NH' and (df['gender'])[i] == 'M':
                nh_entry = {'name':list(df['name'])[i],
                            'gender':list(df['gender'])[i],
                            'size':list(df['amount'])[i]}
                New_Hampshire.append(nh_entry)
                break
            if (df['state'])[i] == 'NJ' and (df['gender'])[i] == 'M':
                nj_entry = {'name':list(df['name'])[i],
                            'gender':list(df['gender'])[i],
                            'size':list(df['amount'])[i]}
                New_Jersey.append(nj_entry)
                break
            if (df['state'])[i] == 'NM' and (df['gender'])[i] == 'M':
                nm_entry = {'name':list(df['name'])[i],
                            'gender':list(df['gender'])[i],
                            'size':list(df['amount'])[i]}
                New_Mexico.append(nm_entry)
                break
            if (df['state'])[i] == 'NY' and (df['gender'])[i] == 'M':
                ny_entry = {'name':list(df['name'])[i],
                            'gender':list(df['gender'])[i],
                            'size':list(df['amount'])[i]}
                New_York.append(ny_entry)
                break
            if (df['state'])[i] == 'NC' and (df['gender'])[i] == 'M':
                nc_entry = {'name':list(df['name'])[i],
                            'gender':list(df['gender'])[i],
                            'size':list(df['amount'])[i]}
                North_Carolina.append(nc_entry)
                break
            if (df['state'])[i] == 'ND' and (df['gender'])[i] == 'M':
                nd_entry = {'name':list(df['name'])[i],
                            'gender':list(df['gender'])[i],
                            'size':list(df['amount'])[i]}
                North_Dakota.append(nd_entry)
                break
            if (df['state'])[i] == 'OH' and (df['gender'])[i] == 'M':
                oh_entry = {'name':list(df['name'])[i],
                            'gender':list(df['gender'])[i],
                            'size':list(df['amount'])[i]}
                Ohio.append(oh_entry)
                break
            if (df['state'])[i] == 'OK' and (df['gender'])[i] == 'M':
                ok_entry = {'name':list(df['name'])[i],
                            'gender':list(df['gender'])[i],
                            'size':list(df['amount'])[i]}
                Oklahoma.append(ok_entry)
                break
            if (df['state'])[i] == 'OR' and (df['gender'])[i] == 'M':
                or_entry = {'name':list(df['name'])[i],
                            'gender':list(df['gender'])[i],
                            'size':list(df['amount'])[i]}
                Oregon.append(or_entry)
                break
            if (df['state'])[i] == 'PA' and (df['gender'])[i] == 'M':
                pa_entry = {'name':list(df['name'])[i],
                            'gender':list(df['gender'])[i],
                            'size':list(df['amount'])[i]}
                Pennsylvania.append(pa_entry)
                break
            if (df['state'])[i] == 'RI' and (df['gender'])[i] == 'M':
                ri_entry = {'name':list(df['name'])[i],
                            'gender':list(df['gender'])[i],
                            'size':list(df['amount'])[i]}
                Rhode_Island.append(ri_entry)
                break
            if (df['state'])[i] == 'SC' and (df['gender'])[i] == 'M':
                sc_entry = {'name':list(df['name'])[i],
                            'gender':list(df['gender'])[i],
                            'size':list(df['amount'])[i]}
                South_Carolina.append(sc_entry)
                break
            if (df['state'])[i] == 'SD' and (df['gender'])[i] == 'M':
                sd_entry = {'name':list(df['name'])[i],
                            'gender':list(df['gender'])[i],
                            'size':list(df['amount'])[i]}
                South_Dakota.append(sd_entry)
                break
            if (df['state'])[i] == 'TN' and (df['gender'])[i] == 'M':
                tn_entry = {'name':list(df['name'])[i],
                            'gender':list(df['gender'])[i],
                            'size':list(df['amount'])[i]}
                Tennessee.append(tn_entry)
                break
            if (df['state'])[i] == 'TX' and (df['gender'])[i] == 'M':
                tx_entry = {'name':list(df['name'])[i],
                            'gender':list(df['gender'])[i],
                            'size':list(df['amount'])[i]}
                Texas.append(tx_entry)
                break
            if (df['state'])[i] == 'UT' and (df['gender'])[i] == 'M':
                ut_entry = {'name':list(df['name'])[i],
                            'gender':list(df['gender'])[i],
                            'size':list(df['amount'])[i]}
                Utah.append(ut_entry)
                break
            if (df['state'])[i] == 'VT' and (df['gender'])[i] == 'M':
                vt_entry = {'name':list(df['name'])[i],
                            'gender':list(df['gender'])[i],
                            'size':list(df['amount'])[i]}
                Vermont.append(vt_entry)
                break
            if (df['state'])[i] == 'VA' and (df['gender'])[i] == 'M':
                va_entry = {'name':list(df['name'])[i],
                            'gender':list(df['gender'])[i],
                            'size':list(df['amount'])[i]}
                Virginia.append(va_entry)
                break
            if (df['state'])[i] == 'WA' and (df['gender'])[i] == 'M':
                wa_entry = {'name':list(df['name'])[i],
                            'gender':list(df['gender'])[i],
                            'size':list(df['amount'])[i]}
                Washington.append(wa_entry)
                break
            if (df['state'])[i] == 'WV' and (df['gender'])[i] == 'M':
                wv_entry = {'name':list(df['name'])[i],
                            'gender':list(df['gender'])[i],
                            'size':list(df['amount'])[i]}
                West_Virginia.append(wv_entry)
                break
            if (df['state'])[i] == 'WI' and (df['gender'])[i] == 'M':
                wi_entry = {'name':list(df['name'])[i],
                            'gender':list(df['gender'])[i],
                            'size':list(df['amount'])[i]}
                Wisconsin.append(wi_entry)
                break
            if (df['state'])[i] == 'WY' and (df['gender'])[i] == 'M':
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