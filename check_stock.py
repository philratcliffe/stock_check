import argparse
from pandas_datareader import data as web
import smtplib
import os
# Import the email modules we'll need
from email.mime.text import MIMEText


def get_latest_stock_price(stock):
    """Returns the latest price for the stock ticker provided"""
    x = web.get_data_yahoo(stock)
    result = x.tail(1)
    stock_price = result['Close'][0]
    return stock_price


def get_env_variable(name):
    """Get the environment variable or return an exception"""
    try:
        return os.environ[name]
    except KeyError:
        error_msg = "Set the {} environment variable".format(name)
        raise Exception(error_msg)


def send_email(msg_body):
    """Send email containing the message supplied"""

    username = get_env_variable("smtp_username")
    password = get_env_variable("smtp_password")
    recip = get_env_variable("recip")
    sender = get_env_variable("sender")

    # Create a text/plain message
    msg = MIMEText(msg_body)
    msg['Subject'] = 'Stock Alert'
    msg['From'] = sender
    msg['To'] = recip

    s = smtplib.SMTP('smtp.philratcliffe.co.uk')
    s.starttls()
    s.login(username, password)
    s.sendmail(sender, [recip], msg.as_string())
    s.quit()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "ticker",
        help="the ticker of the stock to get the price of",
    )
    parser.add_argument(
        "threshold",
        help="if stock falls below this value a notification is sent",
        type=int,
    )
    args = parser.parse_args()
    stock = args.ticker
    price = get_latest_stock_price(stock)
    if price < args.threshold:
        msg = "\nALERT: current {} price is {}".format(stock, price)
        send_email(msg)

