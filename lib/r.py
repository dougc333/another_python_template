import pandas as pd
import statsmodels.api as sm

df = pd.read_csv("data/NLSY.csv")
df.dropna(inplace=True)
print(df.head())
x = df['MCS2000']
x = sm.add_constant(x)
y = df['PCS2000']

model = sm.OLS(y,x).fit()
print(type(model))
print(model.summary())
print("--------------------------------")
print(model.summary2())
print("--------------------------------")
print("HCO_se:",model.HC0_se)
print("--------------------------------")
print("HC1_se:",model.HC1_se)
print("--------------------------------")
print("HC2_se:",model.HC2_se)
print("--------------------------------")
print("HC3_se:",model.HC3_se)
print("--------------------------------")
print("aic:",model.aic)
print("--------------------------------")
print("bic:",model.bic)
print("--------------------------------")
print("bse:",model.bse)
print("--------------------------------")
print("centered_tss:",model.centered_tss)
print("--------------------------------")
print("condition_number:",model.condition_number)
print("--------------------------------")
print("cov_HC0:",model.cov_HC0)
print("--------------------------------")
print("cov_HC1:",model.cov_HC1)
print("--------------------------------")
print("cov_HC2:",model.cov_HC2)
print("--------------------------------")
print("cov_HC3:",model.cov_HC3)
print("--------------------------------")
print("eigenvals:",model.eigenvals)
print("--------------------------------")
print("ess:",model.ess)
print("--------------------------------")
print("f_pvalue:",model.f_pvalue)
print("--------------------------------")
print("fittedvalues:",model.fittedvalues)
print("--------------------------------")
print("f_value:",model.fvalue)
print("--------------------------------")
print("mse_model:",model.mse_model)
print("--------------------------------")
print("mse_resid:",model.mse_resid)
print("--------------------------------")
print("mse_total:",model.mse_total)
print("--------------------------------")
print("nobs:",model.nobs)
print("--------------------------------")
print("p_values:",model.pvalues)
print("--------------------------------")
print("resid:",model.resid)
print("--------------------------------")
print("resid_pearson:",model.resid_pearson)
print("--------------------------------")
print("rsquared:",model.rsquared)
print("--------------------------------")
print("rsquared_adj:",model.rsquared_adj)
print("--------------------------------")
print("ssr:",model.ssr)
print("--------------------------------")
print("tvalues:",model.tvalues)
print("--------------------------------")
print("uncentered_tss:",model.uncentered_tss)
print("--------------------------------")
print("use_t:",model.use_t)
print("--------------------------------")
print("wresid:",model.wresid)
print("--------------------------------")
