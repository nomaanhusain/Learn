pragma solidity 0.8.10;

contract NomaanBank{
    mapping(address=>uint) public balances;

    //To deposit ether
    function deposit() external payable{
        balances[msg.sender]+=msg.value;
    }

    //allows multiple users to store ether in contract and withdraw ether back to their wallet
    //Note: Money can be sent back to ones own wallet only
    function withdraw(address payable addr,uint amount) public payable{
        require(balances[msg.sender] >= amount, "Balance not sufficient");
        //add ether to reciever
        (bool sent, bytes memory data) = addr.call{value: amount}("");
        require(sent,"Some error occured");
        //subtract ether from sender
        balances[msg.sender]-=amount;
    }

    //This function is used to send money to other's wallet
    function sendEther(address sender, address payable reciever, uint amount) public payable{
        require(balances[sender]>=amount,"Balance Insufficient");
        (bool sent, bytes memory data) = reciever.call{value: amount}("");
        require(sent,"Some error occured");
        balances[sender]-=amount;
    }

    //To check balance in contract
    function viewBalance() public view returns (uint){
        return address(this).balance;
    } 
}