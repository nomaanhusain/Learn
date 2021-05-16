import java.util.Arrays;

public class Block {
	private String[] transactions;
	//Hashcode of current block
	private int blockHashCode;
	//Hashcode of previous block
	private int previousBlockHashCode;
	
	
	public Block(String[] transactions, int previousBlockHashCode) {
		super();
		this.transactions = transactions;
		this.previousBlockHashCode = previousBlockHashCode;
		//Calculation of current hashcode
		this.blockHashCode=Arrays.hashCode(new int[] {Arrays.hashCode(transactions),previousBlockHashCode});
	}
	public String[] getTransactions() {
		return transactions;
	}
	public void setTransactions(String[] transactions) {
		this.transactions = transactions;
	}
	public int getBlockHashCode() {
		return blockHashCode;
	}
	public void setBlockHashCode(int blockHashCode) {
		this.blockHashCode = blockHashCode;
	}
	public int getPreviousBlockHashCode() {
		return previousBlockHashCode;
	}
	public void setPreviousBlockHashCode(int previousBlockHashCode) {
		this.previousBlockHashCode = previousBlockHashCode;
	}
	@Override
	public String toString() {
		return "Block [transactions=" + Arrays.toString(transactions) + ", blockHashCode=" + blockHashCode
				+ ", previousBlockHashCode=" + previousBlockHashCode + "]";
	}
}
