import Processing as pp
import pandas as pd
import sys
predict_dict, contributions_dict = pp.processing(menbersfile='Members Data.csv',
                                                 potatofile='Cultivated Data.csv',
                                                 function=['NN', 'GB', 'RF', 'RE', 'DT'],
                                                 max_period=3)
model_comparison = pd.DataFrame(data=predict_dict)
for item in contributions_dict:
    setattr(sys.modules[__name__], item, contributions_dict[item])

