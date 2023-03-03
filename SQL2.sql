-- Creating and using the present database called turma_615
CREATE DATABASE IF NOT EXISTS turma_615;
USE turma_615;

CREATE TABLE IF NOT EXISTS students(
	matricula INT (5) NOT NULL PRIMARY KEY, -- nome da variavel, tipo, tamanho
    nome VARCHAR(30),
    email VARCHAR(50)
);

SELECT * FROM students;

-- Adicionando colunas 
ALTER TABLE students ADD(
	telefone VARCHAR(9),
    course VARCHAR(30)
);

-- Alterando nomes
ALTER TABLE students MODIFY telefone varchar(11);
ALTER TABLE students RENAME estudantes;
ALTER TABLE estudantes RENAME COLUMN course TO curso;

-- Inserindo dados na tabela
INSERT INTO estudantes (matricula,nome,email,telefone, curso)
VALUES (14918,'Gabriel','Gabriel@email.com','12345678999','Data Science');

SELECT *FROM estudantes;

-- Matricula alto incrementada
ALTER TABLE estudantes MODIFY matricula INT (5) NOT NULL AUTO_INCREMENT;

-- Inserindo dados na tabela
INSERT INTO estudantes (nome,email,telefone, curso)
VALUES ('Lucas','Lucas@email.com','12345678998','Full Stack');
INSERT INTO estudantes (nome, email, telefone, curso) 
VALUES ('Guilherme', 'Gui@email', '12345678999', 'DS');
INSERT INTO estudantes (nome, email, telefone, curso) 
VALUES ('Camila', 'Ca@email', '12345678999', 'DS');

-- Atualizando os dados
UPDATE estudantes SET curso = 'Data Science' WHERE curso = 'DS';
UPDATE estudantes SET email = 'Camila@email.com' WHERE email = 'Ca@email';
UPDATE estudantes SET email = 'Guilherme@email.com' WHERE email = 'Gui@email';

-- Ordenando
SELECT *FROM estudantes ORDER BY matricula; 	
SELECT *FROM estudantes WHERE curso = 'Full Stack';

ALTER TABLE estudantes ADD(
	idade int(3)
);

UPDATE estudantes SET idade = 22 WHERE Matricula = 14918;
UPDATE estudantes SET idade = 24 WHERE Matricula = 14919;
UPDATE estudantes SET idade = 26 WHERE Matricula = 14920;
UPDATE estudantes SET idade = 32 WHERE Matricula = 14921;

SELECT matricula,nome,idade from estudantes where idade > 25;
SELECT CAST(FLOOR (AVG(idade)) AS SIGNED) AS 'Média das idades' from estudantes;
SELECT COUNT(*) from estudantes;
