# Task for Sustaihub - Simple stock price crawler

## Local development
```
poetry shell
poetry install
```

## Database Initialize
```
python -m database.session
```


## Run crawler
Just execute

```
python main.py
```


Output should be like

```log
2024-09-25 23:24:42.640 | INFO     | __main__:<module>:41 - No: 1     | 2f6301449ac94b88920a2d8eda54def8 | interval[0:00:20]
2024-09-25 23:24:42.640 | INFO     | __main__:<module>:44 - Scheduler started.

...

2024-09-25 23:22:14.166 | INFO     | database.operations:insert_price:35 - date=datetime.date(2024, 9, 25) symbol='9955' open=38.15 high=39.75 low=37.6 close=37.65 volume=7845109.0 values=303243448.0 inserted into 'price'.
2024-09-25 23:22:14.166 | INFO     | database.operations:insert_price:35 - date=datetime.date(2024, 9, 25) symbol='9958' open=250.0 high=250.5 low=238.0 close=238.0 volume=10003697.0 values=2444472070.0 inserted into 'price'.
2024-09-25 23:22:14.166 | INFO     | database.operations:insert_collect_record:13 - date=datetime.date(2024, 9, 25) data_type=<DataType.STOCK_PRICE: 'stock_price'> result=<CollectResult.SUCCESS: 'success'> reason=None inserted into 'collect_record'.
2024-09-25 23:22:14.166 | INFO     | tasks:get_stock_price_task:38 - 2024-09-25 Stock price collect task is done
2024-09-25 23:22:19.085 | INFO     | __main__:<module>:51 - Scheduler shut down successfully.
```
