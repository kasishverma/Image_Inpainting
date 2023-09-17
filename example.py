import numpy as np
import pandas as pd
import cx_Oracle as sql
import streamlit as st
import plotly.graph_objs as go
from streamlit_echarts import st_echarts
from PIL import Image

import warnings
warnings.filterwarnings('ignore')

import cx_Oracle as sql

try:
    sql.init_oracle_client(lib_dir=r"C:\dev\instantclient_19_20")
except:
    print("SQL Client Already Initialised")

connection = sql.connect(user='GCRP_SM_RO', password='JanFebMarch2013',dsn=f"{'lonuc25301'}:{'1629'}/{'POLNGLA1'}")

st.set_page_config(page_title="Settlements Dashboard", page_icon=":bar_chart:",layout="wide")
st.markdown("<h2 style='text-align: center;'>Rates & Credit Settlements</h2>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center;'>Glacier (London) July-2023</h3>", unsafe_allow_html=True)
st.markdown('<style>div.block-container{padding-top:2rem;}</style>',unsafe_allow_html=True)

tab1, tab2 = st.tabs(["BUSINESS", "TECHNOLOGY"])


#SETTLEMENT OVERALL BOOKINGS
sett_ops = '''select *
from ioa_settlement
where SETTLEMENT_DATE >= to_date('01/07/2023','dd/mm/yyyy')
and SETTLEMENT_DATE <= to_date('31/07/2023','dd/mm/yyyy')''';

df_sett_ops_main = pd.read_sql(sett_ops, connection)
print(df_sett_ops_main.shape)

df_sett_ops = df_sett_ops_main.copy()

df_sett_ops = df_sett_ops.groupby(['SETTLEMENT_DATE','CREATED_BY']).size().reset_index().rename(columns = {0:'COUNT'})

df_sett_ops['day_name'] = df_sett_ops.SETTLEMENT_DATE.dt.day_name()
df_sett_ops = df_sett_ops[~df_sett_ops['day_name'].isin(['Sunday','Saturday'])]

print(df_sett_ops.shape)

#Creating DF for late bookings

df_late_book = df_sett_ops_main[df_sett_ops_main['CREATEDDATE'].dt.date>df_sett_ops_main['SETTLEMENT_DATE'].dt.date]
df_late_book = df_late_book.groupby(['SETTLEMENT_DATE']).size().reset_index().rename(columns = {0:'COUNT'})

print(df_late_book.shape)
colors = ['#CCE5FF', '#99CCFF', '#66B2FF','#3399FF', '#0080FF']
#AUDIT DATAFRAME
# sett = '''
#     select
#         *
#     from
#         aa$ioa_settlement
#     where
#         SETTLEMENT_DATE >= to_date('01/07/2023','dd/mm/yyyy') and
#         SETTLEMENT_DATE <= to_date('31/07/2023','dd/mm/yyyy')''';
#
# sett_audit = pd.read_sql(sett, connection)

print('loading csv file')

sett_audit = pd.read_csv(r'\\rbsres01\shareddata\rassre\AIMLData\Glacier\sett_audit.csv')
sett_audit['day_name'] = pd.to_datetime(sett_audit['SETTLEMENT_DATE']).dt.day_name()

#sett_audit['day_name'] = sett_audit.SETTLEMENT_DATE.dt.day_name()
sett_audit = sett_audit[~sett_audit['day_name'].isin(['Sunday','Saturday'])]

print(sett_audit.shape)

sys = ['glapp', 'ca_gpdp5', 'FPRPCLP']
user_list = sett_audit.UPDATED_BY.value_counts().index.to_list()
item_list = [e for e in user_list if e not in sys]

##Re-writing code for Label column]

# sett_audit['Label'] = ''
#
# for id in sett_audit['ID'].unique():
#     id_rows = sett_audit[sett_audit['ID'] == id]
#     if any(row['UPDATED_BY'] in item_list for _, row in id_rows.iterrows()):
#         sett_audit.loc[sett_audit['ID'] == id, 'Label'] = 'NON_STP'
#     else:
#         sett_audit.loc[sett_audit['ID'] == id, 'Label'] = 'STP'

#Defining Label column for STP & NON-STP Data

sys = ['glapp', 'ca_gpdp5', 'FPRPCLP']
df_user = pd.DataFrame(item_list).reset_index(drop = True).rename(columns={0:'UPDATED_BY'})
df_user['STP_NON_STP']  = 'NON_STP'
df_merge = pd.merge(sett_audit,df_user,on = 'UPDATED_BY',how = 'left')
df_merge['STP_NON_STP'].fillna(value = 'STP', inplace=True)
df_stage1 = df_merge.groupby(['ID','STP_NON_STP']).size()
df_stage1 = pd.DataFrame(df_stage1.reset_index())
df_stage2 = df_merge.groupby(['ID','STP_NON_STP']).size().groupby(['ID']).size().sort_values(ascending = False)
df_stage2 = pd.DataFrame(df_stage2).reset_index().rename(columns={0:'count'})
df_stage3 = pd.merge(df_stage2,df_stage1,on = 'ID',how = 'left')
df_stage4 = df_stage3[(df_stage3['count']==1) & (df_stage3['STP_NON_STP']=='NON_STP')]
df_stage4['count'].replace(to_replace=1, value='NON_STP', inplace = True)
df_stage5 = pd.merge(df_stage3,df_stage4,on = 'ID',how = 'left')
df_stage5['STP_NON_STP_y'][df_stage5['count_x'] == 2] = 'NON_STP'
df_stage5['STP_NON_STP_y'].fillna(value = 'STP',inplace = True)
df_stage5.drop(['count_x','STP_NON_STP_x','0_x','count_y','0_y'],axis=1,inplace=True)
df_stage5.drop_duplicates(inplace=True)
sett_audit = pd.merge(df_merge,df_stage5,on = 'ID',how = 'inner')
sett_audit.rename(columns={'STP_NON_STP_y':'Label'},inplace=True)

#STP NON STP DATAFRAME
sett_audit_dup = sett_audit.copy()
sett_audit_dup_rate = pd.DataFrame()

sett_audit_dup_rate['SETTLEMENT_DATE'] = sett_audit_dup[sett_audit_dup.Label=='STP'].drop_duplicates(subset = ['ID']).groupby(['SETTLEMENT_DATE'])['Label'].count().index
sett_audit_dup_rate['STP_COUNT'] = sett_audit_dup[sett_audit_dup.Label=='STP'].drop_duplicates(subset = ['ID']).groupby(['SETTLEMENT_DATE'])['Label'].count().values
sett_audit_dup_rate['NON_STP_COUNT'] = sett_audit_dup[sett_audit_dup.Label=='NON_STP'].drop_duplicates(subset = ['ID']).groupby(['SETTLEMENT_DATE'])['Label'].count().values

sett_curr = '''
        select 
            SETTLEMENT_DATE, 
            curr_iso_code, 
            count(*)
        from 
            ioa_settlement
        where 
            SETTLEMENT_DATE >= to_date('01/07/2023','dd/mm/yyyy') and 
            SETTLEMENT_DATE <= to_date('31/07/2023','dd/mm/yyyy') and 
            wqty_code_current not like ('%DeletedWFQueue%')
        group by 
            SETTLEMENT_DATE,
            curr_iso_code
        order by 
            1,2 asc''';

df_sett_curr = pd.read_sql(sett_curr, connection)
df_sett_curr['day_name'] = df_sett_curr.SETTLEMENT_DATE.dt.day_name()
df_sett_curr = df_sett_curr[~df_sett_curr['day_name'].isin(['Sunday', 'Saturday'])]
df_sett_curr.rename(columns={'COUNT(*)': 'COUNT'}, inplace=True)

labels = list(df_sett_curr['CURR_ISO_CODE'].value_counts().sort_index(ascending=True).index)
values = list(df_sett_curr.groupby(['CURR_ISO_CODE'])['COUNT'].sum())

stp_rate = []
for i in range(0, sett_audit_dup_rate.shape[0]):
    stp_rate.append(((sett_audit_dup_rate.STP_COUNT[i] / (
                sett_audit_dup_rate.STP_COUNT[i] + sett_audit_dup_rate.NON_STP_COUNT[i])) * 100).round(2))
sett_audit_dup_rate['STP_RATE'] = stp_rate
mean_stp = np.mean(sett_audit_dup_rate.STP_RATE).round(2)

df_sett_excp = sett_audit[sett_audit['WQTY_CODE_CURRENT'].str.contains('Ex', case=True)]

df_sett_excp['day_name'] = pd.to_datetime(df_sett_excp['SETTLEMENT_DATE']).dt.day_name()
#df_sett_excp['day_name'] = df_sett_excp.SETTLEMENT_DATE.dt.day_name()
df_sett_excp = df_sett_excp[~df_sett_excp['day_name'].isin(['Sunday', 'Saturday'])]

df_sett_excp_count = df_sett_excp.groupby(['SETTLEMENT_DATE', 'WQTY_CODE_CURRENT']).size().reset_index().rename(
        columns={0: 'COUNT'})

df_sett_excp.reset_index(inplace=True)
user_top = df_sett_excp[~df_sett_excp.UPDATED_BY.isin(sys)]['UPDATED_BY'].value_counts()[:15].index.to_list()
l1 = []
for i in range(0, df_sett_excp.shape[0]):
    if df_sett_excp.UPDATED_BY[i] in user_top:
        l1.append(df_sett_excp.UPDATED_BY[i])
    elif df_sett_excp.UPDATED_BY[i] in sys:
        l1.append('SYSTEM')
    else:
        l1.append('OTHER')
df_sett_excp['USER'] = l1

df_late_book['day_name'] = df_late_book.SETTLEMENT_DATE.dt.day_name()
df_late_book = df_late_book[~df_late_book['day_name'].isin(['Sunday', 'Saturday'])]
print(df_late_book.shape)

query10 = '''select v1.CCY, round(sum(v1.AMOUNT),2) as BASE_CCY_AMOUNT, round(sum(v1.GBP_EQUIVALENT),2) AS GBP_AMOUNT 
from 
(select ios.curr_iso_code ccy, ios.amount, ios.amount*(1/e.MID_SPOT_RATE) GBP_Equivalent from ioa_settlement ios, ioa_exchange_rate e
where 
ios.settlement_date between '01-Jul-2023'and '31-Jul-2023' 
and ios.wqty_code_current = 'SettlementCompletedWFQueue'
and ios.curr_iso_code=e.curr_iso_code_to 
and e.curr_iso_code_from='GBP'
and amount < 0 
union
select ios.curr_iso_code ccy, ios.amount, ios.amount*e.MID_SPOT_RATE GBP_Equivalent from ioa_settlement ios, ioa_exchange_rate e
where 
ios.settlement_date between '01-Jul-2023'and '31-Jul-2023' 
and ios.wqty_code_current = 'SettlementCompletedWFQueue'
and ios.curr_iso_code=e.curr_iso_code_from 
and e.curr_iso_code_to='GBP'
and amount < 0 
union
select ios.curr_iso_code ccy, ios.amount, ios.amount GBP_Equivalent from ioa_settlement ios, ioa_exchange_rate e
where 
ios.settlement_date between '01-Jul-2023'and '31-Jul-2023' 
and ios.wqty_code_current = 'SettlementCompletedWFQueue'
and ios.curr_iso_code='GBP' 
and amount < 0 ) v1
group by v1.CCY''';

df10 = pd.read_sql(query10,connection)

query11 = '''select v1.CCY, round(sum(v1.AMOUNT),2) as BASE_CCY_AMOUNT, round(sum(v1.GBP_EQUIVALENT),2) AS GBP_AMOUNT 
from 
(select ios.curr_iso_code ccy, ios.amount, ios.amount*(1/e.MID_SPOT_RATE) GBP_Equivalent from ioa_settlement ios, ioa_exchange_rate e
where 
ios.settlement_date between '01-Jul-2023'and '31-Jul-2023' 
and ios.wqty_code_current = 'SettlementCompletedWFQueue'
and ios.curr_iso_code=e.curr_iso_code_to 
and e.curr_iso_code_from='GBP'
and amount > 0 
union
select ios.curr_iso_code ccy, ios.amount, ios.amount*e.MID_SPOT_RATE GBP_Equivalent from ioa_settlement ios, ioa_exchange_rate e
where 
ios.settlement_date between '01-Jul-2023'and '31-Jul-2023' 
and ios.wqty_code_current = 'SettlementCompletedWFQueue'
and ios.curr_iso_code=e.curr_iso_code_from 
and e.curr_iso_code_to='GBP'
and amount > 0 
union
select ios.curr_iso_code ccy, ios.amount, ios.amount GBP_Equivalent from ioa_settlement ios, ioa_exchange_rate e
where 
ios.settlement_date between '01-Jul-2023'and '31-Jul-2023' 
and ios.wqty_code_current = 'SettlementCompletedWFQueue'
and ios.curr_iso_code='GBP' 
and amount > 0 ) v1
group by v1.CCY''';

df11 = pd.read_sql(query11,connection)

#df12 = pd.read_sql(query12,connection)
#df12n = df12[df12.CPTY_INTERNALFLAG=='N']
df12 = pd.read_csv(r'\\rbsres01\shareddata\rassre\AIMLData\Glacier\ioa_settlement')
df12n = df12[df12.CPTY_INTERNALFLAG=='N']

df12n = df12n[(df12n['LONG_NAME'].str.contains('LCH', case=False)==False)
& (df12n['LONG_NAME'].str.contains('EUREX', case=False)==False)
& (df12n['LONG_NAME'].str.contains('CLEAR STREAM', case=False)==False)
& (df12n['LONG_NAME'].str.contains('CLEARSTREAM', case=False)==False)
& (df12n['LONG_NAME'].str.contains('ICE LINK', case=False)==False)
& (df12n['LONG_NAME'].str.contains('ICELINK', case=False)==False)]



with tab1:
   col1, col2, col3 = st.columns((3))
   System = df_sett_ops[df_sett_ops['CREATED_BY'].isin(sys)].groupby('SETTLEMENT_DATE')['COUNT'].sum().sum()
   User = df_sett_ops[~df_sett_ops['CREATED_BY'].isin(sys)].groupby('SETTLEMENT_DATE')['COUNT'].sum().sum()
   with col1:
        st.markdown("<h5 style='text-align: center;'>STP RATE</h5>", unsafe_allow_html=True)
        #st.subheader('STP RATE')
        st.markdown("\n")
        st.markdown("\n")
        st.markdown("\n")
        st.markdown("\n")
        option = {
            "tooltip": {
                "formatter": '{a} <br/>{b} : {c}%'
            },
            "series": [{
                "name": 'STP RATE',
                "type": 'gauge',
                "startAngle": 180,
                "endAngle": 0,
                "progress": {
                    "show": "true"
                },
                "radius": '100%',
                #"center": ['80%', '40%'],

                "itemStyle": {
                    "color": '#58D9F9',
                    "shadowColor": 'rgba(0,138,255,0.45)',
                    "shadowBlur": 10,
                    "shadowOffsetX": 2,
                    "shadowOffsetY": 2,
                    "radius": '55%',
                },
                "progress": {
                    "show": "true",
                    "roundCap": "true",
                    "width": 15
                },
                "pointer": {
                    "length": '55%',
                    "width": 8,
                    "offsetCenter": [0, '-5%']
                },
                "detail": {
                    "valueAnimation": "true",
                    "formatter": '{value}%',
                    "backgroundColor": '#58D9F9',
                    "borderColor": '#999',
                    "borderWidth": 4,
                    "width": '70%',
                    "lineHeight": 20,
                    "height": 30,
                    "borderRadius": 188,
                    "offsetCenter": [0, '50%'],
                    "valueAnimation": "true",
                },
                "data": [{
                    "value": mean_stp,
                    #"name": 'STP RATE'
                }]
            }]
        };

        st_echarts(options=option, key="1")
        # fig.show()
        # st.metric(label='',value=f"{df_sett_ops.groupby('SETTLEMENT_DATE')['COUNT'].sum().sum():,.0f}")
        # st.info('STP RATE')
        # st.metric(label="", value=f"{mean_stp}%")

   with col2:
        st.markdown("<h5 style='text-align: center;'>Total Trade Volume</h5>", unsafe_allow_html=True)
        fig0 = go.Figure()
        fig0.add_trace(go.Scatter(x=df_sett_ops.groupby('SETTLEMENT_DATE')['COUNT'].sum().index,
                                  y=df_sett_ops.groupby('SETTLEMENT_DATE')['COUNT'].sum().values,
                                  mode='lines+markers',
                                  line_color="orange"))              # name='OVERALL BOOKINGS
        fig0.update_layout(
            xaxis_title="Date", yaxis_title="COUNT"
        )
        st.plotly_chart(fig0, use_container_width=True, height=300)
    #
        # st.subheader("Settlements Per Currency by Volume")
        # fig5 = go.Figure(data=[go.Pie(labels=labels, values=values, rotation=250,hole = 0.5,text = labels)])
        # fig5.update_layout(
        #     # title='CURRENCY OF SETTLEMENTS',
        #     template="ggplot2",
        #     uniformtext_minsize=11, uniformtext_mode='hide', showlegend=False
        #     # textinfo = 'text',
        # )
        # fig5.update_layout(height=600)
        # st.plotly_chart(fig5, use_container_width=True, height=300)
   with col3:
        st.markdown("<h5 style='text-align: center;'>Settlement Bookings (System vs Manual)</h5>", unsafe_allow_html=True)
        fig = go.Figure(data=[
            go.Pie(labels=['System', 'User'], values=[System, User], pull=[0, 0.1, 0.2, 0, ], hole=0.5, rotation=45,
                   marker=dict(colors=colors))])
        fig.update_layout(height=450, margin=dict(l=10, r=10, t=50, b=10, pad=8),
                           legend=dict(font=dict(family="Courier", size=12), ),
                           legend_title=dict(font=dict(family="Courier", size=30)))  # paper_bgcolor="lightgrey"
        fig.update_layout(legend=dict(
            orientation="h",
            yanchor="middle",
            y=-15,
            xanchor="auto",
            x=0.5
        ))
        st.plotly_chart(fig, use_container_width=True, height=300)

        # fig0 = go.Figure()
        # fig0.add_trace(go.Scatter(x=df_sett_ops.groupby('SETTLEMENT_DATE')['COUNT'].sum().index,
        #                           y=df_sett_ops.groupby('SETTLEMENT_DATE')['COUNT'].sum().values,
        #                           mode='lines+markers',
        #                           line_color="orange", name='OVERALL BOOKINGS'))
        # fig0.update_layout(
        #     xaxis_title="Date", yaxis_title="COUNT"
        # )
        # st.plotly_chart(fig0, use_container_width=True, height=200)
   st.divider()
   rc2,rc3,rc4 = st.columns((3))
   with rc2:
        st.markdown("<h5 style='text-align: center;'>Late Bookings</h5>", unsafe_allow_html=True)
        fig6 = go.Figure()
        fig6.add_trace(go.Scatter(x=df_late_book.SETTLEMENT_DATE, y=df_late_book['COUNT'],
                                  mode='lines+markers',
                                  line_color="orange"))
        # fig.add_trace(go.Scatter(y = np.mean(sett_audit_dup_rate.STP_RATE).round(2),
        #                     mode='lines',
        #                     name='Unique Transactions'))
        mean1 = np.mean(df_late_book['COUNT']).round(2)
        # np.mean(sett_audit_dup_rate.STP_RATE).round(2)
        fig6.add_hline(y=np.mean(df_late_book['COUNT']).round(2), line_width=3, line_dash="dash", line_color="green",
                       annotation_text=f"MEAN - {mean1}",

                       )

        fig6.update_layout(
        xaxis_title="Trade Date > Settlement Date", yaxis_title="Trade Count")

        st.plotly_chart(fig6, use_container_width=True, height=450)

   with rc3:
        st.markdown("<h5 style='text-align: center;'>Top 15 Counterparties by Trading Volume</h5>", unsafe_allow_html=True)
        st.markdown("\n")
        st.markdown("\n")
        st.markdown("\n")

        # st.subheader("Settlements Per Currency by Volume")
        fig12 = go.Figure(data=[go.Pie(labels=df12n.groupby('LONG_NAME').size().sort_values(ascending=False)[:15].index,
                                       values=df12n.groupby('LONG_NAME').size().sort_values(ascending=False)[
                                              :15].values, rotation=45, hole=0.5)])
        fig12.update_layout(
            # title='CURRENCY OF SETTLEMENTS',
            template="ggplot2",

            # hovertext = hovertext,
            uniformtext_minsize=11, uniformtext_mode='hide', showlegend=False,
            # textinfo = 'text',
        )

        fig12.update_traces( textfont_size=12,
                            hovertemplate='Counterparty : %{label}<br>Count : %{value}'
                            , name='')
        # fig5.update_traces()
         # st.plotly_chart(fig5, use_container_width=True, height=300)

        fig12.update_layout(height=400)
        fig12.update_layout(margin=dict(l=10, r=10, t=50, b=10, pad=8),
                           legend=dict(font=dict(family="Courier", size=12), ),
                           legend_title=dict(font=dict(family="Courier", size=30)))
        # fig5.update_layout(legend=dict(
        #     orientation="h",
        #     yanchor="middle",
        #     y=-15,
        #     xanchor="auto",
        #     x=0.9
        # ))

        st.plotly_chart(fig12, use_container_width=True, height=450)

   with rc4:
        st.markdown("<h5 style='text-align: center;'>User Workload Distribution</h5>", unsafe_allow_html=True)
        # st.markdown('### User Workload Distribution')
        fig4 = go.Figure()
        fig4.add_trace(go.Pie(labels=df_sett_excp[~df_sett_excp.UPDATED_BY.isin(sys)]['USER'].value_counts().index,
                              values=df_sett_excp[~df_sett_excp.UPDATED_BY.isin(sys)]['USER'].value_counts().values,
                              hole=0.5,
                              titlefont=dict(size=15),
                              titleposition="bottom center",
                               textfont_size=12,
                              rotation=-30,textposition = 'inside'))
        fig4.update_layout(height = 450,margin=dict(l=10, r=10, t=50, b=10, pad=8),
                           legend=dict(font=dict(family="Courier", size=12), ),
                           legend_title=dict(font=dict(family="Courier", size=30)))
        # fig4.update_layout(height = 450,legend=dict(
        #     orientation="h",
        #     yanchor="middle",
        #     y=-15,
        #     xanchor="auto",
        #     x=1
        # ))
        st.plotly_chart(fig4, use_container_width=True, height=450)

   st.divider()

   colun1,colun2,colun3 = st.columns((3))
   with colun1:
        st.markdown("<h5 style='text-align: center;'>Swift Payments</h5>", unsafe_allow_html=True)
        fig10 = go.Figure(data=[go.Pie(labels=df10.CCY, values=df10.GBP_AMOUNT.abs(), customdata=df10.BASE_CCY_AMOUNT.abs(), rotation=45,
                   hole=0.5)])
        fig10.update_layout(
            template="ggplot2",
            uniformtext_minsize=11, uniformtext_mode='hide'
        )
        fig10.update_traces(textposition='inside', textfont_size=12, text=df10.CCY, name='',
                            hovertemplate='Base_Ccy_Amt : %{label} %{customdata}<br>GBP_EQUIVALENT : £ %{value:.2f}'
                            )

        fig10.update_layout(height = 420,margin=dict(l=10, r=10, t=50, b=10, pad=8),
                            legend=dict(font=dict(family="Courier", size=12), ),
                            legend_title=dict(font=dict(family="Courier", size=30)))
        # fig10.update_layout(height = 450,legend=dict(
        #     orientation="h",
        #     yanchor="middle",
        #     y =-30,
        #     xanchor="right",
        #     x=1
        # ))
        st.plotly_chart(fig10, use_container_width=True)

   with colun2:
        st.markdown("<h5 style='text-align: center;'>Swift Receipts</h5>", unsafe_allow_html=True)
        pd.set_option('display.float_format', '{:.2f}'.format)
        fig11 = go.Figure(data=[
            go.Pie(labels=df11.CCY, values=df11.GBP_AMOUNT, customdata=df11.BASE_CCY_AMOUNT, rotation=45,
                   hole=0.5)])
        fig11.update_layout(
            template="ggplot2",
            uniformtext_minsize=11, uniformtext_mode='hide'
        )
        fig11.update_traces(textposition='inside', textfont_size=12, text=df11.CCY, name='',
                            hovertemplate='Base_Ccy_Amt : %{label} %{customdata}<br>GBP_EQUIVALENT : £ %{value:.2f}'
                            )


        fig11.update_layout(height= 420,margin=dict(l=10, r=10, t=50, b=10,pad = 8),
                           legend=dict(font=dict(family="Courier", size=12), ),
                           legend_title=dict(font=dict(family="Courier", size=30)))
        #fig11.update_layout(legend=dict(
        #      orientation="h",
        #      yanchor="auto",
        #      y=-1000,
        #      xanchor="auto",
        #      x=1
        # ))
        st.plotly_chart(fig11, use_container_width=True)

   with colun3:
        st.markdown("<h5 style='text-align: center;'>Settlement Vol by Currency</h5>", unsafe_allow_html=True)
        # st.subheader("Settlements Per Currency by Volume")
        fig5 = go.Figure(data=[go.Pie(labels=labels, values=values, rotation=250, hole=0.5, text=labels)])
        fig5.update_layout(
            # title='CURRENCY OF SETTLEMENTS',
            template="ggplot2",
            uniformtext_minsize=11, uniformtext_mode='hide'
            # textinfo = 'text',
        )
        fig5.update_traces(textposition='inside')
        fig5.update_layout(height=450)
        fig5.update_layout(margin=dict(l=10, r=10, t=50, b=10, pad=8),
                           legend=dict(font=dict(family="Courier", size=12), ),
                           legend_title=dict(font=dict(family="Courier", size=30)))
        # fig5.update_layout(legend=dict(
        #     orientation="h",
        #     yanchor="middle",
        #     y=-15,
        #     xanchor="auto",
        #     x=0.9
        # ))

        st.plotly_chart(fig5, use_container_width=True, height=450)

   st.divider()

    # with cl3:
    #     st.markdown("<h5 style='text-align: center;'>User Workload Distribution</h5>", unsafe_allow_html=True)
    #     #st.markdown('### User Workload Distribution')
    #     fig4 = go.Figure()
    #     fig4.add_trace(go.Pie(labels=df_sett_excp[~df_sett_excp.UPDATED_BY.isin(sys)]['USER'].value_counts().index,
    #                           values=df_sett_excp[~df_sett_excp.UPDATED_BY.isin(sys)]['USER'].value_counts().values,
    #                           hole=0.5,
    #                           titlefont=dict(size=15),
    #                           titleposition="bottom center",
    #                           hoverinfo='label+percent', textinfo='value', textfont_size=12,
    #                           rotation=-30))
    #     fig4.update_layout(margin=dict(l=10, r=10, t=50, b=10, pad=8),
    #                        legend=dict(font=dict(family="Courier", size=12), ),
    #                        legend_title=dict(font=dict(family="Courier", size=30)))
    #     fig4.update_layout(legend=dict(
    #         orientation="h",
    #         yanchor="middle",
    #         y=-15,
    #         xanchor="auto",
    #         x=0.9
    #     ))
    #     st.plotly_chart(fig4, use_container_width=True, height=500)

   print(df_sett_excp.shape)

    # LATE BOOKINGS
   print('EXECUTING LATE BOOKINGS')
    # late_book = '''select settlement_date, count(*)
    # from ioa_settlement
    # where trunc(SETTLEMENT_DATE) >= to_date('01/07/2023','dd/mm/yyyy')
    # and trunc(SETTLEMENT_DATE) <= to_date('31/07/2023','dd/mm/yyyy')
    # and trunc(createddate) > trunc(settlement_date)
    # group by SETTLEMENT_DATE
    # order by 1 asc ''';
    #
    # df_late_book = pd.read_sql(late_book, connection)

#PROCESS MAPS





with tab2:
    cl0, cl1, cl2 = st.columns((3))
    with cl0:
        st.markdown("<h5 style='text-align: center;'>Daily STP Rate %age</h5>", unsafe_allow_html=True)
        # st.subheader('Daily STP Rate %age')
        fig1 = go.Figure()
        fig1.add_trace(go.Scatter(x=sett_audit_dup_rate.SETTLEMENT_DATE, y=sett_audit_dup_rate.STP_RATE,
                                  mode='lines+markers',
                                  line_color="orange", text=sett_audit_dup_rate.STP_RATE))
        # fig.add_trace(go.Scatter(y = np.mean(sett_audit_dup_rate.STP_RATE).round(2),
        #                     mode='lines',
        #                     name='Unique Transactions'))

        fig1.add_hline(y=np.mean(sett_audit_dup_rate.STP_RATE).round(2), line_width=3, line_dash="dash",
                       line_color="green",
                       annotation_text=f"MEAN - {mean_stp}")

        fig1.update_layout(
            xaxis_title="Date", yaxis_title="Percentage"
        )
        st.plotly_chart(fig1, use_container_width=True, height=500)

    with cl1:
        st.markdown("<h5 style='text-align: center;'>Exception Categories</h5>", unsafe_allow_html=True)
        # st.markdown('### Exception Categories')
        fig2 = go.Figure()
        fig2.add_trace(go.Pie(labels=df_sett_excp['WQTY_CODE_CURRENT'].value_counts().index,
                              values=df_sett_excp['WQTY_CODE_CURRENT'].value_counts().values
                              ,
                              titlefont=dict(size=15),
                              titleposition="bottom center",
                              marker=dict(colors=colors),
                              hoverinfo='label+percent', textinfo='value', textfont_size=12,
                              rotation=90, hole=0.5))
        fig2.update_layout(height = 500,margin=dict(l=10, r=10, t=50, b=10, pad=8),
                           legend=dict(font=dict(family="Courier", size=12), ),
                           legend_title=dict(font=dict(family="Courier", size=30)))  # paper_bgcolor="lightgrey"
        fig2.update_layout(legend=dict(
            orientation="h",
            yanchor="middle",
            y=-15,
            xanchor="auto",
            x=0.9
        ))
        st.plotly_chart(fig2, use_container_width=True, height=500)

    with cl2:
        fig3 = go.Figure()
        st.markdown("<h5 style='text-align: center;'>Exceptions cleared by System & Users</h5>", unsafe_allow_html=True)
        # st.markdown('### ')
        fig3.add_trace(
            go.Pie(labels=df_sett_excp.USER.apply(lambda x: 'SYSTEM' if x == 'SYSTEM' else 'USER').value_counts().index,
                   values=df_sett_excp.USER.apply(lambda x: 'SYSTEM' if x == 'SYSTEM' else 'USER').value_counts().values
                   ,
                   titlefont=dict(size=15),
                   titleposition="bottom center",
                   hole=0.5,
                   hoverinfo='label+percent', textinfo='value', textfont_size=12,
                   rotation=90))
        fig3.update_layout(height = 400,margin=dict(l=10, r=10, t=50, b=10, pad=8),
                           legend=dict(font=dict(family="Courier", size=12), ),
                           legend_title=dict(font=dict(family="Courier", size=30)))
        fig3.update_layout(legend=dict(
            orientation="h",
            yanchor="auto",
            y=-15,
            xanchor="auto",
            x=0.5
        ))
        st.plotly_chart(fig3, use_container_width=True, height=500)
    st.divider()

    st.markdown("<h3 style='text-align: center,background-color:green;'>Process Maps</h3>", unsafe_allow_html=True)
    tabs1, tabs2 = st.tabs(["Settlement Workflows", "Settlement Exception Workflows"])
    with tabs1:
        @st.cache_data
        def load_image(image_path):
            return Image.open(image_path)


        images1_options1 = load_image(
            r'\\rbsres01\shareddata\rassre\AIMLData\Glacier\Glacier_Processmap\DraftSettlementWFQueue.png')
        images1_options2 = load_image(
            r'\\rbsres01\shareddata\rassre\AIMLData\Glacier\Glacier_Processmap\DraftSettlementWFQueuetime.png')
        images2_options1 = load_image(
            r'\\rbsres01\shareddata\rassre\AIMLData\Glacier\Glacier_Processmap\BrokerageDraftSettlementWFQueue.png')
        images2_options2 = load_image(
            r'\\rbsres01\shareddata\rassre\AIMLData\Glacier\Glacier_Processmap\BrokerageDraftSettlementWFQueuetime.png')
        images3_options1 = load_image(
            r'\\rbsres01\shareddata\rassre\AIMLData\Glacier\Glacier_Processmap\SettlementGeneratedUnknownWFQueue.png')
        images3_options2 = load_image(
            r'\\rbsres01\shareddata\rassre\AIMLData\Glacier\Glacier_Processmap\SettlementGeneratedUnknownWFQueue.png')
        images4_options1 = load_image(
            r'\\rbsres01\shareddata\rassre\AIMLData\Glacier\Glacier_Processmap\SettlementPrimaryAuthorisationWFQueue.png')
        images4_options2 = load_image(
            r'\\rbsres01\shareddata\rassre\AIMLData\Glacier\Glacier_Processmap\SettlementPrimaryAuthorisationWFQueuetime.png')
        images5_options1 = load_image(
            r'\\rbsres01\shareddata\rassre\AIMLData\Glacier\Glacier_Processmap\SettlementCompletedWFQueue.png')
        images5_options2 = load_image(
            r'\\rbsres01\shareddata\rassre\AIMLData\Glacier\Glacier_Processmap\SettlementCompletedWFQueuetime.png')


        #st.markdown("<h5>Settlement Workflows</h5>", unsafe_allow_html=True)
        selected_option = st.selectbox("", ['DraftSettlementWFQueue', 'BrokerageDraftSettlementWFQueue','SettlementGeneratedUnknownWFQueue',
                                            'SettlementPrimaryAuthorisationWFQueue','SettlementCompletedWFQueue'], index=0)

        # Define the paths to your images based on the selected option
        if selected_option == "DraftSettlementWFQueue":
            images1_path = images1_options1
            images2_path = images1_options2

        elif selected_option == "BrokerageDraftSettlementWFQueue":
            images1_path = images2_options1
            images2_path = images2_options2
        elif selected_option == "SettlementGeneratedUnknownWFQueue":
            images1_path = images3_options1
            images2_path = images3_options2
        elif selected_option == "SettlementPrimaryAuthorisationWFQueue":
            images1_path = images4_options1
            images2_path = images4_options2
        elif selected_option == "SettlementCompletedWFQueue":
            images1_path = images5_options1
            images2_path = images5_options2
        # elif selected_option == "Option 4":
        #     image1_path = "path/to/image1_option4.png"
        #     image2_path = "path/to/image2_option4.png"

        # Load the images using PIL
        # image1 = Image.open(image1_path)
        # image2 = Image.open(image2_path)

        colu1, colu2 = st.columns((2))
        with colu1:
            st.image(images1_path, caption=f"{selected_option}", use_column_width=True)
        with colu2:
            st.image(images2_path, caption=f"{selected_option} workflow time ", use_column_width=True)

    with tabs2:
        @st.cache_data
        def load_image(image_path):
            return Image.open(image_path)


        image1_option1 = load_image(
            r'\\rbsres01\shareddata\rassre\AIMLData\Glacier\Glacier_Processmap\STPExceptionSettlementWFQueue.png')
        image1_option2 = load_image(
            r'\\rbsres01\shareddata\rassre\AIMLData\Glacier\Glacier_Processmap\STPExceptionSettlementWFQueuetime.png')
        image2_option1 = load_image(
            r'\\rbsres01\shareddata\rassre\AIMLData\Glacier\Glacier_Processmap\SettlementMultipleSSIExceptionWFQueue.png')
        image2_option2 = load_image(
            r'\\rbsres01\shareddata\rassre\AIMLData\Glacier\Glacier_Processmap\SettlementMultipleSSIExceptionWFQueuetime.png')
        image3_option1 = load_image(
            r'\\rbsres01\shareddata\rassre\AIMLData\Glacier\Glacier_Processmap\SettlementMissingSSIExceptionWFQueue.png')
        image3_option2 = load_image(
            r'\\rbsres01\shareddata\rassre\AIMLData\Glacier\Glacier_Processmap\SettlementMissingSSIExceptionWFQueuetime.png')


        #st.markdown("<h5>Exception Workflows</h5>", unsafe_allow_html=True)
        selected_option = st.selectbox("", ['STPExceptionSettlementWFQueue', 'SettlementMultipleSSIExceptionWFQueue',
                                            'SettlementMissingSSIExceptionWFQueue'], index=0)

        # Define the paths to your images based on the selected option
        if selected_option == "STPExceptionSettlementWFQueue":
            image1_path = image1_option1
            image2_path = image1_option2

        elif selected_option == "SettlementMultipleSSIExceptionWFQueue":
            image1_path = image2_option1
            image2_path = image2_option2
        elif selected_option == "SettlementMissingSSIExceptionWFQueue":
            image1_path = image3_option1
            image2_path = image3_option2
        # elif selected_option == "Option 4":
        #     image1_path = "path/to/image1_option4.png"
        #     image2_path = "path/to/image2_option4.png"

        # Load the images using PIL
        # image1 = Image.open(image1_path)
        # image2 = Image.open(image2_path)

        colu1, colu2 = st.columns((2))
        with colu1:
            st.image(image1_path, caption=f"{selected_option}", use_column_width=True)
        with colu2:
            st.image(image2_path, caption=f"{selected_option} workflow time ", use_column_width=True)



