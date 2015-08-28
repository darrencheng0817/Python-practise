Select TenantName
FROM Tenants
INNER JOIN
(	Select Tenants
	FROM AptTenants
	GROUP BY TenantID
	HAVING cout(*) > 1) C
ON Tenants.TenantID = C.TenantID;

-- Whenever you write a GROUP BY clause -> HAVING && SELECT clause is an aggregate function

