CREATE TABLE tache (
    createur character varying,
    date_debut date,
    date_fin date,
    description character varying,
    etat character varying,
    id character varying,
    priorite character varying,
    percentage character varying,
    responsable character varying,
    titre character varying
);

ALTER TABLE public.tache OWNER TO ebat;

CREATE SEQUENCE tache_id_seq
    INCREMENT BY 1
    NO MAXVALUE
    NO MINVALUE
    CACHE 1;

ALTER TABLE public.tache_id_seq OWNER TO ebat;
