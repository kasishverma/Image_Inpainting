import numpy as np
import  pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import re
import json
import plotly.express as px
import plotly.graph_objects as go
import plotly
from plotly.subplots import make_subplots
import babel.numbers
import geopandas as gpd
import country_converter as coco
from pycountry_convert import country_alpha2_to_country_name, country_name_to_country_alpha3

import streamlit as stre

#import plotly.graph_objs as go
#import plotly.express as px
from streamlit_echarts import st_echarts
import streamlit.components.v1 as components

df_2 = pd.read_json(r'\\rbsres01\shareddata\rassre\AIMLData\TNTR\TNTR_trade_prodprl_sample_data_k.json\TNTR_trade_prodprl_sample_data_k.json')
df_21 = pd.json_normalize(df_2.id)
df_22 = pd.json_normalize(df_2.lifetime)
df_23 = pd.json_normalize(df_2.document)
dff = pd.concat([df_21,df_22,df_23], axis=1)
pd.set_option('display.max_columns',37)
#dff['nonReportableData.tntrReceivedTimestamp'] = dff['nonReportableData.tntrReceivedTimestamp'].astype(str)
#print(dff.shape)
# Extract the date part and store it in a new column named 'date'
#dff['date'] = dff['nonReportableData.tntrReceivedTimestamp'].apply(lambda x: x.split('T')[0])
#dff["date"] = pd.to_datetime(dff["date"])
dff["transactionReportingStatus.stateTransitionDateTime"].sort_values(ascending = False)
dff.reset_index(inplace = True)
df_usermap = pd.read_excel(r'\\rbsres01\shareddata\rassre\AIMLData\TNTR\Ignite-TnTR-Users.xlsx')
#df_usermap['NAME'] = df_usermap['NAME'].apply(lambda x: x.split('TnTR')[0])
#df_usermap.head()
def namemap(x):
    try:
        return x + '-' + list(df_usermap[df_usermap['USER_RACF_ID'].str.contains(x, case=False)]['Role_Name'])[0]
    except:
        return x
dff['exceptionManagement.lastActionUser'] = dff['exceptionManagement.lastActionUser'].apply(namemap)
dff_ft = dff
dff['exceptionManagement.lastActionUser'].fillna('NULL',inplace = True)
st= []
for i in range(0,dff.shape[0]):
    if dff['exceptionManagement.lastActionUser'][i]=='NULL':
        st.append('STP')
    else:
        st.append('NON_STP')
dff['STP_NON_STP'] = st
dff_c = dff
dff_cn = dff_c[dff_c.STP_NON_STP=='NON_STP']
dff_cs = dff_c[dff_c.STP_NON_STP=='STP']
dff_cs = dff_cs.loc[dff_cs.groupby('subjectIdentifier.transactionId')['version'].idxmax()]
dff_cn = dff_cn.loc[dff_cn.groupby('subjectIdentifier.transactionId')['version'].idxmax()]
dff_f = pd.concat([dff_cn,dff_cs],axis= 0)
dff_colorbar = pd.DataFrame()
dff_colorbar = pd.concat([dff_colorbar,dff.STP_NON_STP.value_counts()],ignore_index = True)
dff_colorbar = pd.concat([dff_colorbar,dff_f.STP_NON_STP.value_counts()],ignore_index = True)

#dff_colorbar = dff_colorbar.append(dff.STP_NON_STP.value_counts(),ignore_index = True)
#dff_colorbar = dff_colorbar.append(dff_f.STP_NON_STP.value_counts(),ignore_index = True)
dff_colorbar = dff_colorbar.rename(index={0:'Transactions_All_Versions', 1:'Unique_Transactions'})

# dff_colorbar['STP']=dff_colorbar['STP'].divide(sum(list(dff_colorbar['STP'])))*100
# dff_colorbar['NON_STP']=dff_colorbar['NON_STP'].divide(sum(list(dff_colorbar['NON_STP'])))*100
dff_colorbar.loc['Transactions_All_Versions_percent'] = dff_colorbar.loc['Transactions_All_Versions'].divide(sum(list(dff_colorbar.loc['Transactions_All_Versions'])))*100
dff_colorbar.loc['Unique_Transactions_percent'] = dff_colorbar.loc['Unique_Transactions'].divide(sum(list(dff_colorbar.loc['Unique_Transactions'])))*100

#dff['month'] = pd.to_datetime(dff['nonReportableData.tntrReceivedTimestamp'],dayfirst = True).dt.month_name()
dff['date'] = pd.to_datetime(dff['nonReportableData.tntrReceivedTimestamp'],dayfirst = True).dt.date
dff['day'] = pd.to_datetime(dff['nonReportableData.tntrReceivedTimestamp'],dayfirst = True).dt.day_name()
dff_vol = dff[dff['day']!='Saturday']
dff_vol = dff[dff['day']!='Sunday']
#dff_vol=dff_f
#dff_vol = dff.query("day!='Saturday' and day!='Sunday'")
#dff_f_vol = dff_f.copy()
#dff_f['month'] = pd.to_datetime(dff_f['nonReportableData.tntrReceivedTimestamp'],dayfirst = True).dt.month_name()
dff_f['date'] = pd.to_datetime(dff_f['nonReportableData.tntrReceivedTimestamp'],dayfirst = True).dt.date
dff_f['day'] = pd.to_datetime(dff_f['nonReportableData.tntrReceivedTimestamp'],dayfirst = True).dt.day_name()
dff_f_vol = dff_f[dff_f['day']!='Saturday']
dff_f_vol = dff_f[dff_f['day']!='Sunday']
#dff_f_vol = dff_f_vol.query("day!='Saturday' and day!='Sunday'")
print('dff_f',dff_f.shape)
print('dff',dff.shape)
#print('dff_f',dff_f.shape)
print('dff_f_vol',dff_f_vol.shape)
print('dff_vol',dff_vol.shape)
print(dff_vol.date.value_counts())
print(dff_f_vol.date.value_counts())
print(dff_f_vol.day.value_counts())


fig_1 = go.Figure()
fig_1.add_trace(go.Scatter(x=dff_vol.date.value_counts().index.sort_values(), y = dff_vol.date.value_counts().sort_index(),
                    mode='lines+markers',
                    name='Transaction All Versions'))
fig_1.add_trace(go.Scatter(x=dff_f_vol.date.value_counts().index.sort_values(), y = dff_f_vol.date.value_counts().sort_index(),
                    mode='lines+markers',
                    name='Unique Transactions'))
fig_1.update_layout(
    title="System Processing Volumes",title_x=0.4
)
#fig_1.show()
stre.plotly_chart(fig_1, use_container_width=True, height=300)

