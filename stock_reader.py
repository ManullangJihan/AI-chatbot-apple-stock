from llama_index.core.tools import FunctionTool
import os
import yfinance as yf
import datetime as dt

def apple_stock_reader():
    asset = "AAPL"
    now = dt.datetime.now()
    start_date = now - dt.timedelta(days=15)
    start_date = start_date.strftime("%Y-%m-%d")
    end_date = now - dt.timedelta(days=2)
    interval = "1d"
    df = yf.download(asset, start=start_date, end=end_date, interval=interval)
    last_val = str(df.iloc[-1, 1])
    date = df.index[-1].strftime("%Y-%m-%d")
    file_content = {"current_price": f"The AAPL stock at {date} is: {last_val}"}
    return file_content


stock_reader_func = FunctionTool.from_defaults(
    fn=apple_stock_reader,
    name="apple_stock_reader",
    description="""this tool can read the latest price of Apple (AAPL) stock return 
    its value. Use this when you need to provide the Apple (AAPL) stock""",
)
