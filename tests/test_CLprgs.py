""" Test routine for Statsintro
you may have to install

pip install lifelines
pip install scikits.bootstrap
pip install mord

ToDo:
- fork "bootstrap", and replace scipy.mean with np.mean
"""

# author: Thomas Haslwanter, date: Sept-2021

# Import standard packages
import numpy as np
import pandas as pd
import sys
import os

rootDir = '..'
for dirName, subdirList, fileList in os.walk(rootDir, topdown=False):
    sys.path.append(dirName)
    print('directory: %s added to PYTHONPATH' % dirName)

# additional packages
import unittest

import ISP_anovaOneway
import ISP_anovaTwoway
import ISP_anscombe
import ISP_bayesianStats
import ISP_binomialTest
import ISP_bivariate
import ISP_bootstrapDemo
import ISP_centralLimitTheorem
import ISP_checkNormality
import ISP_compGroups
import ISP_confidence_intervals as ISP_ci        # todo
import ISP_correlation                  # todo
import ISP_corrVis                       # todo
import ISP_distContinuous
import ISP_distDiscrete
import ISP_distNormal
import ISP_fitLine
import ISP_gettingStarted
import ISP_HypothesisTests_vs_Modeling
import ISP_interactive_plots
import ISP_kruskalWallis
import ISP_lifelinesDemo
#import ISP_linearRegression             # todo
import ISP_logisticRegression
import ISP_matlab_data                  # todo
import ISP_modelImplementations
import ISP_multipleRegression
import ISP_multipleTesting
import ISP_mystyle
import ISP_oneGroup
import ISP_ordinalLogisticRegression
import ISP_read_zip                     # todo
import ISP_sampleSize
import ISP_showPandas                   # todo
import ISP_showPlots
import ISP_simpleModels
import ISP_TimeSeries                   # todo
import ISP_twoGroups

import L2_1_square_me                   # todo
import L2_2_python_module               # todo
import L2_3_python_import               # todo
import L2_4_pythonFunction
import L2_4_python_script               # todo
import L2_4_python_script_wfunc         # todo
import L3_2_readZip
import L3_2_readZip
import L4_1_interactivePlots           # ????
import L4_1_simple_Figure               # todo
import L4_5_plots3D                     # todo
import L8_1_HypothesisTests_vs_Modeling # todo
import L9_hypergeometric                # todo
import L10_1_weibullDemo
import L10_2_lifelinesSurvival
import L13_1_logitShort


class TestSequenceFunctions(unittest.TestCase):
    def setUp(self):
        t = np.arange(0,10,0.1)
        x = np.sin(t)
        self.data = x
        

    def test_CIs(self):
        alpha = 0.05
        ci_level = int( (1-alpha)*100 )

        cis = ISP_ci.binomial(5, 100, alpha=alpha, ci_type='two-sided')
        self.assertAlmostEqual(cis[0], 0.0164318792)

        cis = ISP_ci.binomial(1, 20, alpha=0.01, ci_type='upper')
        self.assertAlmostEqual(cis[0], 0.288790368)

        cis = ISP_ci.binomial(30, 1200, alpha=0.01)
        self.assertAlmostEqual(cis[0], 0.0148760034)

        cis = ISP_ci.binomial(30, 1200, alpha=0.05, ci_type='two-sided')
        self.assertAlmostEqual(cis[0], 0.0169295121)

        cis = ISP_ci.binomial_newton(30, 1200, alpha=0.05, ci_type='two-sided')
        self.assertAlmostEqual(cis[0], 0.0169295121)

        cis = ISP_ci.binomial_approx(30, 1200, alpha=0.05, ci_type='two-sided')
        self.assertAlmostEqual(cis[0], 0.0165832284)

        cis = ISP_ci.sigma(sigma_data=30, num=10, ci_type='upper')
        self.assertAlmostEqual(cis[0], 41.1326848195)

        cis = ISP_ci.sigma(sigma_data=30, num=10, ci_type='upper', alpha=0.01)
        self.assertAlmostEqual(cis[0], 46.5467446052)

        cis = ISP_ci.binomial(2, 120, alpha=0.01, ci_type='upper')
        self.assertAlmostEqual(cis[0], 0.0682058584)

        expected = 12
        cis = ISP_ci.poisson(expected, alpha=0.01, ci_type='two-sided')
        self.assertAlmostEqual(cis[0], 4.9431167511)

        (expected, total) = (14, 400)
        cis = ISP_ci.poisson_newton(expected, alpha=0.05, ci_type='two-sided')
        self.assertAlmostEqual(cis[0], 7.6539302763)

        data = [89, 104.1, 92.3, 106.2, 96.3, 107.8, 102.5, 121.2,
                98, 109.4, 99.7, 111.6, 101.4, 113.8, 116.6]
        cis = ISP_ci.mean(data, ci_type='lower', alpha=0.01)
        self.assertAlmostEqual(cis[0], 98.5585492011)

        data = [49.93, 50.03, 49.99, 50.08, 49.96, 50.03]
        cis = ISP_ci.sigma(data, alpha=0.01)
        self.assertAlmostEqual(cis[0], 0.0296584368)

        cis = ISP_ci.mean(values=75, num_and_sigma = (10, 12))
        self.assertAlmostEqual(cis[0], 67.5624596123)


    def test_lifelinesDemo(self):
        ISP_lifelinesDemo.main()
        

    def test_figs_BasicPrinciples(self):   # interactive
        ISP_showPlots.simple_plots()
        ISP_showPlots.show3D()
        

    def test_figs_DistributionNormal(self):    # interactive
        ISP_distNormal.simple_normal()
        ISP_distNormal.shifted_normal()
        ISP_distNormal.many_normals()
        
        
    def test_figs_DistContinuous(self):    # interactive
        ISP_distContinuous.show_t()
        ISP_distContinuous.show_chi2()
        ISP_distContinuous.show_f()
        ISP_distContinuous.show_exp()
        
    def test_figs_DistDiscrete(self):  # interactive
        ISP_distDiscrete.show_binomial()
        ISP_distDiscrete.show_poisson()
        
    def test_anovaOneway(self):
        (F,p) = ISP_anovaOneway.anova_oneway()
        self.assertAlmostEqual(F, 3.711335988266943)
        self.assertAlmostEqual(p, 0.043589334959179327)
        
        (F,p) = ISP_anovaOneway.anova_byHand()
        self.assertAlmostEqual(F, 3.711335988266943)
        self.assertAlmostEqual(p, 0.043589334959179327)
        
        F = ISP_anovaOneway.show_teqf()
        self.assertAlmostEqual(F, 2083.481, places=2)
        

    def test_anovaTwoway(self):
        F = ISP_anovaTwoway.anova_interaction()
        self.assertAlmostEqual(F, 2113.101449275357)
        

    def test_bayesianStats(self):
        np.random.seed(1234)
        (temperature, failures) = ISP_bayesianStats.getData()    
        (alpha, beta) = ISP_bayesianStats.mcmcSimulations(temperature, failures)
        (linearTemperature, mean_p, p, quantiles) = ISP_bayesianStats.calculateProbability(alpha, beta, temperature, failures)
        
        self.assertAlmostEqual(linearTemperature[20][0], 63.51020408)
        self.assertAlmostEqual(mean_p[20], 0.573, places=1) 
        self.assertLess(mean_p[20]-0.573, 0.1)


    def test_binomialTest(self):
        p1,p2 = ISP_binomialTest.binomial_test(51)
        self.assertAlmostEqual(p1, 0.0265442457117)
        self.assertAlmostEqual(p2, 0.0437479701824)
        

    def test_bootstrapDemo(self):
        data = ISP_bootstrapDemo.generate_data()
        CI = ISP_bootstrapDemo.calc_bootstrap(data)        
        self.assertAlmostEqual(CI[0], 1.884, places=2)
        

    def test_checkNormality(self):
        p = ISP_checkNormality.check_normality(show_flag=False)
        self.assertAlmostEqual(p, 0.47144747394230224)
        

    def test_compGroups(self):
        ci = ISP_compGroups.oneProportion()
        self.assertAlmostEqual(ci[0], 0.130, places=2)
        
        chi2 = ISP_compGroups.chiSquare()
        self.assertAlmostEqual(chi2[0], 4.141, places=2)
        
        fisher = ISP_compGroups.fisherExact()
        self.assertAlmostEqual(fisher[1], 0.035, places=2)
        

    def test_fitLine(self):
        
        # example data
        x = np.array([15.3, 10.8, 8.1, 19.5, 7.2, 5.3, 9.3, 11.1, 7.5, 12.2,
                      6.7, 5.2, 19.0, 15.1, 6.7, 8.6, 4.2, 10.3, 12.5, 16.1, 
                      13.3, 4.9, 8.8, 9.5])
        y = np.array([1.76, 1.34, 1.27, 1.47, 1.27, 1.49, 1.31, 1.09, 1.18, 
                      1.22, 1.25, 1.19, 1.95, 1.28, 1.52, np.nan, 1.12, 1.37, 
                      1.19, 1.05, 1.32, 1.03, 1.12, 1.70])
                      
        goodIndex = np.invert(np.logical_or(np.isnan(x), np.isnan(y)))
        (a,b,(ci_a, ci_b), ri,newy) = ISP_fitLine.fitLine(x[goodIndex],y[goodIndex], alpha=0.01,newx=np.array([1,4.5]))        
        
        self.assertAlmostEqual(a,1.09781487777)
        self.assertAlmostEqual(b,0.02196252226)
        

    def test_gettingStarted(self):
        ISP_gettingStarted.main()
        

    def test_interactivePlots(self):
        ISP_interactive_plots.normalPlot()    
        ISP_interactive_plots.positionOnScreen()    
        ISP_interactive_plots.showAndPause()    
        ISP_interactive_plots.waitForInput()    
        ISP_interactive_plots.keySelection()
        

    def test_KruskalWallis(self):
        h = ISP_kruskalWallis.main()
        self.assertAlmostEqual(h, 16.028783253379856)
        
    def test_logit(self):
        from statsmodels.formula.api import glm
        from statsmodels.genmod.families import Binomial
        
        inData = ISP_logisticRegression.getData()
        dfFit = ISP_logisticRegression.prepareForFit(inData)
        model = glm('ok + failed ~ temp', data=dfFit, family=Binomial()).fit()
        ISP_logisticRegression.showResults(inData, model)
        
        self.assertAlmostEqual(model.params.Intercept, -15.042902, places=5)
        
    def test_modeling(self):
        F = ISP_simpleModels.model_formulas()
        self.assertAlmostEqual(F, 156.1407931415788)
        
        params = ISP_simpleModels.polynomial_regression()
        self.assertAlmostEqual(params[0], 4.74244177)
        
    def test_multipleTesting(self):
        var = ISP_multipleTesting.main()
        self.assertAlmostEqual(var,-4.0249223594996213)
        
    def test_multivariate(self):
        F = ISP_bivariate.regression_line()    
        self.assertAlmostEqual(F, 4.4140184331462571)
        
        pearson = ISP_bivariate.correlation()
        self.assertAlmostEqual(pearson, 0.79208623217849117)
        
    def test_multipleRegression(self):
        ISP_multipleRegression.scatterplot()
        (X,Y,Z) = ISP_multipleRegression.generateData()
        bestfit1 = ISP_multipleRegression.regressionModel(X,Y,Z)    
        self.assertAlmostEqual(bestfit1[0], -4.99754526)
        
        bestfit2 = ISP_multipleRegression.linearModel(X,Y,Z)        
        self.assertAlmostEqual(bestfit2[0][0], -4.99754526)
        
    def test_ologit(self):
        X, y = ISP_ordinalLogisticRegression.get_data()
        models = ISP_ordinalLogisticRegression.compare_models(X, y)
        test_val = np.mean(models[1].scores)
        
        self.assertAlmostEqual(test_val, 2.668627450980392, places=5)
        
    def test_oneSample(self):
        p = ISP_oneGroup.check_mean()
        self.assertAlmostEqual(p, 0.018137235176105802)
        
        p2 = ISP_oneGroup.compareWithNormal()
        self.assertAlmostEqual(p2, 0.054201154690070759)


    def test_read_zip(self):
        url = 'https://work.thaslwanter.at/sapy/GLM.dobson.data.zip'
        inFile = 'Table 2.8 Waist loss.xls'
        df = ISP_read_zip.get_data_dobson(url, inFile)
        
        self.assertAlmostEqual(df['after'][0], 97)
        

    def test_sampleSize(self):
        n1 = ISP_sampleSize.sampleSize_oneGroup(0.5)
        self.assertEqual(n1, 31)
        
        n2 = ISP_sampleSize.sampleSize_twoGroups(0.4, sigma1=0.6, sigma2=0.6)
        self.assertEqual(n2, 35)
        

    def test_twoSample(self):
        p1 = ISP_twoGroups.paired_data()
        self.assertAlmostEqual(p1, 0.0009765625) 
        
        p2 = ISP_twoGroups.unpaired_data()
        self.assertAlmostEqual(p2, 0.002121613385880049)
        
    
"""
    # Older functions
    
    def test_figROC(self):
        fig_roc.main()
        
    def test_gettingStarted_ipy(self):
        gettingStarted_ipy.main()
        
    def test_pandas_intro(self):
        df = pandas_intro.labelled_data()
        self.assertAlmostEqual(df['values'][0], 4.7465508100784524)
        
        parameters = pandas_intro.simple_fit(df)
        self.assertAlmostEqual(parameters['x'], 0.50516249093121246)
        
    def test_residuals(self):
        exec(compile(open('residuals.py').read(), 'residuals.py', 'exec'), {})
        
    def test_showStats(self):
        showStats.main()
        
"""
        
        
if __name__ == '__main__':
    testAll = True
    if testAll:
        unittest.main()
    else:
        suite = unittest.TestSuite()
        suite.addTest(TestSequenceFunctions('test_oneSample'))
        runner = unittest.TextTestRunner()
        runner.run(suite)
    
    eval(input('Thanks for using programs from Thomas!'))
    
    """
    # should raise an exception 
    self.assertRaises(TypeError, savgol, np.arange(3), window_size=5)
    self.assertTrue(np.abs(1-smoothed[round(np.pi/2*10)]<0.001))
    self.assertEqual(firstDeriv[14], fD[14])
    """
