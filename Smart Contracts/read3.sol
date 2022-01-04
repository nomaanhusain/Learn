pragma solidity 0.8.10;

contract NomaanContract1{
    ///to store the last sender to this contract
    address public lastSender;
    function recieve() external payable {
        ///msg is global variable used to access all info of the person that called this contract
        ///msg.value is also there to return amount of ether recieved
        /*whenever this function is called(i.e. money is sent to this contract)
        this will hold senders address*/ 
        lastSender = msg.sender;
    }

    function viewBalance() public view returns (uint){
        return address(this).balance;
    }
    ///function to enable the contract to pay ether back to people
    ///addr is address of the reciever, payable is necessary so as the function to know that money will be sent
    function pay(address payable addr, uint amount) public payable{
        //amount is in Wei, 1ETH = 10^18 Wei
        //there is a built in constant 'ether' with is equal to 10^18
        ///sent is true is transaction is successfull
        (bool sent, bytes memory data) =addr.call{value: amount}("");
        /// this is a fancy if statement
        ///if sent is false, then the message will be printed
        require(sent,"Error in sending ether");
    }
}