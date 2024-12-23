DROP DATABASE database_name;
CREATE DATABASE database_name;
use database_name;

create table polzovateli (
	id INT AUTO_INCREMENT PRIMARY KEY,
	login varchar(25) not null unique,
	password varchar(25) not null unique
);

INSERT INTO polzovateli VALUES
('1','boba','dva'),
('2','ivan','odin');

CREATE TABLE material_type_import (
Material_type VARCHAR(30) PRIMARY KEY not null,
Material_scrap_percentage DOUBLE
);

INSERT INTO material_type_import VALUES
('Тип материала 1','0.1'),
('Тип материала 2','0.95'),
('Тип материала 3','0.28'),
('Тип материала 4','0.55'),
('Тип материала 5','0.34');

CREATE TABLE partners_import (
Partner_type TEXT,
Partner_name VARCHAR(30) PRIMARY KEY not null,
Director TEXT,
Partner_email TEXT,
Partners_phone_number TEXT,
Partners_legal_address TEXT,
TIN BIGINT(20),
Rating INT(11)
);

INSERT INTO partners_import VALUES
('ЗАО','База Строитель','Иванова Александра Ивановна','aleksandraivanova@ml.ru','493 123 45 67','652050, Кемеровская область, город Юрга, ул. Лесная, 15',2222455179,7),
('ООО','Паркет 29','Петров Василий Петрович','vppetrov@vl.ru','987 123 56 78','164500, Архангельская область, город Северодвинск, ул. Строителей, 18',3333888520,7),
('ПАО','Стройсервис','Соловьев Андрей Николаевич','ansolovev@st.ru','812 223 32 00','188910, Ленинградская область, город Приморск, ул. Парковая, 21',4440391035,7),
('ОАО','Ремонт и отделка','Воробьева Екатерина Валерьевна','ekaterina.vorobeva@ml.ru','444 222 33 11','143960, Московская область, город Реутов, ул. Свободы, 51',1111520857,5),
('ЗАО','МонтажПро','Степанов Степан Сергеевич','stepanov@stepan.ru','912 888 33 33','309500, Белгородская область, город Старый Оскол, ул. Рабочая, 122',5552431140,10);

CREATE TABLE product_type_import
(
Product_type VARCHAR(30) PRIMARY KEY not null,
Product_Type_Factor double
);

INSERT INTO product_type_import VALUES
('Ламинат','2.35'),
('Массивная доска','5.15'),
('Паркетная доска','4.34'),
('Пробковое покрытие','1.5');

CREATE TABLE products_import (
Product_type TEXT,
Product_name VARCHAR (120) PRIMARY KEY not null,
Article INT(11),
Minimum_cost_for_a_partner TEXT
);

INSERT INTO products_import VALUES
('Паркетная доска','Паркетная доска Ясень темный однополосная 14 мм',8758385,4456.9),
('Паркетная доска','Инженерная доска Дуб Французская елка однополосная 12 мм',8858958,7330.99),
('Ламинат','Ламинат Дуб дымчато-белый 33 класс 12 мм',7750282,1799.33),
('Ламинат','Ламинат Дуб серый 32 класс 8 мм с фаской',7028748,3890.41),
('Пробковое покрытие','Пробковое напольное клеевое покрытие 32 класс 4 мм',5012543,5450.59);

CREATE TABLE partner_products_import
(
id int PRIMARY KEY Auto_Increment not null,
Products VARCHAR (120) not null,
Partner_name VARCHAR(30) not null,
Number_of_products int(11),
Date_of_sale text,
FOREIGN KEY (Products) REFERENCES products_import (Product_name),
FOREIGN KEY (Partner_name) REFERENCES partners_import (Partner_name)
);

INSERT INTO partner_products_import (Products,Partner_name,Number_of_products,Date_of_sale) VALUES
('Паркетная доска Ясень темный однополосная 14 мм','База Строитель',15500,'03/23/2023'),
('Ламинат Дуб дымчато-белый 33 класс 12 мм','База Строитель',12350,'12/18/2023'),
('Ламинат Дуб серый 32 класс 8 мм с фаской','База Строитель',37400,'06/07/2024'),
('Инженерная доска Дуб Французская елка однополосная 12 мм','Паркет 29',35000,'12/02/2022'),
('Пробковое напольное клеевое покрытие 32 класс 4 мм','Паркет 29',1250,'05/17/2023'),
('Ламинат Дуб дымчато-белый 33 класс 12 мм','Паркет 29',1000,'06/07/2024'),
('Паркетная доска Ясень темный однополосная 14 мм','Паркет 29',7550,'07/01/2024'),
('Паркетная доска Ясень темный однополосная 14 мм','Стройсервис',7250,'01/22/2023'),
('Инженерная доска Дуб Французская елка однополосная 12 мм','Стройсервис',2500,'07/05/2024'),
('Ламинат Дуб серый 32 класс 8 мм с фаской','Ремонт и отделка',59050,'03/20/2023'),
('Ламинат Дуб дымчато-белый 33 класс 12 мм','Ремонт и отделка',37200,'03/12/2024'),
('Пробковое напольное клеевое покрытие 32 класс 4 мм','Ремонт и отделка',4500,'05/14/2024'),
('Ламинат Дуб дымчато-белый 33 класс 12 мм','МонтажПро',50000,'09/19/2023'),
('Ламинат Дуб серый 32 класс 8 мм с фаской','МонтажПро',670000,'11/10/2023'),
('Паркетная доска Ясень темный однополосная 14 мм','МонтажПро',35000,'04/15/2024'),
('Инженерная доска Дуб Французская елка однополосная 12 мм','МонтажПро',25000,'06/12/2024');

select * from polzovateli;
select * from material_type_import;
select * from partners_import;
select * from product_type_import;
select * from products_import;
select * from partner_products_import;
