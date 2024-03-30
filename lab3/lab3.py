from spyre import server

class SimpleApp(server.App):
    title = "lab_3"

    inputs = [dict( type='text',
                    key='AreaID',
                    label='Area ID here',
                    value='5',
                    action_id='simple_html_output'),
              dict(type='text',
                    key='year1',
                    label='year 1',
                    value='2005',
                    action_id='simple_html_output'),
              dict(type='text',
                    key='year2',
                    label='year 2',
                    value='2021',
                    action_id='simple_html_output'),
              {"type":'dropdown',
               "label":'NOAA data dropdown',
               "options": [{"label": "VHI", "value":"VHI"},
                         {"label": "VCI", "value":"VCI"},
                         {"label": "TCI", "value":"TCI"}],
               "key": 'ticker',
               "action_id": "update_data"}]

    outputs = [dict( type='html',
                     id='simple_html_output')]



    def getHTML(self, params):
        AreaID = params["AreaID"]
        year1 = params["year1"]
        year2 = params["year2"]
        return "year 1 — <b>%s</b>, year 2 — <b>%s</b>,  AreaID — <b>%s</b>" % ( year1, year2, AreaID)

app = SimpleApp()
app.launch(port=8800)