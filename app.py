# Import Dependency
import datetime as dt 
import numpy as np
import pandas as pd

# Import SQLAlchemy dependencies
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session 
from sqlalchemy import create_engine, func 

# Import Flask dependencies 
from flask import Flask, jsonify 

# Set up our database engine for the Flask 
engine = create_engine("sqlite:///hawaii.sqlite")


# Reflect the database into our classes
Base = automap_base()
Base.prepare(engine, reflect=True)

# Save references to each table 
Measurement = Base.classes.measurement
Station = Base.classes.station 

# Create a session link from Python to database 
session = Session(engine)

# SET UP FLASK
# Reset flask app 
app = Flask(__name__)
   
# Create Flask Routes
@app.route("/")
def welcome():
    return(
    '''
    Welcome to the Climate Analysis API!.<br>   
    Available Routes: <br>
    /api/v1.0/precipitation <br>
    /api/v1.0/stations <br> 
    /api/v1.0/tobs <br> 
    /api/v1.0/temp/start/end
    ''')

# Create route to previous year precipitation:
@app.route("/api/v1.0/precipitation")
def precipitation():
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    precipitation = session.query(Measurement.date, Measurement.prcp).\
        filter(Measurement.date >=prev_year).all() 
    # Create a dictionary with the date as the key and 
    # precipitation as the value
    precip = {date: prcp for date, prcp in precipitation}
    return jsonify(precip)

# Create the stations route:
@app.route("/api/v1.0/stations")
def stations():
    results = session.query(Station.station).all()
    stations = list(np.ravel(results))
    return jsonify(stations=stations)

# Create the route temperature observations for the prev. year:
@app.route("/api/v1.0/tobs")
def temp_monthly():
    prev_year = dt.date(2017,8, 23) - dt.timedelta(days=365)
    results = session.query(Measurement.tobs).\
        filter(Measurement.station == 'USC00519281').\
        filter(Measurement.date >= prev_year).all()
    temps = list(np.ravel(results))
    return jsonify(temps=temps)


# Create the route for summary statistics
@app.route("/api/v1.0/temp/<start>")
@app.route("/api/v1.0/temp/<start>/<end>")
# add parameters to stats() function: a start parameter and an end parameter:
def stats(start=None, end=None):
    # select the minimum, average, and maximum teperature from our SQLite database
    sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]
    
    # add if-not statement to determine the starting date and ending date
    if not end:
        results = session.query(*sel).\
            filter(Measurement.date >= start).\
            filter(Measurement.date <= end).all()
        temps = list(np.ravel(results))
        return jsonify(temps)

    results = session.query(*sel).\
        filter(Measurement.date >= start).\
        filter(Measurement.date <= end).all()
    temps = list(np.ravel(results))
    return jsonify(temps=temps)
