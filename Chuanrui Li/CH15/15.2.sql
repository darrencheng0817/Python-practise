-- updating the data
UPDATE Requests
SET status = "Closed"
WHERE AptID IN(
	Select AptID
	FROM Apartments

)

