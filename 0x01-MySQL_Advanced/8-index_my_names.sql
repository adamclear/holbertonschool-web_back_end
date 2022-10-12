-- creates an index "idx_name_first" ont the table names & 1st letter of name

CREATE INDEX idx_name_first ON names (name(1));