from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.neural_network import MLPRegressor
from sklearn import tree, linear_model
from sklearn.metrics import mean_squared_error
#建立function模型，並計算訓練、驗證、測試的RMSE
def runFunction(split_data, function, estimators=210):
	#初始化
	x, y, rmse = {}, {}, {}
	#切割DV與IV
	for item in split_data:
		x[item] = split_data[item].drop(['Yield'], axis=1)
		y[item] = split_data[item].loc[:, 'Yield']
	#建立function的模型
	if function == 'RF':
		model = RandomForestRegressor(n_estimators=estimators, criterion='mse', random_state=0).fit(x['training'],y['training'])
	if function == 'GB':
		model = GradientBoostingRegressor(n_estimators=50, criterion='mse', loss='huber').fit(x['training'], y['training'])
	if function == 'NN':
		model = MLPRegressor(solver='lbfgs', random_state=0).fit(x['training'], y['training'])
	if function == 'DT':
		model = tree.DecisionTreeRegressor(max_depth=5, random_state=0).fit(x['training'], y['training'])
	if function == 'RE':
		model = linear_model.LinearRegression().fit(x['training'], y['training'])
	#計算訓練、測試、驗證(if any)RMSE
	for item in split_data:
		rmse[item] = mean_squared_error(y[item], model.predict(x[item])) ** 0.5
	return model, rmse
