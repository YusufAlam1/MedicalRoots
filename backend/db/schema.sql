CREATE TYPE morpheme_type AS ENUM ('prefix', 'root', 'suffix', 'combining');

CREATE TABLE morpheme (
    id SERIAL PRIMARY KEY,
    root TEXT NOT NULL,
    type morpheme_type NOT NULL,
    translation TEXT NOT NULL,
    variant_spellings JSONB,
    image_url TEXT
);

CREATE TABLE term (
    id SERIAL PRIMARY KEY,
    term TEXT NOT NULL,
    normalized_term TEXT NOT NULL,
    definition TEXT,
    is_phrase BOOLEAN DEFAULT false,
    image_url TEXT
);

CREATE TABLE term_morpheme (
    id SERIAL PRIMARY KEY,
    term_id INT REFERENCES term(id) ON DELETE CASCADE,
    morpheme_id INT REFERENCES morpheme(id) ON DELETE CASCADE,
    seq INT NOT NULL,
    start_idx INT,
    end_idx INT,
    realized_form TEXT
);

CREATE TYPE language_name AS ENUM ('Greek', 'Latin', 'Roman', 'Other');

CREATE TABLE language (
    id SERIAL PRIMARY KEY,
    name language_name NOT NULL,
    notes TEXT
);

CREATE TYPE system_name AS ENUM (
    'Cardiovascular',
    'Digestive',
    'Endocrine',
    'Immune',
    'Integumentary',
    'Lymphatic',
    'Muscular',
    'Nervous',
    'Reproductive',
    'Respiratory',
    'Skeletal',
    'Urinary'
);

CREATE TABLE system (
    id SERIAL PRIMARY KEY,
    name system_name NOT NULL
);

ALTER TABLE morpheme ADD COLUMN language_id INT REFERENCES language(id);
ALTER TABLE term ADD COLUMN system_id INT REFERENCES system(id);