-- Show the total sum of all polices by policy type

SELECT PolicyType, SUM(Balance) AS TotalSum
FROM Policy
GROUP BY PolicyType;


-- Show the total of sum of all account transactions for each account by transaction type (TranTypeId)
SELECT Account.Id, TranTypeId, SUM(Amount) AS TotalSum
FROM Account
JOIN AccTran ON Account.Id = AccTran.AccountId
GROUP BY Account.Id, TranTypeId;


-- Show a breakdown of each policy balance by account
SELECT Account.Name, Policy.Id, Policy.Balance
FROM Account
JOIN Policy ON Account.Id = Policy.AccountId
ORDER BY Account.Name;



-- Show all policies whose balance does not equal the sum of their respective AccTran transactions, sort by account name
SELECT Policy.Id, Account.Name, Policy.Balance, SUM(AccTran.Amount) AS TotalAmount
FROM Policy
JOIN Account ON Policy.AccountId = Account.Id
JOIN AccTran ON Policy.Id = AccTran.PolicyId
GROUP BY Policy.Id, Account.Name, Policy.Balance
HAVING Policy.Balance != TotalAmount
ORDER BY Account.Name;

