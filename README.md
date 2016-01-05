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


## Monkey Patching

You can change the data returned from Yahoo with the cryptic query parameter at the end of the URL: '&f=nsl1oc1p2'. For all of the possible fields, see: https://code.google.com/p/yahoo-finance-managed/wiki/enumQuoteProperty. You'll want to update the headers passed to 'tabulate()' as well.
