from flask import Blueprint, render_template
import pandas as pd
import plotly
import plotly.express as px
import json

blueprint = Blueprint("plotly-test-page", __name__)

@blueprint.route("/plotly-test")
def index():
    # Students data available in a list of list
    students = [['Akash', 34, 'Sydney', 'Australia'],
                ['Rithika', 30, 'Coimbatore', 'India'],
                ['Priya', 31, 'Coimbatore', 'India'],
                ['Sandy', 32, 'Tokyo', 'Japan'],
                ['Praneeth', 16, 'New York', 'US'],
                ['Praveen', 17, 'Toronto', 'Canada']]
     
    # Convert list to dataframe and assign column values
    df = pd.DataFrame(students,
                      columns=['Name', 'Age', 'City', 'Country'],
                      index=['a', 'b', 'c', 'd', 'e', 'f'])
     
    # Create Bar chart
    fig = px.bar(df, x='Name', y='Age', color='City', barmode='group')
    # fig = px.bar(x=["a", "b", "c"], y=[1, 3, 2])
    figJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)    
    return render_template('plotly_test.html', figJSON=figJSON)