pragma solidity >=0.5.0 <0.9.0;

contract Structs {
    struct Node {
        uint ntype {}; // 0: Hospital, 1: Warehouse, 2: Factory
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
        address buyer;
        address seller;
        Stock ostock;
        uint price;
        Node[] path;
        uint[] status;
    }
}
