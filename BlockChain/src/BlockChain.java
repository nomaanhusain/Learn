import java.util.ArrayList;

public class BlockChain {
	public static void main(String[] args) {

		// TODO Auto-generated method stub
		ArrayList<Block> myBlockChain = new ArrayList<Block>();
		String[] initialValues = { "Nomaan has 550", "Raj has 600" };
//		this is the first block of the blockchain, as no previous block exists, prev block val is 0
		Block firstBlock = new Block(initialValues, 0);
		// Add block to blockchain
		myBlockChain.add(firstBlock);
		System.out.println("-->>"+myBlockChain.toString());
		
		//Block two
		String[] blockTwoValues = { "Nomaan has 650", "Raj has 500" };
		Block secondBlock = new Block(blockTwoValues, firstBlock.getBlockHashCode());
		myBlockChain.add(secondBlock);
		System.out.println("-->>"+myBlockChain.toString());
	}
}
