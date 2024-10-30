from tropycal import tracks, utils, rain
basin = tracks.TrackDataset(include_btk=True)

# Set up the threshold dictionary for minimum wind speed (this gets all hurricanes)
thresh = {'v_min': 73}

# Use filter_storms to get the data
# Setting return_keys=True to get ids 

houston_domain = {'north': 31.5, 'south': 27.0, 'west': -97.0, 'east': -93} #arbitray domain size for houston 

houston_storms = basin.filter_storms(
    storm=None,  # Search through all storms 
    year_range=(1999, 2024),  # Specify year range
    date_range=None,  # Include all dates within years
    thresh=thresh,  # Apply wind threshold 
    domain=houston_domain,  # Gulf of Mexico domain
    interpolate_data=False,  # Keep original 6-hourly data
    return_keys=True  # Return  keys
)

houston_storms

basin.plot_storms(houston_storms,domain = {'north': 36, 'south': 17, 'west': -100, 'east': -77})