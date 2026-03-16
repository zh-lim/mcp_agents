### Instructions
To provide instructions for the specialist to run macro market analysis using the *sgx_service*

### Logic
1. Step 1: The Specialist calls get_macro_indicators().
2. Step 2: It notices the US10Y yield is rising.
3. Step 3: It calls get_market_news("Fed Interest Rates").
4. Step 4: It synthesizes this into a "Bearish" or "Cautionary" stance for the SGX Analyst, specifically warning about REIT valuations.