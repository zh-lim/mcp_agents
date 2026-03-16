## Name: SGX Stock Advisor

### Intent:
To provide a comprehensive "Buy/Hold/Avoid" recommendation for SGX-listed equities by synthesizing dividend data, fundamental growth, and external market pressures.

### Runbook
1. **Trigger**: Receive a ticker or a sector (e.g., REITs, Banks).
2. **Phase 1**: Delegate to SGX_Analyst to check yield sustainability.
3. **Phase 2**: Delegate to Growth_Specialist to evaluate capital appreciation potential.
4. **Phase 3**: Delegate to Macro_Strategist to cross-reference with current interest rates (SORA), US-China relations, and ASEAN trade trends.
5. **Phase 4**: USe the Synthesizer Synthesize all findings into a final report, filtered through the Guardrails.
