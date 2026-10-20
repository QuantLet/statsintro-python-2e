<div style="margin: 0; padding: 0; text-align: center; border: none;">
<a href="https://quantlet.com" target="_blank" style="text-decoration: none; border: none;">
<img src="https://github.com/StefanGam/test-repo/blob/main/quantlet_design.png?raw=true" alt="Header Image" width="100%" style="margin: 0; padding: 0; display: block; border: none;" />
</a>
</div>

```
Name of QuantLet: ISP_fitLine

Published in: An Introduction to Statistics with Python

Description: Linear regression fit Parameters ---------- x : ndarray Input / Predictor y : ndarray Input / Estimator alpha : float Confidence limit [default=0.05] newx : float or ndarray Values for which the fit and the prediction limits are calculated (optional) plotFlag: int (optional) 1 = plot, 0 = no_plot [default] Returns ------- a : float Intercept b : float Slope ci : ndarray Lower and upper confidence interval for the slope info : dictionary, containing return information on - residuals - var_res - sd_res - alpha - tval - df newy : list(ndarray) Predictions for (newx, newx-ciPrediction, newx+ciPrediction) Examples -------- >>> import numpy as np >>> from fitLine import fitLine >>> x = np.r_[0:10:11j] >>> y = x**2 >>> (a,b,(ci_a, ci_b),_)=fitLine(x,y) Notes ----- Example data and formulas are taken from D. Altman, <Practical Statistics for Medicine>

Keywords: line fit, confidence intervals, plot, linear regression

Author: Thomas Haslwanter

Submitted: October 31, 2015

Datafile: 

Example: regression_wLegend.png

```
<div align="center">
<img src="https://raw.githubusercontent.com/QuantLet/statsintro-python-2e/master/src/code_quantlets/12_LinearModels/fitLine/regression_wLegend.png" alt="Image" />
</div>

