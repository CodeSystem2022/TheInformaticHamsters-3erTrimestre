PGDMP         ;        
        {            test_bd    15.2    15.2     �           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false            �           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            �           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            �           1262    16398    test_bd    DATABASE     ~   CREATE DATABASE test_bd WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'Spanish_Argentina.1252';
    DROP DATABASE test_bd;
                postgres    false            �            1259    16399    persona    TABLE     �   CREATE TABLE public.persona (
    id_persona integer NOT NULL,
    nombre character varying,
    apellido character varying,
    email character varying
);
    DROP TABLE public.persona;
       public         heap    postgres    false            �            1259    16402    persona_id_persona_seq    SEQUENCE     �   CREATE SEQUENCE public.persona_id_persona_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 -   DROP SEQUENCE public.persona_id_persona_seq;
       public          postgres    false    214            �           0    0    persona_id_persona_seq    SEQUENCE OWNED BY     Q   ALTER SEQUENCE public.persona_id_persona_seq OWNED BY public.persona.id_persona;
          public          postgres    false    215            e           2604    16403    persona id_persona    DEFAULT     x   ALTER TABLE ONLY public.persona ALTER COLUMN id_persona SET DEFAULT nextval('public.persona_id_persona_seq'::regclass);
 A   ALTER TABLE public.persona ALTER COLUMN id_persona DROP DEFAULT;
       public          postgres    false    215    214            �          0    16399    persona 
   TABLE DATA           F   COPY public.persona (id_persona, nombre, apellido, email) FROM stdin;
    public          postgres    false    214   �
       �           0    0    persona_id_persona_seq    SEQUENCE SET     D   SELECT pg_catalog.setval('public.persona_id_persona_seq', 2, true);
          public          postgres    false    215            g           2606    16410    persona persona_pkey 
   CONSTRAINT     Z   ALTER TABLE ONLY public.persona
    ADD CONSTRAINT persona_pkey PRIMARY KEY (id_persona);
 >   ALTER TABLE ONLY public.persona DROP CONSTRAINT persona_pkey;
       public            postgres    false    214            �   ;   x�3��*M��H-J���* Q���9z���\F�ΉE9���7�����s��c���� ���     