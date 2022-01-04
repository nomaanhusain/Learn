///change this to whatever version of compiler you have
pragma solidity 0.8.10;

///Making a contract
contract NomaanContract1{
    uint public x=20;
    /// funtion to modify x, this requires 'gas fee' as it changes state
    function changeX(uint newX) public{
        x=newX;
    }
    ///maps like hashtable/dictonary, they have default getter in solidity
    ///'gas fee' is required as it changes state of contract
    mapping(uint => int) public map;
    function putMap(uint key, int value) public {
        map[key]=value;
    }
}
