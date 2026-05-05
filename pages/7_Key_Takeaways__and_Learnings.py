# -------------------------
# Import libraries
# -------------------------
import streamlit as st
import pandas as pd
import geopandas as gpd
import json
import plotly.express as px
import plotly.io as pio

from data_loader import load_dvf, load_rent

# -------------------------
# Global plot style
# -------------------------
pio.templates.default = "plotly_white"

# -------------------------
# Page config
# -------------------------
st.set_page_config(
    page_title="Key Takeaways and Lessons Learned",
    page_icon=":bulb:",
    layout="wide",
)

# -------------------------
# Header
# -------------------------
st.title("Key Takeaways and Learnings")
st.caption(
    "In this final section, we summarize our key analytical findings and lessons learned from the project."
)

# -------------------------
#  Conclusions of the analysis
# -------------------------
st.markdown("---") 

st.header("Key Takeaways from the Data")
st.markdown("...")

# -------------------------
#  Assessment of goal achievement
# -------------------------
st.markdown("---") 

st.header("Did we achieve our project objectives?")
st.markdown("""
We laid the technical foundation for monitoring property values and rent control data, achieving most of our objectives:   

* :white_check_mark:  A robust database schema

* :white_check_mark:  Analytical visualisations tracking key metrics and patterns

* :toolbox:  An efficient ETL pipeline...
""")

# -------------------------
#  Challenges and Lessons Learned
# -------------------------
st.markdown("---") 


st.markdown("""


**Manual Uploads Slow Pipeline and Increase Risk of Error**	

* :toolbox:  The main weakness of our ETL pipeline is the manual uploads involved at multiple steps in the pipeline. 

* :white_check_mark:  To ensure consistency, there are checkpoints along the way were necessary data uploads are flagged.

* :bulb:  Looking forward, one solution would be to integrate the entire pipeline into Snowflake (which was not possible with a trial account).


**Joining Geographic Data**

* :toolbox:  One significant challenge we faced is how to integrate geographic data into our schema. Since the relationships between variables are spacial, a traditional primary key / foreign key relationship isn't applicable.

* :white_check_mark:  Since the scope of our project didn't require a full geospatial schema, our hybrid star model sufficed.

* :bulb:  Looking forward, if the further development of a geospatial layer is key aspect of the analysis, working with PostgreSQL and PostGIS would be a more suitable option.

""")

# -------------------------
#  Challenges and Lessons Learned
# -------------------------

st.header("Challenges and Lessons Learned")

r1c1, r1c2 = st.columns(2)
r2c1, r2c2 = st.columns(2)

with r1c1:
    st.markdown(
        """
        <div style="border:1px solid #e5e7eb; border-radius:8px; padding:16px;">
        <strong>Manual Uploads Slow Pipeline and Increase Risk of Error</strong><br>
        <span style="color:#6b7280; font-size:0.9rem;">
        * :toolbox:  The main weakness of our ETL pipeline is the manual uploads involved at multiple steps in the pipeline. 
        * :white_check_mark:  To ensure consistency, there are checkpoints along the way were necessary data uploads are flagged.
        * :bulb:  Looking forward, one solution would be to integrate the entire pipeline into Snowflake (which was not possible with a trial account).

        </span>
        </div>
        """, unsafe_allow_html=True,
    )
with r1c2:
    st.markdown(
        """
        <div style="border:1px solid #e5e7eb; border-radius:8px; padding:16px;">
        <strong>Joining Geographic Data</strong><br>
        <span style="color:#6b7280; font-size:0.9rem;">
        From 3NF to Star Schema — schema design decisions, the full ER diagram, and key
        trade-offs made for analytical usability.
        </span>
        </div>
        """, unsafe_allow_html=True,
    )
with r2c1:
    st.markdown(
        """
        <div style="border:1px solid #e5e7eb; border-radius:8px; padding:16px; margin-top:12px;">
        <strong>ETL / ELT Pipeline</strong><br>
        <span style="color:#6b7280; font-size:0.9rem;">
        End-to-end pipeline from raw CSVs to a Snowflake Star Schema — extraction, transformation,
        loading, and lessons learned.
        </span>
        </div>
        """, unsafe_allow_html=True,
    )
with r2c2:
    st.markdown(
        """
        <div style="border:1px solid #e5e7eb; border-radius:8px; padding:16px; margin-top:12px;">
        <strong>Analysis</strong><br>
        <span style="color:#6b7280; font-size:0.9rem;">
        Interactive map of sale prices and rent-control zones. Price distributions, arrondissement
        comparisons, and green-space relationships.
        </span>
        </div>
        """, unsafe_allow_html=True,
    )
