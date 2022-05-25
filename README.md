### Telco Classification Project

#### Project Goals:
Construct a classification model to predict customer churn
Forcast future churn with enhanced accuracy
Presenting insightful company recommendations
Empower executives to improve the current trajectory of customer churn
Thoroughly document the process and key findings

#### Initial Hypotheses:
I predict contract_type, payment_type, internet_type, and tenure may be drivers of churn. For internet type, I predict fiber optic customers may be churning due to dissatisfaction with the service which may be correlated with tenure.

#### Data Dictionary: 

Unnamed: 0 int64
-this is the unique id with 7043 unique values. will need this later for .csv, but will drop in preparation for now

contract_type_id int64
-there are 3 contract types here that are represented numerically
1 - month to month contract
2 - 1 year contract
3 - 2 year contract

payment_type_id int64
-there are 4 types of payments that are represented numerically
1 - electronic check
2 - mailed check
3 - bank transfer
4 - credit card (automatic)

internet_service_type_id int64
-there are 3 types of internet service that are represented numerically
1 - DSL
2 - fiber optic
3 - no internet service

customer_id object
-there are 7043 customer ids each representing a unique customer

gender object
- there are two gender types "male" and "female"

senior_citizen int64
- senior citizens are represented numerically
1 - is a senior citizen
0 - is not a senior citizen

partner object
- whether or not the customer has a partner is represented by "No" and "Yes"

dependents object
- whether or not the customer has dependent(s) is represented by "No" and "Yes"

tenure int64
- customer tenure is represented numerically in the amount of months a customer has been at Telco

phone_service object
- whether or not the customer has phone service is represented by "No" and "Yes"

multiple_lines object
- whether or not the customer has multiple lines is represented by "No", "Yes", and "No phone service"

online_security object
- whether or not the customer has online sercurity is represented by "No", "Yes", and "No internet service"

online_backup object
- whether or not the customer has online backup is represented by "No", "Yes", and "No internet service"

device_protection object
- whether or not the customer has device protection is represented by "No", "Yes", and "No internet service"

tech_support object
- whether or not the customer has tech support is represented by "No", "Yes", and "No internet service"

streaming_tv object
- whether or not the customer has tv streaming is represented by "No", "Yes", and "No internet service"

streaming_movies object
- whether or not the customer has movie streaming is represented by "No", "Yes", and "No internet service"

paperless_billing object
- whether or not the customer has paperless billing is represented by "No" and "Yes"

monthly_charges float64
- the customer's average monthly charges is represented numerically

total_charges object
- the customer's all time charges is represented as an object data type, but can be viewed numerically

churn object
- whether or not a customer has churned is represented by "Yes" and "No"

internet_service_type object
- there are 3 internet service options: "Fiber optic", "DSL", and "None"

payment_type object
- there are 4 payment methods:
"Electronic check", "Mailed check", "Bank transfer (automatic)", "Credit card (automatic)"

contract_type object
- there are 3 contract types: "Month-to-month", "Two year", "One year"

#### Project Planning (lay out your process through the data science pipeline):

data acquistion, preparation, exploratory data analysis and statistical testing, modeling, and model evaluation

#### Key Findings, Recommendations, and Takeaways

My analysis indicates that the top drivers of customer churn are:

month-to-month contract type
electronic check payment type
fiber optic internet service
higher monthly charges
Top drivers of customer loyalty are:

two year contract type
higher tenure
I contructed and trained a random forest classification model which is able to predict churn with 82% accuracy (9% better accuracy than baseline).

Summary of Recommendations:
By utilizing this model and considering the drivers customer churn & retention, I can recommend the following with reasonable confidence:

Prefered Plan: Proactively reach out to customers that are predicted to churn (use predictions.csv in this repository for specific customers and churn prediction). Address any concerns with awareness to top drivers of churn. Make the customer's life easier (and our churn rate lower), by helping them switch to our prefered two-year auto-pay plan.

Incentivize loyalty: As customers on a two year contract have very low churn, we need switch as many month-to-month payers over as possible. We should offer at least one perk (ie. a complimentary 6 months of device protection and/or streaming services) for customers that switch to autopay.

Offer Pausing Service: For month-to-month customers resistant to change, implement the option to pause service for up to 6 months. This will buy time to retain these customers and slow down churn.