# CoinGecko

Python programm which retrieves `N` coins sorted by market capitalization.

# Beautiful Soup

Beautiful Soup is a Python library for pulling data out of HTML and XML files. It works with your favorite parser to provide idiomatic ways of navigating, searching, and modifying the parse tree.

## Installation

Script uses `bs4` and `selenium` libraries

```shell
$ pip install bs4
$ pip install selenium
```

Also script uses `Safari` browser to send HTTP requests.

```shell
safaridriver --enable
```

## Usage

To run main script simply type these commands:

```shell
$ cd src/
$ python3 coingesko.py
```

To run tests type following commands:

```shell
$ cd test/
$ python3 test.py
```

## Examples

Here is the example of script usage:

```shell
Enter amount of coins: 10
1: Bitcoin
2: Ethereum
3: Cardano
4: Tether
5: Binance Coin
6: XRP
7: Solana
8: Polkadot
9: USD Coin
10: Dogecoin
```
