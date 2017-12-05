#將每筆資料的變數以變數貢獻大小降冪排列，並回傳合併貢獻值與變數名稱的dataframe
import numpy as np
import pandas as pd
def contributionSort(contributions, col):
	col.remove('Yield')
	row_num, col_num = contributions.shape
	sort_contri_tuple = np.zeros((row_num, col_num), dtype=tuple)
	sort_contri_dataframe = pd.DataFrame(np.nan, index = range(row_num), columns=range(col_num))
	for i in range(row_num):
		for j in range(col_num):
			sort_contri_tuple[i, j] = (contributions[i, j], col[j])
	for i in range(row_num):
		sort_contri_tuple[i, :] = sorted(sort_contri_tuple[i, :], reverse=True)
		for j in range(col_num):
			sort_contri_dataframe.iloc[i, j] = str(sort_contri_tuple[i][j][0]) + " " + str(sort_contri_tuple[i][j][1])
	return sort_contri_dataframe
