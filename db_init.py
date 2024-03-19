# Criar a estrutura inicial do banco de dados em SQLite

import connection

print(f"Script {__name__} executado.")


def drop_tables():
    """Excluir as tabelas."""

    con, cur = connection.get()

    try:
        cur.execute("DROP TABLE medicos")
        cur.execute("DROP TABLE pacientes")
    except:
        pass

    con.commit()
    con.close()

def tbl_create():
    """Criar as tabelas MEDICOS e PACIENTES."""
    con, cur = connection.get()

    PRIMARY_KEY = (
        "id SERIAL NOT NULL PRIMARY KEY"
        if connection.DB_TYPE == connection.TYPE_PSQL
        else "id integer PRIMARY KEY AUTOINCREMENT"
    )

    cur.execute(
        f"""
            CREATE TABLE IF NOT EXISTS medicos
            (   {PRIMARY_KEY},
                nome varchar(150),
                rg varchar(15),
                cpf varchar(14),
                dt_nasc date,
                sexo varchar(15),
                uf varchar(2),
                cidade varchar(100),
                cep varchar(9),
                logradouro varchar(150),
                crm varchar(10),
                email varchar(100),
                telefone varchar(15),
                especialidade varchar(50),
                turno varchar(20),
                status varchar(20)
            )
        """
    )

    cur.execute(
        f"""
            CREATE TABLE IF NOT EXISTS pacientes
            (   {PRIMARY_KEY},
                nome varchar(150),
                rg varchar(15),
                cpf varchar(14),
                dt_nasc date,
                sexo varchar(15),
                peso integer,
                altura integer,
                tp_sanguineo varchar(3),
                uf varchar(2),
                cidade varchar(100),
                cep varchar(9),
                logradouro varchar(150),
                email varchar(100),
                telefone varchar(15),
                status varchar(20)
            )
        """
    )

    con.commit()
    con.close()

    print("Tabelas criadas.")


def tables_init():
    """Incluir dados iniciais de teste nas tabelas."""

    con, cur = connection.get()

    medicos = [(
            "Rancho Cruxx",
            "12345/SSP-PA",
            "123.456.789-10",
            "1970-01-11",
            "Masculino",
            "DF",
            "Taguatinga",
            "71123-123",
            "Rua 123, lote 3, casa 22",
            "001/PA",
            "rancho_med_cruxx@gmail.com",
            "(61) 98111-1111",
            "Cardiologista",
            "Noturno",
            "Ativo"
            ),
    ]

    pacientes = [
        (
            "Jéssica Vieira Sousa",
            "12345/SSP-MT",
            "123.456.789-10",
            "1998-03-30",
            "Feminino",
            54,
            163,
            "A+",
            "DF",
            "Vicente Pires",
            "71123-123",
            "Rua 123, lote 14, casa 9",
            "jessiquinha@gmail.com",
            "(61) 98222-2222",
            "Agendada"
        ),
    ]

    cur.execute("DELETE FROM medicos")
    cur.execute("DELETE FROM pacientes")

    if connection.DB_TYPE == connection.TYPE_PSQL:
        cur.executemany("INSERT INTO medicos VALUES (DEFAULT,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", medicos)
        cur.executemany("INSERT INTO pacientes VALUES (DEFAULT,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", pacientes)
    else:
        cur.executemany("INSERT INTO medicos VALUES (NULL,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", medicos)
        cur.executemany("INSERT INTO pacientes VALUES (NULL,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", pacientes)
    

    con.commit()
    con.close()

    print("Dados iniciais incluidos nas tabelas.")

if __name__ == "__main__":
    drop_tables()
    tbl_create()
    tables_init()
