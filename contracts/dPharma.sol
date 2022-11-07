// SPDX-License-Identifier: GPL-3.0-only
pragma solidity >=0.5.0 <0.9.0;

// import "./Structs.sol";

contract dPharma {

    struct Node {
        uint node_id;
        address add;
        uint ntype; // 0: Hospital, 1: Warehouse, 2: Factory
        uint x;
        uint y;
    }

    struct Stock {
        bytes32 serial;
        string name;
        Node location;
        uint stype; // Stock type: Drug, Equipment, etc
        uint qty;
        uint ppu; // Price per unit
        bool is_rx; // Requires prescription or not?
        string batch;
        string date; // yyyymmdd
        uint expiry; // Days
    }

    struct Order {
        uint order_id;
        address buyer;
        address seller;
        Stock ostock;
        uint price;
        Node[] path;
        uint[] status;
    }

    mapping (uint => Node) total_nodes; // Mapping of all available nodes (node_id => Node)
    uint num_nodes;
    mapping (uint => Stock[]) total_stock; // Mapping of Stocks stored at a particular Node (node_id => Stock[])

    mapping (address => mapping (uint => Order)) customer_map; // Orders for hospital (address<hospital> => (order_id => Order))
    uint num_orders;
    mapping (address => Order[]) manufacturer_map; // Orders for manufacturer (address<manufacturer> => Order)

    function updateOrder(address buy, uint order_no, uint xloc, uint yloc, uint days_elapsed) public {
        for (uint i=0; i<customer_map[buy][order_no].path.length; i++) {
            if ((customer_map[buy][order_no].path[i].x == xloc) && (customer_map[buy][order_no].path[i].y == yloc)) {
                customer_map[buy][order_no].status[i] = days_elapsed;
                break;
            }
        }
    }

    function fetchUser(address add) public view returns(uint){
        for (uint i=0; i<num_nodes; i++) {
            if (total_nodes[i].add == add) {
                return total_nodes[i].ntype;
            }
        }
        return 3;
    }

//     function createOrder(address buyer, address seller, Stock ostock, Path[] path, ) public {}
//
//     function createListing() public {}

    function createNode(uint node_id, uint ntype, uint x, uint y) public {
        total_nodes[num_nodes++] = Node(node_id, msg.sender, ntype, x, y);
    }

}
