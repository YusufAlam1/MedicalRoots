-- Languages
INSERT INTO language (name, notes)
VALUES
('Greek', 'Most morphemes here are of Greek origin');

-- Systems
INSERT INTO system (name)
VALUES
('Endocrine');

-- Morphemes
INSERT INTO morpheme (root, type, translation, variant_spellings, image_url, language_id)
VALUES
('hypo', 'prefix', 'low/below/insufficient', '[]', '/images/hypo.png', 1),
('glyc', 'root', 'sugar/glucose', '["glyco"]', '/images/glucose.png', 1),
('emia', 'suffix', 'blood condition', '["haemia"]', '/images/blood_cond.png', 1);

-- Term
INSERT INTO term (term, normalized_term, definition, is_phrase, image_url, system_id)
VALUES
('Hypoglycemia', 'hypoglycemia', 'Abnormally low level of glucose in the blood', false, '/images/hypoglycemia.png', 1);

-- Term-Morpheme links
INSERT INTO term_morpheme (term_id, morpheme_id, seq, start_idx, end_idx, realized_form)
VALUES
(1, 1, 1, 0, 4, 'hypo'),   -- hypo
(1, 2, 2, 4, 8, 'glyc'),   -- glyc
(1, 3, 3, 8, 12, 'emia');  -- emia
