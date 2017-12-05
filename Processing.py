import pandas as pd
import RunFunction as rc
import VariableGroup as vg
import Contribution as ct
import SplitData as sp
def processing(menbersfile, potatofile, function, max_period):
	#初始化
	potato = pd.read_csv(potatofile)
	model_dict = {}#各期各方法訓練後的模型
	predict_dict = {}#各期各方法的訓練、測試、驗證(if any)的RMSE
	contributions_dict = {}#各期隨機森林的變數貢獻度
	for period in range(1, max_period + 1):
		#獲取第period期數所需要分析的資料欄位
		anly_columns = vg.variableGroup(potato, period, max_period)
		#將資料切割成訓練、測試、驗證
		split_data = sp.splitData(potato.loc[:, anly_columns])
		#計算第period期各方法建立的模型、訓練RMSE、測試RMSE、驗證RMSE(if any)
		for func_type in function:
			model, rmse = rc.runFunction(split_data, func_type)
			model_dict['P' + str(period) + str(func_type)] = model
			predict_dict['P' + str(period) + str(func_type)] = rmse
		#計算第period期的隨機森林中，預測testing與validation時各變數的貢獻
		for item in split_data:
			contributions_dict['P' + str(period) + item] = ct.Contribution(model_dict, split_data[item], period)
	return predict_dict, contributions_dict
