-- sql/seed.sql
INSERT INTO users (first_name, last_name, email, phone, address_line1, city, state, pincode)
VALUES
('John','Doe','john@example.com','9999999999','Street 1','Chennai','TN','600001'),
('Mary','Jane','mary@example.com','8888888888','Street 2','Mumbai','MH','400001');

INSERT INTO user_bank_info (user_id, bank_name, account_number, ifsc, account_type)
VALUES (1,'HDFC','123456789','HDFC0001','Savings'), (2,'SBI','555666777','SBIN0002','Current');

INSERT INTO employment_info (user_id, company_name, designation, start_date, is_current, salary)
VALUES (1,'TCS','Developer','2020-01-01',true,25000), (2,'Infosys','Analyst','2019-05-10',true,30000);
