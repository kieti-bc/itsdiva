
from token_types import TokenType

class Language_SQL:

	# If this token is specific to this language
	# add it to scanner and return True
	# Otherwise return false
	def scan_token(self, character, scanner):
		if character == ' ':
			return False
		# If is letter, could be keyword
		elif character.isalpha():
			# Go forwards until something else than letter
			while scanner.peek().isalpha() and scanner.isAtEnd() == False:
				# Could be a keyword that contains a space!
				scanner.advance()

			# Is this a space
			if scanner.peek() == ' ' or scanner.isAtEnd():
				text = scanner.get_current_text()
				# see if this part is in some keyword
				for w in self.keywords:
					if w.find(text) >= 0:
						scanner.add_token(TokenType.KEYWORD)
						return True	

		return False

	def is_user_type_keyword(self, word:str):
		return word in Language_SQL.user_type_keywords

	# TODO: SQL is special in that commands can contain
	# spaces

	user_type_keywords = [
	]

	name = "SQL"

	keywords = [
		"ADD",
		"ADD CONSTRAINT",
		"ALL",
		"ALTER",
		"ALTER COLUMN",
		"ALTER TABLE",
		"AND",
		"ANY",
		"AS",
		"ASC",
		"BACKUP DATABASE",
		"BETWEEN",
		"CASE",
		"CHECK",
		"COLUMN",
		"CONSTRAINT",
		"CREATE",
		"CREATE DATABASE",
		"CREATE INDEX",
		"CREATE OR REPLACE VIEW",
		"CREATE TABLE",
		"CREATE PROCEDURE",
		"CREATE UNIQUE INDEX",
		"CREATE VIEW",
		"DATABASE",
		"DEFAULT",
		"DELETE",
		"DESC",
		"DISTINCT",
		"DROP",
		"DROP COLUMN",
		"DROP CONSTRAINT",
		"DROP DATABASE",
		"DROP DEFAULT",
		"DROP INDEX",
		"DROP TABLE",
		"DROP VIEW",
		"EXEC",
		"EXISTS",
		"FOREIGN KEY",
		"FROM",
		"FULL OUTER JOIN",
		"GROUP BY",
		"HAVING",
		"IN",
		"INDEX",
		"INNER JOIN",
		"INSERT INTO",
		"INSERT INTO SELECT",
		"IS NULL",
		"IS NOT NULL",
		"JOIN",
		"LEFT JOIN",
		"LIKE",
		"LIMIT",
		"NOT",
		"NOT NULL",
		"OR",
		"ORDER BY",
		"OUTER JOIN",
		"PRIMARY KEY",
		"PROCEDURE",
		"RIGHT JOIN",
		"ROWNUM",
		"SELECT",
		"SELECT DISTINCT",
		"SELECT INTO",
		"SELECT TOP",
		"SET",
		"TABLE",
		"TOP",
		"TRUNCATE TABLE",
		"UNION",
		"UNION ALL",
		"UNIQUE",
		"UPDATE",
		"VALUES",
		"VIEW",
		"WHERE",
			]

	# Types work like functions, they can have parameters in brackets
	# like INTEGER(16)
	primitive_types = [
		"CHAR",
		"VARCHAR",
		"BINARY",
		"VARBINARY",
		"TINYBLOB",
		"TINYTEXT",
		"TEXT",
		"BLOB",
		"MEDIUMTEXT",
		"MEDIUMBLOB",
		"LONGTEXT",
		"LONGBLOB",
		"ENUM",
		"SET",

		"BIT",
		"TINYINT",
		"BOOL",
		"BOOLEAN",
		"SMALLINT",
		"MEDIUMINT",
		"INT",
		"INTEGER",
		"BIGINT",
		"FLOAT",
		"DOUBLE",
		"DECIMAL",
		"DEC",

		"DATE",
		"DATETIME",
		"TIMESTAMP",
		"TIME",
		"YEAR",
	]

	builtin_types = []
