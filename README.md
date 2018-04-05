# Gets the value of a stock and if it is below a threshold sends an email.

## Update 
Yahoo have removed their financial data API, which this code relied on, so
currently it is not working.

## Installation
    - Ensure that you are running in a Python3 environment.
    - pip install -r requirements.txt

## Running 
In the example below, an email will be sent if the FTSE has dropped below 6000.

```bash
$ python check_stock.py FTSE 6000
```

