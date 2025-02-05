
# # Run the data collection pipeline
# python  -m  src  --pipeline=data_collection

# python -m src.cli runner


# # Fetch multiple symbols
# python -m src.cli runner --symbols "AAPL,MSFT,GOOGL" --days 60


# # Use different pipeline
# python -m src.cli runner --pipeline different_pipeline



# python -m src.cli fetch AAPL --days 45
python -m src.cli fetch PLTR --days 45
python -m src.cli fetch BLK --days 45
