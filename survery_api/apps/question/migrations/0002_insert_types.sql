-- Insert Option
INSERT INTO question_type (created_on, update_on, is_active, is_deleted, name, code)
VALUES (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, '1', '0', 'Radio', 'radio');

-- Insert Textual Response
INSERT INTO question_type (created_on, update_on, is_active, is_deleted, name, code)
VALUES (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, '1', '0', 'Textual Response', 'response');

-- Insert Textual Response
INSERT INTO question_type (created_on, update_on, is_active, is_deleted, name, code)
VALUES (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, '1', '0', 'Checkbox', 'checkbox');