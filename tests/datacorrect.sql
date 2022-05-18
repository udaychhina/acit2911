INSERT INTO user (id, username, [password])
VALUES
  (1, 'testuser', 'pbkdf2:sha256:260000$cIx532rCPut06JUx$a5e5dc14c9017f4ea4ad74139da17880b369789a73348959455a58d844f28946'),
  (2, 'otheruser', 'pbkdf2:sha256:260000$JnwQwi8X2mDfiGMD$c03e0e5e31a6a3a0730bf7c6501c58a59951b6d14ed74ebf85a1389280ce5171');

INSERT INTO hw (course, [name], typehw, [desc], duedate, completed, author_id)
VALUES
  ('test', 'test', 'assignment', 'testtheassignment', '2022-05-05', 'no', 1);