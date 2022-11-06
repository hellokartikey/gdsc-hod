# dPharma

Pharma - SLAs, Traceability & Safety

## Tech Specs

1. dPharma etherium smart contract
    1. struct Nodes array:
        * Hospital (0)
        * Warehouses (1)
        * Factory (2)
    1. struct Stock:
        * serial
        * name
        * location Node
        * type
        * qty
        * ppu
        * category
        * batch_no
        * mfg_date
        * expiry
    1. Total_Stocks = array Stock
    1. Orders mapping: (address(Hospital) => (order_no => struct Order))
    1. struct Order
        * Stock
        * price
    1. order_no = unique id generated for each order placed

1. Backend Flask and JS
    1. Route calculation
    1. Updation of orders (Distributors)
    1. Updation of stocks (Manufacturers)
    1. Placement of orders (Hospitals)
