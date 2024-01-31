import streamlit as st
import pytz
from datetime import datetime

# Function to get current time for a given timezone
def get_time(zone):
    tz = pytz.timezone(zone)
    return datetime.now(tz).strftime('%Y-%m-%d %H:%M:%S')

# Streamlit UI
st.title('World Clock')

# Dropdown menu for selecting locations
locations = st.multiselect('Select Locations', pytz.all_timezones, default=['UTC'])

# Displaying the time for selected locations
for loc in locations[:4]:  # Limiting to up to 4 locations
    st.write(f"{loc}: {get_time(loc)}")

# Updating the time every second
st_autorefresh = st.empty()  # Placeholder for autorefresh feature