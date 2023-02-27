CREATE TABLE IF NOT EXISTS company (
    company_id VARCHAR(20) NOT NULL,
    products json,
    PRIMARY KEY(company_id)
);

CREATE TABLE IF NOT EXISTS company (
    company_id VARCHAR(20) NOT NULL,
    PRIMARY KEY(company_id)
);

INSERT into company VALUES ('claro_11');

CREATE TABLE IF NOT EXISTS products (
    id VARCHAR(20) NOT NULL,
    value DOUBLE PRECISION NOT NULL,
    id_company VARCHAR(20) NOT NULL,
    PRIMARY KEY(id),
    FOREIGN KEY (id_company) REFERENCES company(company_id)
);

INSERT into products (id, value, id_company) VALUES ('claro_20', 10, 'claro_11');
INSERT into products (id, value, id_company) VALUES ('claro_50', 50, 'claro_11');
INSERT into products (id, value, id_company) VALUES ('claro_99', 99.0, 'claro_11');



CREATE TABLE IF NOT EXISTS recharges (
    recharge_id VARCHAR(36),
    created_at VARCHAR NOT NULL,
    phone_number VARCHAR(13) NOT NULL,
    product_id VARCHAR(20) NOT NULL,
    PRIMARY KEY(recharge_id),
    FOREIGN KEY (product_id) REFERENCES products(id)
);

INSERT into recharges (recharge_id, created_at, phone_number, product_id) VALUES ('bd65600d-8669-4903-8a14-af88203add38', '2019-02-01T13:00:00.000Z' ,'5511999999999', 'claro_50');

INSERT into recharges (recharge_id, created_at, phone_number, product_id) VALUES ('7a3fd8e8-2317-44d2-aff3-93e6cba119e9', '2020-02-01T13:00:00.000Z' ,'5511899998888', 'claro_99');

INSERT into recharges (recharge_id, created_at, phone_number, product_id) VALUES ('0be28cc4-7776-4339-9d02-325fae1b6084', '2020-02-01T13:00:00.000Z' ,'5511899998888', 'claro_99');