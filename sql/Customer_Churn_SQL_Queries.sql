
/* CUSTOMER CHURN ANALYSIS SQL QUERIES*/


/* Query 1: Total Customers*/
SELECT COUNT(*) AS Total_Customers
FROM customer_churn;



/* Query 2: Churn Customers*/
SELECT COUNT(*) AS Churn_Customers
FROM customer_churn
WHERE Churn = 'Yes';



/* Query 3: Active Customers*/
SELECT COUNT(*) AS Active_Customers
FROM customer_churn
WHERE Churn = 'No';


/* Query 4: Churn Rate (%)*/
SELECT
ROUND(
COUNT(CASE WHEN Churn='Yes' THEN 1 END) * 100.0 / COUNT(*),
2
) AS Churn_Rate
FROM customer_churn;


/* Query 5: Gender Distribution*/
SELECT
gender,
COUNT(*) AS Customers
FROM customer_churn
GROUP BY gender;



/* Query 6: Churn by Gender*/
SELECT
gender,
Churn,
COUNT(*) AS Customers
FROM customer_churn
GROUP BY gender, Churn;



/*Query 7: Customers by Contract Type*/
SELECT
Contract,
COUNT(*) AS Customers
FROM customer_churn
GROUP BY Contract;


/*Query 8: Churn by Contract Type*/
SELECT
Contract,
Churn,
COUNT(*) AS Customers
FROM customer_churn
GROUP BY Contract, Churn;


/* Query 9: Customers by Internet Service*/
SELECT
InternetService,
COUNT(*) AS Customers
FROM customer_churn
GROUP BY InternetService;



/*Query 10: Churn by Internet Service*/
SELECT
InternetService,
Churn,
COUNT(*) AS Customers
FROM customer_churn
GROUP BY InternetService, Churn;


/*Query 11: Average Monthly Charges*/
SELECT
ROUND(AVG(MonthlyCharges),2) AS Average_Monthly_Charges
FROM customer_churn;


/*Query 12: Average Total Charges*/
SELECT
ROUND(AVG(TotalCharges),2) AS Average_Total_Charges
FROM customer_churn;


/* Query 13: Average Tenure*/
SELECT
ROUND(AVG(tenure),2) AS Average_Tenure
FROM customer_churn;


/* Query 14: Senior Citizens Count*/
SELECT
SeniorCitizen,
COUNT(*) AS Customers
FROM customer_churn
GROUP BY SeniorCitizen;


/* Query 15: Churn by Senior Citizen*/
SELECT
SeniorCitizen,
Churn,
COUNT(*) AS Customers
FROM customer_churn
GROUP BY SeniorCitizen, Churn;



/* Query 16: Payment Method Distribution*/
SELECT
PaymentMethod,
COUNT(*) AS Customers
FROM customer_churn
GROUP BY PaymentMethod;


/* Query 17: Churn by Payment Method*/
SELECT
PaymentMethod,
Churn,
COUNT(*) AS Customers
FROM customer_churn
GROUP BY PaymentMethod, Churn;



/* Query 18: Top 10 Highest Monthly Charges*/
SELECT
customerID,
MonthlyCharges
FROM customer_churn
ORDER BY MonthlyCharges DESC
LIMIT 10;


/*Query 19: Top 10 Highest Total Charges*/
SELECT
customerID,
TotalCharges
FROM customer_churn
ORDER BY TotalCharges DESC
LIMIT 10;



/*Query 20: Customers with Tenure Greater Than 60 Months*/
SELECT
customerID,
tenure,
MonthlyCharges,
TotalCharges
FROM customer_churn
WHERE tenure > 60
ORDER BY tenure DESC;
