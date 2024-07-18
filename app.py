import streamlit as st
import pandas as pd
from src.mushroom_model import predict_mushroom

observation = {
    'cap-diameter': [50],
    'stem-height': [20],
    'stem-width': [30],
    'has-ring': ['t'],
    'cap-shape': ['c']
}

###Widgets
has_ring = st.checkbox('The mushroom has a ring')
observation['has-ring'] = ['t'] if has_ring else ['f']

cap_shape = st.selectbox(
    'Mushroom Cap Shape',
    options=[
        'conical', 'bell', 'convex', 'flat',
        'sunken', 'spherical', 'others'
    ]
)

cap_shape_map = {
    'conical': 'c',
    'bell': 'b',
    'convex': 'x',
    'flat': 'f',
    'sunken': 's',
    'spherical': 'p',
    'others': 'o'
}
observation['cap-shape'] = [cap_shape_map[cap_shape]]

cap_diameter = st.number_input(
    "Cap diameter (cm)",
    min_value=0.38,
    max_value=62.34,
    value=50.0,
    help="Cap diameter from .38 to 62.34 cm"
)
observation['cap-diameter'] = [cap_diameter]

stem_height = st.number_input(
    "stem_height (cm)",
    min_value=0.00,
    max_value=33.92,
    value=20.0,
    help="stem_height from 0 to 33.92 cm"
)
observation['stem_height'] = [stem_height]

stem_width = st.number_input(
    "stem_width (mm)",
    min_value=0.00,
    max_value=103.91,
    value=30.0,
    help="stem_width from 0 to 103.91 mm"
)
observation['stem_width'] = [stem_width]


###Prediction

single_obs_df = pd.DataFrame(observation)


current_prediction = predict_mushroom(single_obs_df)

print(f"model results: {current_prediction}")
print(observation)

if current_prediction == 0:
    st.markdown('### 🍄🍄🍄 Mushroom is not poisonous')
else:
    st.markdown('###💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀')