pragma solidity >=0.5.0 <0.9.0;

import "./Structs.sol";

contract dPharma {

    mapping (Node => Stock[]) total_stock;
    mapping (address => mapping (uint => Order)) customer_map; // Orders for hospital
    mapping (address => Order[]) manufacturer_map; // Orders for manufacturer

    function updateOrder(address buy, address sell, uint order_no, uint index, uint days_elapsed) public {
        cystomer_map[]
    }

    function createOrder() public {}

    function createListing() public {}

}
