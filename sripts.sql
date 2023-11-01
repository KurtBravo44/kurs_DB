CREATE TABLE employers
(
	company_id int PRIMARY KEY,
	company_name varchar(100) NOT NULL
)

CREATE TABLE vacs
(
	vac_id serial PRIMARY KEY,
	title varchar(100) NOT NULL,
	company_id int REFERENCES employers(employer_id),
	salary_from int,
	salary_to int,
	url varchar(100)
)