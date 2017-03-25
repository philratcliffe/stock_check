#!/bin/bash
source /home/redkestrel/.virtualenvs/stock_check/bin/activate

export smtp_username=phil@philratcliffe.co.uk
export smtp_password=
export recip=phil@redkestrel.co.uk
export sender=phil@redkestrel.co.uk

/home/redkestrel/.virtualenvs/stock_check/bin/python /home/redkestrel/projects/stock_check/check_stock.py ^FTSE 8000




