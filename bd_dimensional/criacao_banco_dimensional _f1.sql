/* CRIAÇÃO DO BANCO DIMENSIONAL */
CREATE DATABASE DW_F1;
USE DW_F1;

/* CRIAÇÃO DAS DIMENSÕES DO
   DATA WAREHOUSE
   FORMULA ANALITICYS ONE
 */

/* CRIAÇÃO DIMENSÃO CIRCUITOS */
CREATE TABLE dim_circuitos (
    id_circuito INTEGER PRIMARY KEY,
    ref_circuito VARCHAR(100) NOT NULL,
    nome_circuito VARCHAR(100) NOT NULL,
    localizacao_circuito VARCHAR(100) NOT NULL,
    pais_circuito varchar (50) NOT NULL
);

/* CRIAÇÃO DIMENSÃO CORRIDAS */
CREATE TABLE dim_corridas (
    id_corrida INTEGER PRIMARY KEY,
    nome_gp VARCHAR(50) NOT NULL,
    data_gp DATE NOT NULL,
    horario_gp TIME NOT NULL,
    temporada VARCHAR(10) NOT NULL
);

/* CRIAÇÃO DIMENSÃO CONSTRUTORES */
CREATE TABLE dim_construtores (
    id_construtor INTEGER PRIMARY KEY,
    nome_construtor VARCHAR(50) NOT NULL,
    nacionalidade_construtor DATE NOT NULL
);

/* CRIAÇÃO DIMENSÃO PILOTOS */
CREATE TABLE dim_pilotos (
    id_piloto INTEGER PRIMARY KEY,
    ref_piloto VARCHAR(50) NOT NULL,
    code_piloto VARCHAR(5) NOT NULL,
    primeiro_nome VARCHAR(50) NOT NULL,
    ultimo_nome VARCHAR(50) NOT NULL,
    nacionalidade VARCHAR(50) NOT NULL,
    data_nascimento DATE NOT NULL
);

/* CRIAÇÃO DIMENSÃO TEMPO */
CREATE TABLE dim_tempo (
    id_tempo INTEGER PRIMARY KEY,
    decada VARCHAR(10) NOT NULL,
    ano VARCHAR(10) NOT NULL,
    mes_do_ano VARCHAR(10) NOT NULL,
    dia_do_mes VARCHAR(10) NOT NULL,
    dia_do_ano VARCHAR(50) NOT NULL
);

/* CRIAÇÃO FATO RESULTADOS */
CREATE TABLE fato_resultados (
    id_resultado INTEGER NOT NULL,
    id_construtor INTEGER NOT NULL,
    id_piloto INTEGER NOT NULL,
    id_corrida INTEGER NOT NULL,
    id_circuito INTEGER NOT NULL,
    id_tempo INTEGER NOT NULL,
    temporada VARCHAR(10) NOT NULL,
    pontos_ganhos INTEGER NOT NULL,
    qtd_voltas INTEGER NOT NULL,
    grid INTEGER NOT NULL,
    ordem_posicao INTEGER NOT NULL,
    ranking INTEGER,
    tempo_de_prova VARCHAR(50),
    status VARCHAR(50) NOT NULL,
    FOREIGN KEY (id_construtor) REFERENCES dim_construtores (id_construtor),
    FOREIGN KEY (id_piloto) REFERENCES dim_pilotos (id_piloto),
    FOREIGN KEY (id_circuito) REFERENCES dim_circuitos (id_circuito),
    FOREIGN KEY (id_corrida) REFERENCES dim_corridas (id_corrida),
    FOREIGN KEY (id_tempo) REFERENCES dim_tempo (id_tempo)
);