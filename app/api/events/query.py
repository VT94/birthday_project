SQL = {'Add_person': '''INSERT INTO person(name, birthday) VALUES($1, $2)''',
       'Del_person': '''DELETE FROM person WHERE name=$1'''}