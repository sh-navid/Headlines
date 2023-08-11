-- --------------------------------------------------------------------------
-- IFNULL                                                                  --
-- --------------------------------------------------------------------------

DROP DATABASE IF EXISTS Test;
CREATE DATABASE Test;
USE Test;

DROP TABLE IF EXISTS Author;
CREATE TABLE IF NOT EXISTS Author(
    ID              INTEGER         NOT NULL    UNIQUE      AUTO_INCREMENT,
    Name            VARCHAR(100),
    PRIMARY KEY (ID)
);

INSERT INTO Author VALUES(NULL,"Hello");
INSERT INTO Author VALUES(NULL,"Bye");
INSERT INTO Author VALUES(NULL,"ByeBye");
INSERT INTO Author VALUES(NULL,"Foot");
INSERT INTO Author VALUES(NULL,NULL);
INSERT INTO Author VALUES(NULL,NULL);


SELECT ID, IFNULL(Name,"Not Defined") FROM Author;