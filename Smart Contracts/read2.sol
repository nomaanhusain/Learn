pragma solidity 0.8.10;

///Here we actually perform some monetary transactions
contract NomaanContract1{
    ///external means function cannot be called from within the contract
    ///payable means this recieves ether, adds ether to the contract
    function recieve() external payable {}

    ///function to view current balance of this smart contract
    ///'view' means this function is read-only, cannot perform state changes
    function viewBalance() public view returns (uint){
        ///address(this) gives the address of the smart contract
        ///a property 'balance' is associated with each smart contract that holds its value
        return address(this).balance;
    }
}