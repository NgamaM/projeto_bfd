--
-- PostgreSQL database dump
--

-- Dumped from database version 16.1
-- Dumped by pg_dump version 17.0

-- Started on 2026-01-20 10:38:56

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET transaction_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- TOC entry 4 (class 2615 OID 2200)
-- Name: public; Type: SCHEMA; Schema: -; Owner: -
--

CREATE SCHEMA public;


--
-- TOC entry 4813 (class 0 OID 0)
-- Dependencies: 4
-- Name: SCHEMA public; Type: COMMENT; Schema: -; Owner: -
--

COMMENT ON SCHEMA public IS 'standard public schema';


SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- TOC entry 218 (class 1259 OID 40976)
-- Name: categorias; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.categorias (
    id integer NOT NULL,
    nome_categoria character varying(100) NOT NULL,
    descricao text
);


--
-- TOC entry 217 (class 1259 OID 40975)
-- Name: categorias_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.categorias_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- TOC entry 4814 (class 0 OID 0)
-- Dependencies: 217
-- Name: categorias_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.categorias_id_seq OWNED BY public.categorias.id;


--
-- TOC entry 220 (class 1259 OID 40987)
-- Name: cores; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.cores (
    id integer NOT NULL,
    nome_cor character varying(50) NOT NULL
);


--
-- TOC entry 219 (class 1259 OID 40986)
-- Name: cores_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.cores_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- TOC entry 4815 (class 0 OID 0)
-- Dependencies: 219
-- Name: cores_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.cores_id_seq OWNED BY public.cores.id;


--
-- TOC entry 216 (class 1259 OID 40967)
-- Name: marcas; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.marcas (
    id integer NOT NULL,
    nome_marca character varying(100) NOT NULL,
    data_criacao date
);


--
-- TOC entry 215 (class 1259 OID 40966)
-- Name: marcas_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.marcas_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- TOC entry 4816 (class 0 OID 0)
-- Dependencies: 215
-- Name: marcas_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.marcas_id_seq OWNED BY public.marcas.id;


--
-- TOC entry 4645 (class 2604 OID 40979)
-- Name: categorias id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.categorias ALTER COLUMN id SET DEFAULT nextval('public.categorias_id_seq'::regclass);


--
-- TOC entry 4646 (class 2604 OID 40990)
-- Name: cores id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.cores ALTER COLUMN id SET DEFAULT nextval('public.cores_id_seq'::regclass);


--
-- TOC entry 4644 (class 2604 OID 40970)
-- Name: marcas id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.marcas ALTER COLUMN id SET DEFAULT nextval('public.marcas_id_seq'::regclass);


--
-- TOC entry 4805 (class 0 OID 40976)
-- Dependencies: 218
-- Data for Name: categorias; Type: TABLE DATA; Schema: public; Owner: -
--

INSERT INTO public.categorias VALUES (1, 'Trator', NULL);
INSERT INTO public.categorias VALUES (2, 'Colheitadeira', NULL);
INSERT INTO public.categorias VALUES (3, 'Pulverizador', NULL);


--
-- TOC entry 4807 (class 0 OID 40987)
-- Dependencies: 220
-- Data for Name: cores; Type: TABLE DATA; Schema: public; Owner: -
--

INSERT INTO public.cores VALUES (1, 'verde fosco');
INSERT INTO public.cores VALUES (2, 'amarelo insdustrial');
INSERT INTO public.cores VALUES (3, 'azul metalico');


--
-- TOC entry 4803 (class 0 OID 40967)
-- Dependencies: 216
-- Data for Name: marcas; Type: TABLE DATA; Schema: public; Owner: -
--

INSERT INTO public.marcas VALUES (1, 'John Deere', NULL);
INSERT INTO public.marcas VALUES (2, 'Massey Ferguson', NULL);
INSERT INTO public.marcas VALUES (3, 'New Holland', NULL);
INSERT INTO public.marcas VALUES (4, 'PA-14', NULL);


--
-- TOC entry 4817 (class 0 OID 0)
-- Dependencies: 217
-- Name: categorias_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.categorias_id_seq', 3, true);


--
-- TOC entry 4818 (class 0 OID 0)
-- Dependencies: 219
-- Name: cores_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.cores_id_seq', 3, true);


--
-- TOC entry 4819 (class 0 OID 0)
-- Dependencies: 215
-- Name: marcas_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.marcas_id_seq', 4, true);


--
-- TOC entry 4652 (class 2606 OID 40985)
-- Name: categorias categorias_nome_categoria_key; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.categorias
    ADD CONSTRAINT categorias_nome_categoria_key UNIQUE (nome_categoria);


--
-- TOC entry 4654 (class 2606 OID 40983)
-- Name: categorias categorias_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.categorias
    ADD CONSTRAINT categorias_pkey PRIMARY KEY (id);


--
-- TOC entry 4656 (class 2606 OID 40994)
-- Name: cores cores_nome_cor_key; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.cores
    ADD CONSTRAINT cores_nome_cor_key UNIQUE (nome_cor);


--
-- TOC entry 4658 (class 2606 OID 40992)
-- Name: cores cores_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.cores
    ADD CONSTRAINT cores_pkey PRIMARY KEY (id);


--
-- TOC entry 4648 (class 2606 OID 40974)
-- Name: marcas marcas_nome_marca_key; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.marcas
    ADD CONSTRAINT marcas_nome_marca_key UNIQUE (nome_marca);


--
-- TOC entry 4650 (class 2606 OID 40972)
-- Name: marcas marcas_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.marcas
    ADD CONSTRAINT marcas_pkey PRIMARY KEY (id);


-- Completed on 2026-01-20 10:38:56

--
-- PostgreSQL database dump complete
--

