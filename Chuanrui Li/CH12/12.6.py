How would you test an ATM in a distributed banking system?

Here are a few test cases for how to test just the withdrawing functionality:
single machine
» Withdrawing money less than the account balance
» Withdrawing money greater than the account balance
» Withdrawing money equal to the account balance

multiple proccess
» Withdrawing money from an ATM and from the internet at the same time
» Withdrawing money when the connection to the bank’s network is lost
» Withdrawing money from multiple ATMs simultaneously --> transfer or withdrawing from diff ATM


