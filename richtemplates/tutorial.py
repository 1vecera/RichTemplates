#%%
import numpy as np  # Import numpy

data = np.random.randn(50)


#%% MATPLOT LIB EXAMPLE
from matplotlib import pyplot as plt  # Import matplotlib

plt.style.use('richview.mplstyle')  # Use the richview style
# Generate some random data
plt.plot(data)  # Plot the data
#%% PLOTLY EXAMPLE
import plotly.io as io  # Import plotly io so we can set the template
from plotly_theme import generate_RichView_plotly_theme  # Import the richview theme

io.templates['richview'] = generate_RichView_plotly_theme()  # Generate the richview template
io.templates.default = 'richview'  # Set the default template to richview

import plotly.express as px  # Import plotly express

px.line(data)  # Plot the data

#%% ALTAIR EXAMPLE
from altair_theme import RichView_Theme  # Import the richview theme

import altair as alt  # Import altair

alt.themes.register('richview', RichView_Theme)  # Register the richview theme
alt.themes.enable('richview')  # Enable the richview theme

import pandas as pd  # Import pandas

df = pd.Series(data).rename('data').to_frame()  # Convert the data to a dataframe
base = alt.Chart(df).mark_line().encode(y='data', x='data').interactive()  # Create the base chart
base