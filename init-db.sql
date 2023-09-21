CREATE TABLE IF NOT EXISTS
users(
    id INTEGER PRIMARY KEY UNIQUE NOT NULL,
    login VARCHAR(15) UNIQUE NOT NULL,
    money_amount INTEGER NOT NULL,
    card_number VARCHAR(16) UNIQUE NOT NULL,
    status BOOLEAN NOT NULL DEFAULT TRUE
);

INSERT INTO users VALUES
    (1, 'admin', 1000000, '9999999999999999', True),
    (2, 'fish', 0, '5565640418306493', True),
    (3, 'user', 1000, '4916927901302769', True),
    (4, 'student', 100, '375542539971448', False),
    (5, 'wiener', 777, '4556486537735756', False),
    (6, 'carlos', 777, '5143627838129200', False)
;

CREATE TABLE IF NOT EXISTS
passwords(
    id INTEGER PRIMARY KEY UNIQUE NOT NULL,
    password VARCHAR(15) NOT NULL
);

INSERT INTO passwords VALUES
    (1, 'admin'),
    (2, 'champion'),
    (3, 'qwerty'),
    (4, 'NeverSayVmik'),
    (5, 'peter'),
    (6, 'montoya')
;