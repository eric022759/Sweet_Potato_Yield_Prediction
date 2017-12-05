"""""
計算當期所需要分析的資料欄位
e.g. variableGroup(Period1) => single_group(Period1)
	 variableGroup(Period2) => single_group(Period1) U single_group(Period2)
	 variableGroup(Period3) => single_group(Period1) U single_group(Period2) U single_group(Period3)
"""
#將當期與所有前期的變數群組取聯集
def variableGroup(data, current_period, max_period):
	union_group = []
	for period in range(1, current_period + 1):
		union_group = list(set(union_group).union(single_group(data, period, max_period)))
	return union_group

#僅含當期的變數群組
def single_group(data, current_period, max_period):
	data_col_num = len(data.columns)
	data_col = data.columns
	group = []
	for col_inx in range(data_col_num):
		for i in range(1, max_period + 1):
			if (current_period == i) and (data_col[col_inx].find(str(current_period),-2) == len(data_col[col_inx]) - 1):
				group.append(data_col[col_inx])
				break
			elif data_col[col_inx].find(str(i),-2) == len(data_col[col_inx]) - 1:
				break
			elif i == max_period:
				group.append(data_col[col_inx])
	return group
