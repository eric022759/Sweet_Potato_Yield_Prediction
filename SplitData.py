#將資料集分割成訓練資料、測試資料、驗證資料
def splitData(df, validation_num=0, testing_num=10):
	split_data = {}
	split_data['training'] = df.iloc[:df.shape[0] - validation_num - testing_num, :].reset_index(drop=True)
	split_data['testing'] = df.iloc[df.shape[0] - testing_num:, :].reset_index(drop=True)
	if validation_num != 0:
		split_data['validation'] = df.iloc[df.shape[0] - validation_num - testing_num : df.shape[0] - validation_num, :].reset_index(drop=True)
	return split_data