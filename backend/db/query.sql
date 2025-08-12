SELECT m.root,
    m.type,
    m.translation,
    l.name
FROM morpheme m
    JOIN language l ON m.language_id = l.id
WHERE l.name = 'Greek';

SELECT m.root,
    m.type,
    m.translation,
    tm.seq
FROM term t
    JOIN term_morpheme tm ON t.id = tm.term_id
    JOIN morpheme m ON tm.morpheme_id = m.id
WHERE t.term = 'Hypoglycemia'
ORDER BY tm.seq;