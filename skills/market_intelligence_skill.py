# market_intelligence_skill.py
from mcp.server.fastmcp import FastMCP
import yfinance as yf
import logging

mcp = FastMCP("SGX_Service")

@mcp.tool()
def get_dividend_data(ticker: str) -> dict:
    """Fetches yield, payout ratio, and 57 avg yield for an SGX stock."""
    stock = yf.Ticker(f"{ticker}.SI")
    info = stock.info
    logging.info(f"[INFO] Retrieving information on {ticker}")
    return {
        "symbol": ticker,
        "yield": info.get("dividendYield"),
        "payout": info.get("payoutRatio"),
        "history": stock.dividends.tail(5).to_dict() if len(stock.dividends) > 0 else {}
    }

@mcp.tool()
def get_macro_indicators() -> dict:
    """Fetches Singapore inflation, SORA rates, and GDP outlook."""
    # Logic to fetch from MAS (Monetary Authority of Singapore) or News APIs
    return {
        "SORA_rate": "3.65%",
        "inflation_target": "2.5%",
        "geopolitical_risk_index": "Elevated"
    }

@mcp.tool()
def get_growth_fundamentals(ticker: str) -> dict:
    """"Fetches revenue growth, P/E ratios, and analyst targets for SGX stocks."""
    stock = yf.Ticker(f"{ticker}.SI")
    return {
        "pe_ratio": stock.info.get("forwardPE"),
        "debt_to_equity": stock.info.get("debtToEquity"),
        "revenue_growth": stock.info.get("revenueGrowth"),
        "earnings_growth": stock.info.get("earningsGrowth"),
        "peg_ratio": stock.info.get("pegRatio"),
        "target_price_high": stock.info.get("targetHighPrice"),
        "current_price": stock.info.get("currentPrice")
    }


@mcp.tool()
def get_macro_indicators() -> dict:
    """
    Fetches key macroeconomic indicators relevant to the Singapore market:
    - US 10Y Yield (Interest rate benchmark)
    - Brent Crude (Energy costs)
    - STI Index (Overall market sentiment)
    """
    # Indicators: ^TNX (US 10Y), BZ=F (Brent Crude), ^STI (STI Index)
    indicators = {
        "US10Y": "^TNX",
        "Brent_Crude": "BZ=F",
        "STI_Index": "^STI"
    }

    results = {}
    for name, ticker in indicators.items():
        data = yf.Ticker(ticker)
        hist = data.history(period="5d")
        if not hist.empty:
            results[name] = {
                "current_price": hist['Close'].iloc[-1],
                "5d_change_pct": ((hist['Close'].iloc[-1] / hist['Close'].iloc[0]) - 1) * 100
            }

    return results


@mcp.tool()
def get_market_news(query: str = "Singapore Economy") -> list:
    """
    Fetches recent news headlines for a specific query to assess geopolitical/economic sentiment.
    """
    logging.info(f"[INFO] Searching news for: {query}")
    # Using yfinance news for the STI as a proxy for Singapore macro news
    sti = yf.Ticker("^STI")
    news_items = sti.news[:5]  # Get top 5 headlines

    formatted_news = []
    for item in news_items:
        formatted_news.append({
            "headline": item.get("title"),
            "publisher": item.get("publisher"),
            "link": item.get("link")
        })

    return formatted_news

if __name__ == "__main__":
    mcp.run()