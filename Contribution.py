import pandas as pd
from treeinterpreter import treeinterpreter as ti
import ContributionSort as cs
def Contribution(model_dict, data_to_anly, period):
		predict, biases, contributions = ti.predict(model_dict['P' + str(period) + 'RF'], data_to_anly.drop(['Yield'], axis=1))
		#將各筆資料的變數以貢獻程度降冪排列，合併貢獻值與變數名稱
		df_sort_contributions = cs.contributionSort(contributions, list(data_to_anly.columns))
		tmp = pd.DataFrame(data={'Actual': data_to_anly.loc[:, 'Yield'],
								 'Predict':list(predict),
								 'Biases': list(biases)})
		contribution = pd.concat([tmp, df_sort_contributions], axis=1)
		return contribution
