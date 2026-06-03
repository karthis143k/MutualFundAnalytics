 Data Dictionary

 01_fund_master.csv
- amfi_code : Unique scheme identifier
- scheme_name : Name of scheme
- fund_house : AMC name
- category : Fund category
- plan : Direct/Regular plan

 02_nav_history.csv
- amfi_code : Scheme identifier
- date : NAV date
- nav : Net Asset Value

 03_aum_by_fund_house.csv
- fund_house : AMC name
- aum_crore : Assets under management

 07_scheme_performance.csv
- return_1yr_pct : 1-year return %
- return_3yr_pct : 3-year return %
- return_5yr_pct : 5-year return %
- alpha : Alpha metric
- beta : Beta metric
- sharpe_ratio : Sharpe ratio
- expense_ratio_pct : Expense ratio %

 08_investor_transactions.csv
- investor_id : Investor identifier
- transaction_date : Transaction date
- transaction_type : SIP/Lumpsum/Redemption
- amount_inr : Transaction amount
- state : Investor state
- kyc_status : KYC verification status