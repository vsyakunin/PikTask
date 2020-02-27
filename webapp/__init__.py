from flask import Flask, request, jsonify
from webapp.stations import hh_stations 

def create_app():
    app=Flask(__name__)

    @app.route('/api/v1/metro/verificate', methods=['POST'])
    def verificate_station():
        stations_to_verify=[]
        unchanged=[]
        updated=[]
        deleted=[]
        verification_result={}

        stations_input=request.json
        for station in stations_input:
            stations_to_verify.append(station)
        
        old_stations=hh_stations()

        for station in stations_to_verify:
            if station in old_stations:
                unchanged.append(station)
            else:
                updated.append(station)

        deleted=list(set(old_stations)-set(unchanged))

        verification_result["unchanged"]=unchanged
        verification_result["updated"]=updated
        verification_result["deleted"]=deleted

        return jsonify(verification_result)

    return app
