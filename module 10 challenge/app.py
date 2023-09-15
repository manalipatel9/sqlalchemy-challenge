# Import the dependencies.
%matplotlib inline
from matplotlib import style
style.use('fivethirtyeight')
import matplotlib.pyplot as plt

import numpy as np
import pandas as pd
import datetime as dt

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

import flask
from flask import Flask, jsonify

#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
base=automap_base()
# reflect the tables
base.prepare(autoload_with=engine)

# Save references to each table
measurement= base.classes.measurement
station=base.classes.station

# Create our session (link) from Python to the DB
session=Session(engine)

#################################################
# Flask Setup
#################################################
app=Flask(_name_)

#################################################
# Flask Routes
#################################################
@app.route("/")
def home():
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        
@app.route("/api/v1.0/precipitation")
def precipitation():
        recent_date=session.query(measurement.date).order_by(measurement.date.desc()).first()
        year_ago=dt.date(2017,8,23)-dt.timedelta(days=365)
        prec_query = session.query(measurement.prcp ,measurement.date).filter(measurement.date>year_ago).order_by(measurement.date).all()
        return jsonify(dict(prec_query))
        
@app.route("/api/v1.0/stations")
def stations():
        num_stations=session.query(measurement.station).distinct().count()
 
@app.route("/api/v1.0/tobs")
    
