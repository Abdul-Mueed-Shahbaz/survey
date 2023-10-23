-- Insert Option
INSERT INTO question_option (created_on, update_on, is_active, is_deleted, option_text, is_correct)
VALUES (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, '1', '0', 'Yes', '0');

-- Insert Textual Response
INSERT INTO question_option (created_on, update_on, is_active, is_deleted, option_text, is_correct)
VALUES (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, '1', '0', 'No', '0');