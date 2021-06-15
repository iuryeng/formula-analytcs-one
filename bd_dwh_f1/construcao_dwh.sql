

/* SCRIPT CRIAÇÃO DA BASE DE DWH_FORMULA1 */
CREATE DATABASE DWH_FORMULA1;

/* SCRIPT CRIAÇÃO DA TABELA DIMENSÃO PILOTOS */
CREATE TABLE dim_pilotos (
    id_piloto INTEGER PRIMARY KEY,
    ref_piloto VARCHAR (50) NOT NULL,
    code_piloto VARCHAR (5),
    primeiro_nome VARCHAR(50) NOT NULL,
    ultimo_nome VARCHAR(50) NOT NULL,
    nascimento DATE,
    nacionalidade_piloto VARCHAR (50)
);

/* SCRIPT CRIAÇÃO DA TABELA DIMENSÃO CORRIDAS */
CREATE TABLE dim_corridas (
    id_corrida INTEGER PRIMARY KEY,    
    nome_corrida VARCHAR(100) NOT NULL,
    data_corrida DATE NOT NULL,
    duracao_corrida TIME,
    temporada VARCHAR (50)
);

/* SCRIPT CRIAÇÃO DA TABELA DIMENSÃO CIRCUITOS */
CREATE TABLE dim_circuitos (
    id_circuito INTEGER PRIMARY KEY,
    ref_circuito VARCHAR (100) NOT NULL,
    nome_circuito VARCHAR (100) NOT NULL,
    localizacao VARCHAR (100) NOT NULL,
    pais VARCHAR (50)
);

/* SCRIPT CRIAÇÃO DA TABELA DIMENSÃO CONSTRUTORES */
CREATE TABLE dim_construtores (
    id_construtor INTEGER PRIMARY KEY,
    nome_construtor VARCHAR (50) NOT NULL,
    nacionalidade_construtor VARCHAR (50),
    fabricante_motor VARCHAR (50)
     
);

CREATE TABLE dim_tempo (
	id_tempo INTEGER PRIMARY KEY,
	dia_semana VARCHAR (50),
	dia_mes INTEGER (2),
	dia_ano INTEGER (3),
	mes INTEGER (2),
	decada INTEGER (2)
);


/* SCRIPT CRIAÇÃO DA TABELA FATO RESULTADOS */
CREATE TABLE fato_resultados (   
    id_corrida INTEGER NOT NULL,
    id_piloto INTEGER NOT NULL,
    id_construtor INTEGER NOT NULL,
    id_circuito INTEGER NOT NULL,
    id_tempo INTEGER NOT NULL, 
    temporada VARCHAR (50),   
    grid INTEGER NOT NULL,
    pontos_ganhos FLOAT NOT NULL,
    qtd_voltas INTEGER NOT NULL,
    ranking INTEGER,  
    ordem_posicao INTEGER NOT NULL,    
    voltas INTEGER NOT NULL,
    tempo_de_prova VARCHAR (50),    
   
    FOREIGN KEY (id_corrida) REFERENCES dim_corridas (id_corrida),
    FOREIGN KEY (id_piloto) REFERENCES dim_pilotos (id_piloto),
    FOREIGN KEY (id_construtor) REFERENCES dim_construtores (id_construtor),
    FOREIGN KEY (id_circuito) REFERENCES dim_circuitos (id_circuito),
    FOREIGN KEY (id_tempo) REFERENCES dim_tempo (id_tempo)
);
