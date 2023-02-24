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