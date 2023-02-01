from flask import Flask, request

def merit_order(data: dict) -> list:
    """
        This function decides which powerplants to activate according to the merit-order
        
        -----------------------------------------------------------------------

        input: data = dictionnary of the recieved request on the /productionplan endpoint of the REST API

        -----------------------------------------------------------------------

        output: activated_plants = list of dictionnaries; each dictionnary contains the name of the powerplant and the power that the powerplant should deliver (multiple of 0.1)
    """

    # First, we retreive load, fuels and powerplants
    load, fuels, powerplants = [data[key] for key in data.keys()]

    powerplant_fuels_map = {'gasfired': fuels['gas(euro/MWh)'],
                            'turbojet': fuels['kerosine(euro/MWh)'],
                            'windturbine': 0}

    # Then, we sort powerplants based on merit order
    powerplants = sorted(powerplants, key=lambda plant: powerplant_fuels_map[plant['type']])

    # We initialize the total generated power and the activated powerplants list
    total_generated = 0
    activated_plants = []

    for plant in powerplants:

        # If wind turbine
        if plant['type'] == 'windturbine':

            # If the plant is a wind turbine, we compute the generated power based on the wind percentage and we check if the generated power is enough to meet load
            generated = plant['pmax'] * fuels['wind(%)'] / 100
            too_much_energy = total_generated + generated >= load
            generated = load - total_generated if too_much_energy else generated
            
            # We add the plant to the list, and we don't forget to set the 'p' parameter with a precision of 0.1
            activated_plants.append({'name': plant['name'], 'p': int(generated * 10) / 10.0})
            
            if too_much_energy:
                break

        
        # For the other cases
        else:

            too_much_energy = total_generated + plant['pmax'] >= load

            # If the plant is gas-fired or turbojet type, we check if switching on the plant will meet the load or not
            generated = load - total_generated if too_much_energy else plant['pmin']
            
            # We add the plant to the list, and we don't forget to set the 'p' parameter with a precision of 0.1
            activated_plants.append({'name': plant['name'], 'p': int(generated * 10) / 10.0})

            if too_much_energy:
                break
        
        # Also, let's not forget to update what we have generated so far
        total_generated += generated

    # Finally, we add the powerplants that has not been activated and set their power to 0
    if len(activated_plants) != len(powerplants):
        activated_plants += [{'name': plant['name'], 'p': 0.0} for plant in powerplants[len(activated_plants):]]


    return activated_plants


app = Flask(__name__)

@app.route('/productionplan', methods=['POST'])
def production_plan():

    print("Production plan received!")

    payload = request.get_json()
    return merit_order(payload)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='8888')