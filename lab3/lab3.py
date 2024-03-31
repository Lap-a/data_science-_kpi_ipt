from spyre import server
import pandas as pd
from os import listdir
from datetime import datetime
import urllib.request

def dwn (i, y1, y2):
    url='https://www.star.nesdis.noaa.gov/smcd/emb/vci/VH/get_TS_admin.php?country=UKR&provinceID='+str(i)+'&week1='+str(y1)+'&week2='+str(y2)+'&type=Mean'

    wp = urllib.request.urlopen(url)
    text = wp.read()

    now = datetime.now()
    date_and_time_time = now.strftime('%d-%m-%Y_%H-%M-%S')
    out = open('data/NOAA_ID'+str(i)+'_'+date_and_time_time+'.csv','wb') # 'data/' — dir name
    out.write(text)
    out.close()

def csvs_to_frame(dir):
    file_names = listdir(dir)

    headers = ['Year', 'Week', 'SMN', 'SMT', 'VCI', 'TCI', 'VHI', 'AreaID']
    dfs = []

    for name in file_names:
        df = pd.read_csv(dir+name, header = 1, names = headers)
        df['AreaID'] = int(name[7:-24])

        # data cleaning
        df = df.drop(df.loc[df['VHI'] == -1].index)
        df = df.drop(df.index[-1])
        df.at[0, 'Year'] =  df.at[0, 'Year'][9:]
        df['Year'] = df['Year'].astype(int)

        dfs.append(df)

    frame = pd.concat(dfs).drop_duplicates().reset_index(drop=True)
    return frame

#==================================================

#user_input = input("wanna download data? (y/n): ")
#if user_input == "y":
#    for i in range(1,28): # y 29
#        dwn(i, 2000, 2023)

df = csvs_to_frame('data/')

#==================================================

class WebApp(server.App):
    title = "lab_3"

    inputs = [dict( type='text',
                    key='AreaID',
                    label='Area ID here',
                    value='5',
                    action_id='simple_html_output'),
              dict(type='text',
                    key='week1',
                    label='min week',
                    value='5',
                    action_id='simple_html_output'),
              dict(type='text',
                    key='week2',
                    label='max week',
                    value='21',
                    action_id='simple_html_output'),
              dict(type='text',
                    key='year',
                    label='year',
                    value='2021',
                    action_id='simple_html_output'),
              {"type":'dropdown',
               "label":'NOAA data dropdown',
               "options": [{"label": "VHI", "value":"VHI"},
                         {"label": "VCI", "value":"VCI"},
                         {"label": "TCI", "value":"TCI"}],
               "key": 'indicator',
               "action_id": "update_data"}]
    
    controls = [{"type" : "hidden",
                 "id" : "update_data"}]

    tabs = ["Table", "Plot"]

    outputs = [{"type":"table",
                 "id":"table_id",
                 "control_id":"update_data",
                 "tab":"Table",
                 "on_page_load":True},
                 {"type":"plot",
                 "id":"plot",
                 "control_id":"update_data",
                 "tab":"Plot"}]

    def getTable(self, params):
        global df
        w1 = int(params["week1"])
        w2 = int(params["week2"])
        y = int(params["year"])
        AreaID = int(params["AreaID"])
        indicator = params["indicator"]

        result_df = df[[indicator, 'Year', 'Week', 'AreaID']]
        result_df = result_df[(df["Year"]) == y]
        result_df = result_df[(df["AreaID"]) == AreaID]
        result_df = result_df[(df["Week"]) >= w1]
        result_df = result_df[(df["Week"]) <= w2]
        return result_df


    def getPlot(self, params):
        plt_obj = self.getTable(params).plot()
        plt_obj.set_ylabel("set_ylabel")
        plt_obj.set_title("set_title")
        fig = plt_obj.get_figure()
        return fig

app = WebApp()
app.launch(port=8800)