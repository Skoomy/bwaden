# BWADEN 🚀




## Running the Project with Docker

1. **Build the Docker image**:

```bash
   docker-compose build
```

2. **Run container**

```bash
docker-compose up
```
3. **Stop container**

```sh
docker-compose down
```

4. **Run in the docker**

```sh
docker-compose exec stock_analysis bash
```


## Pre-requisites

### Setting Up Pre-Commit Hooks

Pre-commit hooks are used to enforce code quality and consistency before each commit. Follow these steps to set it up:

1. **Install pre-commit**:
   ```bash
   pip install pre-commit
   ```

2. Install the hook

```sh
pre-commit install
```

3. Run precommit on each file

```sh
pre-commit run --all-files
```


## Strategy

5. Momentum Strategy

Capitalizes on the continuation of existing price trends. Strategies like using the Relative Strength Index (RSI) or trend-following indicators help traders ride strong market movements in a specific direction.

6. Time-Weighted Average Price (TWAP)

Splits the trade evenly over a set time period regardless of volume, aiming to achieve an average execution price close to the start-to-finish (arrival) price.

7. Volume-Weighted Average Price (VWAP)

Divides orders into smaller trades executed throughout the day at the volume-weighted average price.

It takes into account historical volume profiles and market impact to optimize execution, with strategies like Implementation Shortfall VWAP aiming for minimal deviation from the VWAP.

8. Seasonality Trading

Identifies recurring market patterns based on time factors (year, month, week, etc.). For example, the Calendar Spread Strategy exploits seasonal trends by taking positions in futures contracts or options with different expiration dates.

9. Volatility Trading

Focuses on profiting from changes in market volatility by using options, futures, or other derivatives. An example is the Volatility Breakout strategy, which aims to capture significant price movements after periods of low volatility.

10. Machine Learning-Based Strategy

Leverages machine learning algorithms (e.g., Neural Networks, Random Forests, Support Vector Machines) to analyze large datasets and uncover complex patterns, aiding in making data-driven trading decisions.


## Teckstack

- Django
