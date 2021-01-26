from flask import Flask, request, render_template, session, redirect, url_for
from commands import ssh, scp
import folium, os
import pandas as pd
import numpy as np


# TODO: add predicted delay ***interval*** to points on map for livemap

def draw_df(mapit, df, radius=1/4, color='green'):
	df.apply(lambda row:folium.CircleMarker(location=[row['latitude'], row['longitude']], 
											radius=radius, color=color, fill=True,
											tooltip='delay interval: '+str(row['delay_interval'])+
												'\nvehicleId: '+str(row['vehicleId'])+
												'\ndatetime: '+str(row['datetime'])) 
	.add_to(mapit), axis=1)


def create_map(df, vehicleId, map_name):
	# lineId = df['patternLine'][0]
	vehicleId = int(vehicleId)
	anomaly_df = df[df['vehicleId']==vehicleId]
	regular_df = df[df['vehicleId']!=vehicleId]

	mapit = folium.Map( location=[df['latitude'].mean(), df['longitude'].mean()], zoom_start=15)

	draw_df(mapit, regular_df, radius=2, color='green')
	draw_df(mapit, anomaly_df, radius=3, color='red'  )
	

	mapit.save(f'templates/map_{map_name}.html')
	return map_name


def log(s):
	return 
	with open("a.txt", 'a') as f:
		f.write(s+'\n')


def read_elastic(file_name, index=None, patternLine=None, directionLine=None, year=None, month=None, day=None):
	if all(var is not None for var in [index, patternLine, directionLine, year, month, day]):
		options = f'-i {index} -l {patternLine} -dl {directionLine} -y {year} -m {month} -d {day}'
	else:
		options = ''
		index = 'menu_df'

	ssh(cmd=f'/opt/anaconda3/bin/python3 /home/vmadmin/read_index.py {options}')
	scp(path=f'/home/vmadmin/{index}.csv', dest=f'data/{file_name}.csv')


app = Flask(__name__) 
# run_with_ngrok(app) 


@app.route('/')
@app.route('/index')
def home():
	return render_template("index.html")

@app.route('/analyze')
def analyze_page():
	return render_template("analyze.html")


@app.route('/handle_data', methods=['POST'])
def handle_data():
	date = request.form['Date']
	directionLine = request.form['direction']
	patternLine = request.form['lineid']
	vehicleId = request.form['vehicle']
	year, month, day = date.split('-')
	map_name = '_'.join([year, str(int(month)), str(int(day)), patternLine, directionLine, vehicleId])
	print(map_name)

	if not os.path.isfile(f'data/map_{map_name}.csv'):
		read_elastic(f'map_{map_name}', index='df_full', patternLine=patternLine, 
				 directionLine=directionLine, year=year, month=month, day=day)
	else:
		print('skipping read_elastic')

	df = pd.read_csv(f'data/map_{map_name}.csv')
	if df.empty:
		return render_template('no_data.html')

	# create_map(df, vehicleId, map_name)
	return redirect(f"/live_map_{map_name}")


@app.route('/live_menu')
def liveMonitoring_menu():

	read_elastic('menu')

	menu_df = pd.read_csv("data/menu.csv")

	menu_df = menu_df.sort_values(['year', 'month', 'day'], ascending=False)
	menu_df['link'] = menu_df.apply(lambda row: '_'.join([str(row[c]) for c in ['year', 'month', 'day', 'patternLine', 'directionLine', 'vehicleId']]), axis=1)
	menu_df['link'] = menu_df['link'].apply(lambda link: f'<a href="http://127.0.0.1:5000/live_map_{link}">click here</a>')
	menu_df['date'] = menu_df.apply(lambda row: '.'.join([str(row[c]) for c in ['day', 'month', 'year']]), axis=1)
	menu_df = menu_df.rename(columns={'patternLine':'Line', 'directionLine': 'Direction', 
									  'vehicleId': 'Vehicle ID', 'link': 'Link', 'date': 'Date'})

	menu_df = menu_df[['Date', 'Line', 'Direction', 'Vehicle ID','Link']]
	menu_df = menu_df.reset_index(drop=True)
	menu_df.index += 1

	return render_template('live_menu.html',  table=menu_df.to_html(header="true", escape=False))


@app.route('/live_map_<map_name>')
def liveMonitoring_map(map_name):
	# 2017_11_24_044B_0_28051


	year, month, day, patternLine, directionLine, vehicleId = map_name.split('_')[:]
	print(patternLine, directionLine, vehicleId)
	if not os.path.isfile(f'data/map_{map_name}.csv'):
		read_elastic(f'map_{map_name}', index='df_full', patternLine=patternLine, 
				 directionLine=directionLine, year=year, month=month, day=day)
	else:
		print('skipping read_elastic')
	
	df = pd.read_csv(f'data/map_{map_name}.csv')
	map_name = create_map(df, vehicleId, map_name)

	menu_df = pd.read_csv("data/menu.csv")
	map_row = menu_df.loc[(menu_df['patternLine']==patternLine) & (menu_df['directionLine']==int(directionLine)) & 
						  (menu_df['vehicleId']==int(vehicleId)) & (menu_df['year']==int(year)) & 
						  (menu_df['month']==int(month)) & (menu_df['day']==int(day))]
	
	if map_row.empty: # not anomaly
		return render_template("map_page.html", map_name=map_name, lineId=patternLine)

	return render_template("map_page.html", map_name=map_name, lineId=patternLine, 
						   tweets=list(eval(map_row['relevant_tweets'].iloc[0])), events=list(eval(map_row['events_around'].iloc[0])),
						   rmse=round(map_row['prediction_rmse'].iloc[0], 3), acc=round(map_row['prediction_acc'].iloc[0], 3))


@app.route('/map_<map_name>')
def map(map_name):
	log(map_name)
	return render_template(f'map_{map_name}.html')

def main():
	app.run(debug=True)

if __name__ == '__main__':
    app.run(debug=True)
