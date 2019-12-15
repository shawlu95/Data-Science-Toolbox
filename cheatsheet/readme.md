### Formula & Proof
| Name                      | Notebook |
|---------------------------|----------|
| Common distributions      | [Link](cheatsheet/distribution.pdf)
| Gaussian error function   | [Link](cheatsheet/gaussian_erf.pdf)
| Integrating Gaussian      | [Link](cheatsheet/integrate_Gaussian.pdf)
| Markov Inequality         | [Link](cheatsheet/markov_inequality.pdf)
| Statistical testing       | [Link](cheatsheet/statistical_test.pdf)

### Stats Test [[Link](https://github.com/quantopian/research_public/blob/master/notebooks/lectures/Violations_of_Regression_Models/notebook.ipynb)]
* Durbin-Watson test: If the errors are homoskedastic, we can test for autocorrelation
* Breusch-Pagan test / White test: conditional heteroskedasticity. null: not heteroscedastic.
  - fix: differences analysis, log transformations, and Box-Cox transformations.
  - GARCH (generalized autoregressive conditional heteroscedasticity) 
* Jarque-Bera: normality
* Ljun-Box test: autocorrelation, null: not autocorrelation
* Newey-West: computing variance which accounts for autocorrelation
* Dickey-Fuller: checking for non-stationary, the presence of a unit root (null: has unit root)
