# ticks

Simple command line tool for displaying stock data in the command line

## Installation

```
pip install ticks
```

or if you plan on developing or monkey-patching:

```
pip install -e {ticks directory}
```

## Usage

```
ticks aapl goog ^spx ^FTSE
```

*Note:* all arguments must be Yahoo Finance URL parameters for the symbol

## Results

```
$ ticks VTI VXUS BND ^SPX ^FTSE ^BCOM VNQ
Name                             Symbol        Price     Open    Change  Change%
-------------------------------  --------  ---------  -------  --------  ---------
Vanguard Total Stock Market ETF  VTI        102.97     102.9     0.23    +0.22%
Vanguard Total International St  VXUS        44.25      44.34   -0.08    -0.18%
Vanguard Total Bond Market ETF   BND         80.82      80.76    0.1     +0.12%
S&P 500                          ^SPX      2016.71    2013.78    4.05    +0.20%
FTSE 100                         ^FTSE     6137.24    6093.43   43.81    +0.72%
Dow Jones-UBS Commodity Index    ^BCOM       77.6628   100.01   -0.2426  -0.3114%
Vanguard REIT ETF - DNQ          VNQ         80.29      78.8     1.52    +1.93%
```

## Monkey Patching

You can change the data returned from Yahoo with the cryptic query parameter at the end of the URL: `&f=nsl1oc1p2`.

For all of the possible fields, see https://code.google.com/p/yahoo-finance-managed/wiki/enumQuoteProperty (this list seems to be out of date...)

You'll want to update the headers passed to `tabulate()` as well.
