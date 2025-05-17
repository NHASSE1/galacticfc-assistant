
import streamlit as st
import pandas as pd

# Load player data
@st.cache_data
def load_data():
    return pd.read_csv("galactic_fc_players.csv")

df = load_data()

st.title("Galactic FC Virtual Assistant Coach")

# Sidebar filters
with st.sidebar:
    st.header("Filters")
    selected_unit = st.selectbox("Select Unit", ["All", "Goalkeeper", "Defender", "Midfielder", "Attacker"])
    available_sunday = st.checkbox("Available on Sunday Only", value=False)

# Filter data
filtered_df = df.copy()
if selected_unit != "All":
    filtered_df = filtered_df[filtered_df['Unit'] == selected_unit]
if available_sunday:
    filtered_df = filtered_df[filtered_df['Availability for Sunday Matches'].str.contains("Yes", case=False, na=False)]

# Display players
st.subheader(f"Player List ({selected_unit})")
st.dataframe(filtered_df)

# Grouped training groups
st.subheader("Training Groups")
for unit in ["Goalkeeper", "Defender", "Midfielder", "Attacker"]:
    unit_df = df[df['Unit'] == unit]
    st.markdown(f"**{unit}s**")
    st.dataframe(unit_df[['First Name', 'Last Name', 'Preferred Position', 'Availability for Training (Days & Times)']])

# Tactical suggestion (basic)
st.subheader("Drill Suggestion")
selected_focus = st.selectbox("Select Tactical Focus", ["3v2 Defending Transition", "1v1 Finishing", "5v2 Rondo", "Back 4 Shifting"])
if selected_focus:
    st.markdown(f"**Suggested Drill: {selected_focus}**")
    if selected_focus == "3v2 Defending Transition":
        st.markdown("- 3 Attackers vs 2 Defenders + GK")
        st.markdown("- Focus: Delaying attack, recovering shape, pressing triggers")
        st.markdown("- Outcome: Force wide, intercept, or reset possession")

st.markdown("---")
st.caption("Built by your Virtual Assistant Coach")
